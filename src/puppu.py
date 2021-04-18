import random
from pathlib import Path
from .inflect import inflect_nominal, conjugate_verb


def main():
    generate = PuppuGenerator()

    for _ in range(10):
        print(generate())


class PuppuGenerator:
    def __init__(self):
        self.vocab = self.load_vocabulary()

    def __call__(self):
        cases = ['Nom', 'Gen', 'Acc', 'Par', 'Ess', 'Tra', 'Ine', 'Ela', 'Ill', 'Ade', 'Abl', 'All']
        case_weights = [1]*len(cases)
        case_weights[0] = 10

        case = random.choices(cases, case_weights)[0]
        number = random.choices(['Sing', 'Plur'], [3, 1])[0]
        adj = random.choice(self.vocab['laatusana'])
        noun = random.choice(self.vocab['nimisana'])
        verb = random.choice(self.vocab['teonsana'])
        tense = random.choices(['Pres', 'Past'], [2, 1])
        obj = random.choice(self.vocab['nimisana'])
        obj_case = random.choices(['Par', 'Gen'], [2, 1])[0]

        return (inflect_nominal(adj, case=case, number=number) + ' ' +
                inflect_nominal(noun, case=case, number=number) + ' ' +
                conjugate_verb(verb, tense=tense, person='3', number=number, mood='Ind') + ' ' +
                inflect_nominal(obj, case=obj_case, number='Sing'))

    def load_vocabulary(self):
        vocab = {}
        vocab_path = Path('data/vocab')
        for f in vocab_path.glob('*.txt'):
            vocab[f.stem] = [x.strip() for x in f.open('r', encoding='utf-8').readlines()]
        return vocab


if __name__ == '__main__':
    main()
