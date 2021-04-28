import gzip
from itertools import islice
from pathlib import Path
from voikko import libvoikko

voikko = libvoikko.Voikko("fi")

ignored_pos = {'kieltosana', 'huudahdussana', 'lyhenne', 'asemosana', 'sidesana', 'etuliite', 'etunimi'}
simplify_pos = {
    'nimisana_laatusana': 'laatusana',
    'nimi': 'nimisana',
    'paikannimi': 'nimisana',
    'sukunimi': 'nimisana',
}
lexemes_by_pos = {
    'nimisana': set(),
    'laatusana': set(),
    'lukusana': set(),
    'teonsana': set(),
    'suhdesana': set(),
    'seikkasana': set(),
}

def main():
    infile = 'data/finnish_vocab/finnish_vocab.txt.gz'
    words = []
    frequencies = {}
    with gzip.open(infile, 'rt', encoding='utf-8') as f:
        for line in f:
            freq, token = line.strip().rsplit(' ', 1)
            words.append(token)
            frequencies[token] = int(freq)

        for token in islice(words, 1000000):
            token = token.strip('-').strip(';').strip('"')
            analyses = analyze(token)
            if len(analyses) > 1:
                analyses = [x for x in analyses if x['BASEFORM'] in frequencies] or analyses

            for analysis in analyses:
                sanaluokka = analysis.get('CLASS')
                baseform = analysis.get('BASEFORM')
                sanaluokka = simplify_pos.get(sanaluokka, sanaluokka)
                if baseform and sanaluokka and sanaluokka not in ignored_pos:
                    lexemes_by_pos[sanaluokka].add(baseform)

    outpath = Path('data/vocab')
    outpath.mkdir(parents=True)
    print(f'Writing vocabulary files to {outpath}')
    for pos, lexemes in lexemes_by_pos.items():
        with open(outpath / (pos + '.txt'), 'w', encoding='utf-8') as outf:
            for lex in lexemes:
                outf.write(lex)
                outf.write('\n')


def analyze(token):
    analyses = voikko.analyze(token)

    new_analyses = []
    for analysis in analyses:
        if analysis.get('CLASS') == 'seikkasana' and token.lower().endswith('itse'):
            analysis['BASEFORM'] = token.lower()
        elif (analysis.get('CLASS') in ['laatusana', 'lukusana'] and
              analysis.get('SIJAMUOTO') == 'kerrontosti' and
              'FOCUS' not in analysis and
              'KYSYMYSLIITE' not in analysis):
            new_analyses.append({
                'BASEFORM': token.lower(),
                'CLASS': 'seikkasana',
                'SIJAMUOTO': 'kerrontosti',
                'STRUCTURE': analysis['STRUCTURE'],
                'WORDBASES': analysis['WORDBASES']
            })

    return analyses + new_analyses


if __name__ == '__main__':
    main()
