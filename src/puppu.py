import random
from pathlib import Path
from .inflect import conjugate_verb, inflect_nominal, inflect_pronoun

punctuation = '.,:;!?'

class Vocabulary:
    def __init__(self):
        self.vocabulary = self.load_vocabulary()

    def load_vocabulary(self):
        vocab = {}
        vocab_path = Path('data/vocab')
        for f in vocab_path.glob('*.txt'):
            words = []
            weights = []
            for line in f.open('r', encoding='utf-8'):
                line = line.strip()
                if ' ' in line:
                    freq, word = line.split(' ', 1)
                    freq = float(freq)
                else:
                    word = line
                    freq = 1.0
                words.append(word)
                weights.append(freq)
            vocab[f.stem] = (words, weights)
        return vocab

    def random_word(self, word_class):
        if word_class in self.vocabulary:
            words, weights = self.vocabulary[word_class]
            return random.choices(words, weights=weights)[0]
        else:
            return ''


class Grammar:
    def __init__(self, rules):
        self.validate_rules(rules)
        self.rules = rules

    def get(self, key):
        return self.rules.get(key)

    def validate_rules(self, rules):
        known_rule_names = set(rules.keys())
        known_word_classes = ['teonsana', 'nimisana', 'laatusana', 'lukusana',
                              'asemosana', 'seikkasana', 'sidesana', 'välimerkki']
        for _, rule_alternatives in rules.items():
            for rule_list in rule_alternatives:
                for rule in rule_list:
                    if isinstance(rule, Optional):
                        rule = rule.rule

                    if isinstance(rule, Rule):
                        if rule.name not in known_rule_names:
                            raise ValueError(f'Reference to unknown rule: {rule.name}')

                    if isinstance(rule, Terminal):
                        if rule.word_class not in known_word_classes:
                            raise ValueError(f'Unknown word class: {rule.word_class}')

    def generate(self, rule_name, vocabulary):
        attributes = {
            'case': 'Nom',
            'number': random.choice(['Sing', 'Plur']),
            'person': '3',
            'tense': random.choice(['Pres', 'Past']),
            'mood': 'Ind',
        }
        tokens = self._generate_recursive(rule_name, vocabulary, attributes)
        if tokens and tokens[-1] not in '.?!':
            tokens.append('.')
        text = ''
        for token in tokens:
            if text and token not in punctuation:
                text += ' '
            elif text and token in punctuation and text[-1] in punctuation:
                text = text[:-1]
            text += token

        if text:
            text = text[0].upper() + text[1:]
        return text

    def _generate_recursive(self, rule_name, vocabulary, attributes):
        generated = []
        options = self.rules.get(rule_name)
        for rule in random.choice(options):
            if isinstance(rule, Optional):
                if random.random() < rule.p:
                    rule = rule.rule
                else:
                    continue

            attributes2 = {**attributes, **rule.attributes}
            
            if isinstance(rule, Rule):
                generated.extend(self._generate_recursive(rule.name, vocabulary, attributes2))
            elif isinstance(rule, Terminal):
                inflected = self._inflect(rule.get_lexeme(vocabulary), rule.word_class, attributes2)
                generated.append(inflected)
            else:
                raise ValueError(f'Unknown rule: {rule}')

        return generated

    def _inflect(self, lexeme, word_class, attributes):
        if word_class == 'teonsana':
            return conjugate_verb(
                lexeme,
                tense=attributes.get('tense'),
                person=attributes.get('person'),
                number=attributes.get('number'),
                mood=attributes.get('mood'),
                infform=attributes.get('infform'),
                partform=attributes.get('partform'),
                connegative=attributes.get('connegative'))
        elif word_class in ['laatusana', 'lukusana', 'nimisana']:
            return inflect_nominal(
                lexeme,
                case=attributes.get('case'),
                number=attributes.get('number'),
                degree=attributes.get('degree'),
                person_psor=attributes.get('person_psor'),
                number_psor=attributes.get('number_psor'))
        elif word_class == 'asemosana':
            return inflect_pronoun(
                lexeme,
                case=attributes.get('case'),
                number=attributes.get('number'))
        else:
            return lexeme


class Rule:
    def __init__(self, name, **kwargs):
        self.name = name
        self.attributes = kwargs


class Terminal:
    def __init__(self, word_class, lexeme=None, **kwargs):
        self.word_class = word_class
        self.lexeme = lexeme
        self.attributes = kwargs

    def get_lexeme(self, vocabulary):
        if isinstance(self.lexeme, str):
            return self.lexeme
        elif self.lexeme is not None:
            return random.choice(self.lexeme)
        else:
            return vocabulary.random_word(self.word_class)


class Punct(Terminal):
    def __init__(self, punctuation_character):
        super().__init__('välimerkki', punctuation_character)


class Optional:
    def __init__(self, rule, p=0.5):
        self.rule = rule
        self.p = p


R = Rule
grammar = Grammar({
    'SENTENCE': [
        # declarative sentence
        [R('NP', case='Nom'), R('VP', person='3')],
        [R('NP', case='Nom'), R('VP', person='3')], # Repeated to make this clause type more common

        # passive
        [R('NP', case='Ine'), R('VPass'), Optional(R('AdvP'), 0.2)],

        # conditional
        [R('NP', case='Nom'),
         R('V', person='3', mood='Cnd'),
         R('OBJECTIVE'),
         Optional(R('AdvP'), 0.2)],

        # subordinate clause
        [R('SENTENCE'),
         Punct(','),
         Terminal('asemosana', ['että', 'jotta', 'koska', 'kun', 'jos', 'vaikka',
                                'kunnes', 'mikäli', 'eli', 'ja', 'mutta', 'tai']),
         R('SENTENCE'),
         Punct(',')],

        # interrogative clause
        [Terminal('asemosana', ['mikä', 'kuka']), R('VP', person='3'), Punct('?')],

        # omistuslause: https://kaino.kotus.fi/visk/sisallys.php?p=895
        [R('NP', case='Ade'),
         Terminal('teonsana', 'olla', person='3', number='Sing'),
         R('NP', case='Nom')],

        # tuloslause: https://kaino.kotus.fi/visk/sisallys.php?p=904
        [R('NP', case='Ela'),
         Terminal('teonsana', ['tulla', 'kehittyä', 'muodostua'], person='3', number='Sing'),
         R('PREDICATIVE')]
    ],
    'OBJECTIVE': [
        [R('NP', case='Gen')],
        [R('NP', case='Par')],
        [Terminal('asemosana', 'minä', case='Par')],
        [Terminal('asemosana', 'sinä', case='Par')],
        [Terminal('asemosana', 'hän', case='Par')],
    ],
    'PREDICATIVE': [
        [R('NP', case='Nom')],
        [R('AP', case='Nom')],
        [Terminal('laatusana', case='Nom', degree='Cmp'),
         Terminal('sidesana', 'kuin'),
         R('N', case='Nom')],
    ],
    'VP': [
        [R('V'), Optional(R('AdvP'), 0.5)],
        [R('V'), R('OBJECTIVE'), Optional(R('AdvP'), 0.2)],

        [R('V'), Optional(R('AdvP'), 0.2)],

        # predicative
        [Terminal('teonsana', 'olla'), R('PREDICATIVE')],
    ],
    'NP': [
        [R('N')],
        [R('AP'), R('N')],
        [R('NP', case='Gen'), R('N')],
        [R('NPPron')],
        [R('NP'),
         Punct(','),
         Terminal('asemosana', ['joka', 'mikä']),
         R('VP'),
         Punct(',')]
    ],
    'NPPron': [
        [Optional(Terminal('asemosana', 'minä', case='Gen', number='Sing')),
         Optional(R('AP')),
         R('N', person_psor='1', number_psor='Sing')],
        [Optional(Terminal('asemosana', 'sinä', case='Gen', number='Sing')),
         Optional(R('AP')),
         R('N', person_psor='2', number_psor='Sing')],
        [Optional(Terminal('asemosana', 'minä', case='Gen', number='Plur')),
         Optional(R('AP')),
         R('N', person_psor='1', number_psor='Plur')],
        [Optional(Terminal('asemosana', 'sinä', case='Gen', number='Plur')),
         Optional(R('AP')),
         R('N', person_psor='2', number_psor='Plur')],
    ],
    'AP': [
        [Terminal('laatusana')],
    ],
    'V': [
        [Terminal('teonsana')],
        [Terminal('teonsana', 'ei'),
         Optional(Terminal('seikkasana', ['koskaan', 'kuitenkaan', 'aina', 'onneksi', 'ehkä', 'enää']), 0.2),
         Terminal('teonsana', person='3', connegative=True)],
        [Terminal('teonsana', 'olla'), Terminal('teonsana', partform='Past')],
        [Terminal('teonsana', 'ei'),
         Terminal('teonsana', 'olla', person='3', connegative=True),
         Terminal('teonsana', partform='Past')],
        [Terminal('teonsana', ['alkaa', 'ehtiä', 'meinata', 'saada', 'saattaa',
                               'tahtoa', 'taitaa', 'uhata', 'voida']),
         Terminal('teonsana', infform='1')]
    ],
    'VPass': [
        [Terminal('teonsana', person='4')],
        [Terminal('teonsana', 'ei', person='4'),
         Optional(Terminal('seikkasana', ['koskaan', 'kuitenkaan', 'aina', 'onneksi', 'ehkä', 'enää']), 0.2),
         Terminal('teonsana', person='4', connegative=True)],
        [Terminal('teonsana', 'olla', person='3', number='Sing'),
         Terminal('teonsana', person='4', partform='Past')],
    ],
    'N': [
        [Terminal('nimisana')]
    ],
    'AdvP': [
        [Terminal('seikkasana')]
    ]
})
vocabulary = Vocabulary()

for _ in range(10):
    print(grammar.generate('SENTENCE', vocabulary))
