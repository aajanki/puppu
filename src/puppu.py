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
            vocab[f.stem] = [x.strip() for x in f.open('r', encoding='utf-8').readlines()]
        return vocab

    def random_word(self, word_class):
        return random.choice(self.vocabulary.get(word_class, ''))


class Grammar:
    def __init__(self, rules):
        self.rules = rules

    def get(self, key):
        return self.rules.get(key)

    def generate(self, rule_name, vocabulary):
        attributes = {
            'case': 'Nom',
            'number': random.choice(['Sing', 'Plur']),
            'person': random.choice(['1', '2', '3']),
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
                if rule.lexeme:
                    lexeme = rule.lexeme
                else:
                    lexeme = vocabulary.random_word(rule.word_class)
                inflected = self._inflect(lexeme, rule.word_class, attributes2)
                generated.append(inflected)
            else:
                raise ValueError(f'Unknown rule: {rule}')

        return generated

    def _inflect(self, lexeme, word_class, attributes):
        if word_class == 'teonsana':
            return conjugate_verb(
                lexeme,
                tense=attributes.get('tense', 'Pres'),
                person=attributes.get('person', '1'),
                number=attributes.get('number', 'Sing'),
                mood=attributes.get('mood', 'Ind'))
        elif word_class in ['laatusana', 'lukusana', 'nimisana']:
            return inflect_nominal(
                lexeme,
                case=attributes.get('case', 'Nom'),
                number=attributes.get('number', 'Sing'),
                degree=attributes.get('degree', 'Pos'),
                person_psor=attributes.get('person_psor'),
                number_psor=attributes.get('number_psor'))
        elif word_class == 'asemosana':
            return inflect_pronoun(
                lexeme,
                case=attributes.get('case', 'Nom'),
                number=attributes.get('number', 'Sing'))
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


class Optional:
    def __init__(self, rule, p=0.5):
        self.rule = rule
        self.p = p
        

R = Rule
Comma = Terminal('välimerkki', ',')
grammar = Grammar({
    'SENTENCE': [
        [R('NP'), R('V', person='3'), Optional(R('AdvP'), 0.5)],
        [R('NP'), R('V', person='3'), R('OBJECTIVE'), Optional(R('AdvP'), 0.2)],

        # predicative
        [R('NP'), Terminal('teonsana', 'olla', person='3'), R('PREDICATIVE')],

        # passive
        [R('V', person='4'), Optional(R('AdvP'), 0.2)],
        [R('NP', case='Ine'), R('V', person='4'), Optional(R('AdvP'), 0.2)],

        # conditional
        [R('NP', case='Nom'),
         R('V', person='3', mood='Cnd'),
         R('OBJECTIVE'),
         Optional(R('AdvP'), 0.2)],
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
    ],
    'NP': [
        [R('N')],
        [R('AP'), R('N')],
        [R('NP', case='Gen'), R('N')],
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
        [R('NP'),
         Comma,
         Terminal('asemosana', 'joka'),
         Terminal('teonsana', 'olla', person='3'),
         R('PREDICATIVE'),
         Comma]
    ],
    'AP': [
        [Terminal('laatusana')],
    ],
    'V': [
        [Terminal('teonsana')]
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
