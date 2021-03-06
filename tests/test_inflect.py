import pytest
from src.inflect import conjugate_verb, inflect_nominal, inflect_pronoun

ACTIVE_INDICATIVE_EXAMPLES = [
    (
        {'token': 'ostaa', 'tense': 'Pres', 'person': '1', 'number': 'Sing', 'mood': 'Ind'},
        'ostan'
    ),
    (
        {'token': 'ostaa', 'tense': 'Pres', 'person': '2', 'number': 'Sing', 'mood': 'Ind'},
        'ostat'
    ),
    (
        {'token': 'ostaa', 'tense': 'Pres', 'person': '3', 'number': 'Sing', 'mood': 'Ind'},
        'ostaa'
    ),
    (
        {'token': 'ostaa', 'tense': 'Pres', 'person': '1', 'number': 'Plur', 'mood': 'Ind'},
        'ostamme'
    ),
    (
        {'token': 'ostaa', 'tense': 'Pres', 'person': '2', 'number': 'Plur', 'mood': 'Ind'},
        'ostatte'
    ),
    (
        {'token': 'ostaa', 'tense': 'Pres', 'person': '3', 'number': 'Plur', 'mood': 'Ind'},
        'ostavat'
    ),
    (
        {'token': 'ostaa', 'tense': 'Past', 'person': '1', 'number': 'Sing', 'mood': 'Ind'},
        'ostin'
    ),
    (
        {'token': 'ostaa', 'tense': 'Past', 'person': '2', 'number': 'Sing', 'mood': 'Ind'},
        'ostit'
    ),
    (
        {'token': 'ostaa', 'tense': 'Past', 'person': '3', 'number': 'Sing', 'mood': 'Ind'},
        'osti'
    ),
    (
        {'token': 'ostaa', 'tense': 'Past', 'person': '1', 'number': 'Plur', 'mood': 'Ind'},
        'ostimme'
    ),
    (
        {'token': 'ostaa', 'tense': 'Past', 'person': '2', 'number': 'Plur', 'mood': 'Ind'},
        'ostitte'
    ),
    (
        {'token': 'ostaa', 'tense': 'Past', 'person': '3', 'number': 'Plur', 'mood': 'Ind'},
        'ostivat'
    ),
    (
        {'token': 'kadota', 'tense': 'Pres', 'person': '1', 'number': 'Sing', 'mood': 'Ind'},
        'katoan'
    ),
    (
        {'token': 'kadota', 'tense': 'Pres', 'person': '2', 'number': 'Sing', 'mood': 'Ind'},
        'katoat'
    ),
    (
        {'token': 'kadota', 'tense': 'Pres', 'person': '3', 'number': 'Sing', 'mood': 'Ind'},
        'katoaa'
    ),
    (
        {'token': 'kadota', 'tense': 'Pres', 'person': '1', 'number': 'Plur', 'mood': 'Ind'},
        'katoamme'
    ),
    (
        {'token': 'kadota', 'tense': 'Pres', 'person': '2', 'number': 'Plur', 'mood': 'Ind'},
        'katoatte'
    ),
    (
        {'token': 'kadota', 'tense': 'Pres', 'person': '3', 'number': 'Plur', 'mood': 'Ind'},
        'katoavat'
    ),
    (
        {'token': 'kadota', 'tense': 'Past', 'person': '1', 'number': 'Sing', 'mood': 'Ind'},
        'katosin'
    ),
    (
        {'token': 'kadota', 'tense': 'Past', 'person': '2', 'number': 'Sing', 'mood': 'Ind'},
        'katosit'
    ),
    (
        {'token': 'kadota', 'tense': 'Past', 'person': '3', 'number': 'Sing', 'mood': 'Ind'},
        'katosi'
    ),
    (
        {'token': 'kadota', 'tense': 'Past', 'person': '1', 'number': 'Plur', 'mood': 'Ind'},
        'katosimme'
    ),
    (
        {'token': 'kadota', 'tense': 'Past', 'person': '2', 'number': 'Plur', 'mood': 'Ind'},
        'katositte'
    ),
    (
        {'token': 'kadota', 'tense': 'Past', 'person': '3', 'number': 'Plur', 'mood': 'Ind'},
        'katosivat'
    ),
    (
        {'token': 'lähteä', 'tense': 'Pres', 'person': '1', 'number': 'Sing', 'mood': 'Ind'},
        'lähden'
    ),
    (
        {'token': 'lähteä', 'tense': 'Pres', 'person': '2', 'number': 'Sing', 'mood': 'Ind'},
        'lähdet'
    ),
    (
        {'token': 'lähteä', 'tense': 'Pres', 'person': '3', 'number': 'Sing', 'mood': 'Ind'},
        'lähtee'
    ),
    (
        {'token': 'lähteä', 'tense': 'Pres', 'person': '1', 'number': 'Plur', 'mood': 'Ind'},
        'lähdemme'
    ),
    (
        {'token': 'lähteä', 'tense': 'Pres', 'person': '2', 'number': 'Plur', 'mood': 'Ind'},
        'lähdette'
    ),
    (
        {'token': 'lähteä', 'tense': 'Pres', 'person': '3', 'number': 'Plur', 'mood': 'Ind'},
        'lähtevät'
    ),
    (
        {'token': 'lähteä', 'tense': 'Past', 'person': '1', 'number': 'Sing', 'mood': 'Ind'},
        'lähdin'
    ),
    (
        {'token': 'lähteä', 'tense': 'Past', 'person': '2', 'number': 'Sing', 'mood': 'Ind'},
        'lähdit'
    ),
    (
        {'token': 'lähteä', 'tense': 'Past', 'person': '3', 'number': 'Sing', 'mood': 'Ind'},
        'lähti'
    ),
    (
        {'token': 'lähteä', 'tense': 'Past', 'person': '1', 'number': 'Plur', 'mood': 'Ind'},
        'lähdimme'
    ),
    (
        {'token': 'lähteä', 'tense': 'Past', 'person': '2', 'number': 'Plur', 'mood': 'Ind'},
        'lähditte'
    ),
    (
        {'token': 'lähteä', 'tense': 'Past', 'person': '3', 'number': 'Plur', 'mood': 'Ind'},
        'lähtivät'
    ),
    (
        {'token': 'uida', 'tense': 'Pres', 'person': '1', 'number': 'Sing', 'mood': 'Ind'},
        'uin'
    ),
    (
        {'token': 'uida', 'tense': 'Pres', 'person': '2', 'number': 'Sing', 'mood': 'Ind'},
        'uit'
    ),
    (
        {'token': 'uida', 'tense': 'Pres', 'person': '3', 'number': 'Sing', 'mood': 'Ind'},
        'ui'
    ),
    (
        {'token': 'uida', 'tense': 'Pres', 'person': '1', 'number': 'Plur', 'mood': 'Ind'},
        'uimme'
    ),
    (
        {'token': 'uida', 'tense': 'Pres', 'person': '2', 'number': 'Plur', 'mood': 'Ind'},
        'uitte'
    ),
    (
        {'token': 'uida', 'tense': 'Pres', 'person': '3', 'number': 'Plur', 'mood': 'Ind'},
        'uivat'
    ),
    (
        {'token': 'uida', 'tense': 'Past', 'person': '1', 'number': 'Sing', 'mood': 'Ind'},
        'uin'
    ),
    (
        {'token': 'uida', 'tense': 'Past', 'person': '2', 'number': 'Sing', 'mood': 'Ind'},
        'uit'
    ),
    (
        {'token': 'uida', 'tense': 'Past', 'person': '3', 'number': 'Sing', 'mood': 'Ind'},
        'ui'
    ),
    (
        {'token': 'uida', 'tense': 'Past', 'person': '1', 'number': 'Plur', 'mood': 'Ind'},
        'uimme'
    ),
    (
        {'token': 'uida', 'tense': 'Past', 'person': '2', 'number': 'Plur', 'mood': 'Ind'},
        'uitte'
    ),
    (
        {'token': 'uida', 'tense': 'Past', 'person': '3', 'number': 'Plur', 'mood': 'Ind'},
        'uivat'
    ),
    (
        {'token': 'nähdä', 'tense': 'Past', 'person': '2', 'number': 'Sing', 'mood': 'Ind'},
        'näit'
    ),
    (
        {'token': 'nähdä', 'tense': 'Past', 'person': '3', 'number': 'Sing', 'mood': 'Ind'},
        'näki'
    ),
    (
        {'token': 'nähdä', 'tense': 'Past', 'person': '2', 'number': 'Plur', 'mood': 'Ind'},
        'näitte'
    ),
    (
        {'token': 'nähdä', 'tense': 'Past', 'person': '3', 'number': 'Plur', 'mood': 'Ind'},
        'näkivät'
    ),
    (
        {'token': 'alkaa', 'tense': 'Pres', 'person': '2', 'number': 'Sing', 'mood': 'Ind'},
        'alat'
    ),
    (
        {'token': 'alkaa', 'tense': 'Pres', 'person': '3', 'number': 'Sing', 'mood': 'Ind'},
        'alkaa'
    ),
    (
        {'token': 'alkaa', 'tense': 'Pres', 'person': '3', 'number': 'Plur', 'mood': 'Ind'},
        'alkavat'
    ),
    (
        {'token': 'alkaa', 'tense': 'Past', 'person': '2', 'number': 'Plur', 'mood': 'Ind'},
        'aloitte'
    ),
    (
        {'token': 'alkaa', 'tense': 'Past', 'person': '3', 'number': 'Plur', 'mood': 'Ind'},
        'alkoivat'
    ),
    (
        {'token': 'meinata', 'tense': 'Pres', 'person': '3', 'number': 'Sing', 'mood': 'Ind'},
        'meinaa'
    ),
    (
        {'token': 'uhata', 'tense': 'Past', 'person': '2', 'number': 'Sing', 'mood': 'Ind'},
        'uhkasit'
    ),
    (
        {'token': 'uhata', 'tense': 'Past', 'person': '3', 'number': 'Sing', 'mood': 'Ind'},
        'uhkasi'
    ),
    (
        {'token': 'uhata', 'tense': 'Past', 'person': '2', 'number': 'Plur', 'mood': 'Ind'},
        'uhkasitte'
    ),
    (
        {'token': 'uhata', 'tense': 'Past', 'person': '3', 'number': 'Plur', 'mood': 'Ind'},
        'uhkasivat'
    ),
    (
        {'token': 'kumartaa', 'tense': 'Past', 'person': '1', 'number': 'Sing', 'mood': 'Ind'},
        'kumarsin'
    ),
    (
        {'token': 'kumartaa', 'tense': 'Past', 'person': '3', 'number': 'Sing', 'mood': 'Ind'},
        'kumarsi'
    ),
    (
        {'token': 'olla', 'tense': 'Pres', 'person': '1', 'number': 'Sing', 'mood': 'Ind'},
        'olen'
    ),
    (
        {'token': 'olla', 'tense': 'Pres', 'person': '2', 'number': 'Sing', 'mood': 'Ind'},
        'olet'
    ),
    (
        {'token': 'olla', 'tense': 'Pres', 'person': '3', 'number': 'Sing', 'mood': 'Ind'},
        'on'
    ),
    (
        {'token': 'olla', 'tense': 'Pres', 'person': '1', 'number': 'Plur', 'mood': 'Ind'},
        'olemme'
    ),
    (
        {'token': 'olla', 'tense': 'Pres', 'person': '2', 'number': 'Plur', 'mood': 'Ind'},
        'olette'
    ),
    (
        {'token': 'olla', 'tense': 'Pres', 'person': '3', 'number': 'Plur', 'mood': 'Ind'},
        'ovat'
    ),
    (
        {'token': 'olla', 'tense': 'Past', 'person': '1', 'number': 'Sing', 'mood': 'Ind'},
        'olin'
    ),
    (
        {'token': 'olla', 'tense': 'Past', 'person': '2', 'number': 'Sing', 'mood': 'Ind'},
        'olit'
    ),
    (
        {'token': 'olla', 'tense': 'Past', 'person': '3', 'number': 'Sing', 'mood': 'Ind'},
        'oli'
    ),
    (
        {'token': 'olla', 'tense': 'Past', 'person': '1', 'number': 'Plur', 'mood': 'Ind'},
        'olimme'
    ),
    (
        {'token': 'olla', 'tense': 'Past', 'person': '2', 'number': 'Plur', 'mood': 'Ind'},
        'olitte'
    ),
    (
        {'token': 'olla', 'tense': 'Past', 'person': '3', 'number': 'Plur', 'mood': 'Ind'},
        'olivat'
    ),

    # pääverbin kieltomuoto
    (
        {'token': 'olla', 'tense': 'Pres', 'person': '1', 'number': 'Sing', 'mood': 'Ind', 'connegative': True},
        'ole'
    ),
    (
        {'token': 'olla', 'tense': 'Pres', 'person': '2', 'number': 'Sing', 'mood': 'Ind', 'connegative': True},
        'ole'
    ),
    (
        {'token': 'olla', 'tense': 'Pres', 'person': '3', 'number': 'Sing', 'mood': 'Ind', 'connegative': True},
        'ole'
    ),
    (
        {'token': 'olla', 'tense': 'Pres', 'person': '1', 'number': 'Plur', 'mood': 'Ind', 'connegative': True},
        'ole'
    ),
    (
        {'token': 'olla', 'tense': 'Pres', 'person': '2', 'number': 'Plur', 'mood': 'Ind', 'connegative': True},
        'ole'
    ),
    (
        {'token': 'olla', 'tense': 'Pres', 'person': '3', 'number': 'Plur', 'mood': 'Ind', 'connegative': True},
        'ole'
    ),
    (
        {'token': 'olla', 'tense': 'Past', 'person': '1', 'number': 'Sing', 'mood': 'Ind', 'connegative': True},
        'ollut'
    ),
    (
        {'token': 'kävellä', 'tense': 'Pres', 'person': '1', 'number': 'Sing', 'mood': 'Ind', 'connegative': True},
        'kävele'
    ),
    (
        {'token': 'kävellä', 'tense': 'Pres', 'person': '2', 'number': 'Sing', 'mood': 'Ind', 'connegative': True},
        'kävele'
    ),
    (
        {'token': 'kävellä', 'tense': 'Pres', 'person': '3', 'number': 'Sing', 'mood': 'Ind', 'connegative': True},
        'kävele'
    ),
    (
        {'token': 'kävellä', 'tense': 'Pres', 'person': '1', 'number': 'Plur', 'mood': 'Ind', 'connegative': True},
        'kävele'
    ),
    (
        {'token': 'kävellä', 'tense': 'Pres', 'person': '2', 'number': 'Plur', 'mood': 'Ind', 'connegative': True},
        'kävele'
    ),
    (
        {'token': 'kävellä', 'tense': 'Pres', 'person': '3', 'number': 'Plur', 'mood': 'Ind', 'connegative': True},
        'kävele'
    ),
    (
        {'token': 'kävellä', 'tense': 'Pres', 'person': '2', 'number': 'Sing', 'mood': 'Cnd', 'connegative': True},
        'kävelisi'
    ),
    (
        {'token': 'kävellä', 'tense': 'Pres', 'person': '2', 'number': 'Sing', 'mood': 'Imp', 'connegative': True},
        'kävele'
    ),
    (
        {'token': 'kävellä', 'tense': 'Past', 'person': '2', 'number': 'Sing', 'mood': 'Ind', 'connegative': True},
        'kävellyt'
    ),
    (
        {'token': 'kävellä', 'tense': 'Past', 'person': '2', 'number': 'Plur', 'mood': 'Ind', 'connegative': True},
        'kävelleet'
    ),
    (
        {'token': 'kävellä', 'tense': 'Past', 'person': '2', 'number': 'Sing', 'mood': 'Cnd', 'connegative': True},
        'kävelisi'
    ),
    (
        {'token': 'olla', 'tense': 'Pres', 'person': '4', 'number': 'Sing', 'mood': 'Ind', 'connegative': True},
        'olla'
    ),
    (
        {'token': 'kävellä', 'tense': 'Pres', 'person': '4', 'number': 'Sing', 'mood': 'Ind', 'connegative': True},
        'kävellä'
    ),
    (
        {'token': 'hautoa', 'tense': 'Pres', 'person': '4', 'number': 'Sing', 'mood': 'Ind', 'connegative': True},
        'haudota'
    ),
    (
        {'token': 'syödä', 'tense': 'Pres', 'person': '4', 'number': 'Sing', 'mood': 'Ind', 'connegative': True},
        'syödä'
    ),
    (
        {'token': 'kertoa', 'tense': 'Pres', 'person': '4', 'number': 'Sing', 'mood': 'Imp', 'connegative': True},
        'kerrottako'
    ),
    (
        {'token': 'suudella', 'tense': 'Past', 'person': '4', 'number': 'Sing', 'mood': 'Ind', 'connegative': True},
        'suudeltu'
    ),
]

ACTIVE_CONDITIONAL_EXAMPLES = [
    (
        {'token': 'näyttää', 'tense': 'Pres', 'person': '1', 'number': 'Sing', 'mood': 'Cnd'},
        'näyttäisin',
    ),
    (
        {'token': 'näyttää', 'tense': 'Pres', 'person': '2', 'number': 'Sing', 'mood': 'Cnd'},
        'näyttäisit',
    ),
    (
        {'token': 'näyttää', 'tense': 'Pres', 'person': '3', 'number': 'Sing', 'mood': 'Cnd'},
        'näyttäisi',
    ),
    (
        {'token': 'näyttää', 'tense': 'Pres', 'person': '1', 'number': 'Plur', 'mood': 'Cnd'},
        'näyttäisimme',
    ),
    (
        {'token': 'näyttää', 'tense': 'Pres', 'person': '2', 'number': 'Plur', 'mood': 'Cnd'},
        'näyttäisitte',
    ),
    (
        {'token': 'näyttää', 'tense': 'Pres', 'person': '3', 'number': 'Plur', 'mood': 'Cnd'},
        'näyttäisivät',
    ),
    (
        {'token': 'näyttää', 'tense': 'Past', 'person': '1', 'number': 'Sing', 'mood': 'Cnd'},
        'näyttäisin',
    ),
    (
        {'token': 'näyttää', 'tense': 'Past', 'person': '2', 'number': 'Sing', 'mood': 'Cnd'},
        'näyttäisit',
    ),
    (
        {'token': 'näyttää', 'tense': 'Past', 'person': '3', 'number': 'Sing', 'mood': 'Cnd'},
        'näyttäisi',
    ),
    (
        {'token': 'näyttää', 'tense': 'Past', 'person': '1', 'number': 'Plur', 'mood': 'Cnd'},
        'näyttäisimme',
    ),
    (
        {'token': 'näyttää', 'tense': 'Past', 'person': '2', 'number': 'Plur', 'mood': 'Cnd'},
        'näyttäisitte',
    ),
    (
        {'token': 'näyttää', 'tense': 'Past', 'person': '3', 'number': 'Plur', 'mood': 'Cnd'},
        'näyttäisivät',
    ),
    (
        {'token': 'haluta', 'tense': 'Pres', 'person': '1', 'number': 'Sing', 'mood': 'Cnd'},
        'haluaisin',
    ),
    (
        {'token': 'haluta', 'tense': 'Pres', 'person': '2', 'number': 'Sing', 'mood': 'Cnd'},
        'haluaisit',
    ),
    (
        {'token': 'haluta', 'tense': 'Pres', 'person': '3', 'number': 'Sing', 'mood': 'Cnd'},
        'haluaisi',
    ),
    (
        {'token': 'haluta', 'tense': 'Pres', 'person': '1', 'number': 'Plur', 'mood': 'Cnd'},
        'haluaisimme',
    ),
    (
        {'token': 'haluta', 'tense': 'Pres', 'person': '2', 'number': 'Plur', 'mood': 'Cnd'},
        'haluaisitte',
    ),
    (
        {'token': 'haluta', 'tense': 'Pres', 'person': '3', 'number': 'Plur', 'mood': 'Cnd'},
        'haluaisivat',
    ),
    (
        {'token': 'lykätä', 'tense': 'Pres', 'person': '1', 'number': 'Sing', 'mood': 'Cnd'},
        'lykkäisin',
    ),
    (
        {'token': 'lykätä', 'tense': 'Pres', 'person': '2', 'number': 'Sing', 'mood': 'Cnd'},
        'lykkäisit',
    ),
    (
        {'token': 'lykätä', 'tense': 'Pres', 'person': '3', 'number': 'Sing', 'mood': 'Cnd'},
        'lykkäisi',
    ),
    (
        {'token': 'lykätä', 'tense': 'Pres', 'person': '1', 'number': 'Plur', 'mood': 'Cnd'},
        'lykkäisimme',
    ),
    (
        {'token': 'lykätä', 'tense': 'Pres', 'person': '2', 'number': 'Plur', 'mood': 'Cnd'},
        'lykkäisitte',
    ),
    (
        {'token': 'lykätä', 'tense': 'Pres', 'person': '3', 'number': 'Plur', 'mood': 'Cnd'},
        'lykkäisivät',
    ),
    (
        {'token': 'taitaa', 'tense': 'Pres', 'person': '1', 'number': 'Sing', 'mood': 'Cnd'},
        'taitaisin',
    ),
    (
        {'token': 'taitaa', 'tense': 'Pres', 'person': '2', 'number': 'Sing', 'mood': 'Cnd'},
        'taitaisit',
    ),
    (
        {'token': 'taitaa', 'tense': 'Pres', 'person': '3', 'number': 'Sing', 'mood': 'Cnd'},
        'taitaisi',
    ),
    (
        {'token': 'taitaa', 'tense': 'Pres', 'person': '1', 'number': 'Plur', 'mood': 'Cnd'},
        'taitaisimme',
    ),
    (
        {'token': 'taitaa', 'tense': 'Pres', 'person': '2', 'number': 'Plur', 'mood': 'Cnd'},
        'taitaisitte',
    ),
    (
        {'token': 'taitaa', 'tense': 'Pres', 'person': '3', 'number': 'Plur', 'mood': 'Cnd'},
        'taitaisivat',
    ),
    (
        {'token': 'olla', 'tense': 'Pres', 'person': '1', 'number': 'Sing', 'mood': 'Cnd'},
        'olisin',
    ),
    (
        {'token': 'olla', 'tense': 'Pres', 'person': '2', 'number': 'Sing', 'mood': 'Cnd'},
        'olisit',
    ),
    (
        {'token': 'olla', 'tense': 'Pres', 'person': '3', 'number': 'Sing', 'mood': 'Cnd'},
        'olisi',
    ),
    (
        {'token': 'olla', 'tense': 'Pres', 'person': '1', 'number': 'Plur', 'mood': 'Cnd'},
        'olisimme',
    ),
    (
        {'token': 'olla', 'tense': 'Pres', 'person': '2', 'number': 'Plur', 'mood': 'Cnd'},
        'olisitte',
    ),
    (
        {'token': 'olla', 'tense': 'Pres', 'person': '3', 'number': 'Plur', 'mood': 'Cnd'},
        'olisivat',
    ),
]

ACTIVE_IMPERATIVE_EXAMPLES = [
    (
        {'token': 'tulla', 'tense': 'Pres', 'person': '2', 'number': 'Sing', 'mood': 'Imp'},
        'tule',
    ),
    (
        {'token': 'tulla', 'tense': 'Pres', 'person': '3', 'number': 'Sing', 'mood': 'Imp'},
        'tulkoon',
    ),
    (
        {'token': 'tulla', 'tense': 'Pres', 'person': '1', 'number': 'Plur', 'mood': 'Imp'},
        'tulkaamme',
    ),
    (
        {'token': 'tulla', 'tense': 'Pres', 'person': '2', 'number': 'Plur', 'mood': 'Imp'},
        'tulkaa',
    ),
    (
        {'token': 'tulla', 'tense': 'Pres', 'person': '3', 'number': 'Plur', 'mood': 'Imp'},
        'tulkoot',
    ),
    (
        {'token': 'hävetä', 'tense': 'Pres', 'person': '2', 'number': 'Sing', 'mood': 'Imp'},
        'häpeä',
    ),
    (
        {'token': 'hävetä', 'tense': 'Pres', 'person': '3', 'number': 'Sing', 'mood': 'Imp'},
        'hävetköön',
    ),
    (
        {'token': 'hävetä', 'tense': 'Pres', 'person': '1', 'number': 'Plur', 'mood': 'Imp'},
        'hävetkäämme',
    ),
    (
        {'token': 'hävetä', 'tense': 'Pres', 'person': '2', 'number': 'Plur', 'mood': 'Imp'},
        'hävetkää',
    ),
    (
        {'token': 'hävetä', 'tense': 'Pres', 'person': '3', 'number': 'Plur', 'mood': 'Imp'},
        'hävetkööt',
    ),
    (
        {'token': 'surra', 'tense': 'Pres', 'person': '2', 'number': 'Sing', 'mood': 'Imp'},
        'sure',
    ),
    (
        {'token': 'surra', 'tense': 'Pres', 'person': '3', 'number': 'Sing', 'mood': 'Imp'},
        'surkoon',
    ),
    (
        {'token': 'surra', 'tense': 'Pres', 'person': '1', 'number': 'Plur', 'mood': 'Imp'},
        'surkaamme',
    ),
    (
        {'token': 'surra', 'tense': 'Pres', 'person': '2', 'number': 'Plur', 'mood': 'Imp'},
        'surkaa',
    ),
    (
        {'token': 'surra', 'tense': 'Pres', 'person': '3', 'number': 'Plur', 'mood': 'Imp'},
        'surkoot',
    ),
    (
        {'token': 'olla', 'tense': 'Pres', 'person': '2', 'number': 'Sing', 'mood': 'Imp'},
        'ole',
    ),
    (
        {'token': 'olla', 'tense': 'Pres', 'person': '3', 'number': 'Sing', 'mood': 'Imp'},
        'olkoon',
    ),
    (
        {'token': 'olla', 'tense': 'Pres', 'person': '1', 'number': 'Plur', 'mood': 'Imp'},
        'olkaamme',
    ),
    (
        {'token': 'olla', 'tense': 'Pres', 'person': '2', 'number': 'Plur', 'mood': 'Imp'},
        'olkaa',
    ),
    (
        {'token': 'olla', 'tense': 'Pres', 'person': '3', 'number': 'Plur', 'mood': 'Imp'},
        'olkoot',
    ),
]

ACTIVE_POTENTIAL_EXAMPLES = [
    (
        {'token': 'auttaa', 'tense': 'Pres', 'person': '1', 'number': 'Sing', 'mood': 'Pot'},
        'auttanen',
    ),
    (
        {'token': 'auttaa', 'tense': 'Pres', 'person': '2', 'number': 'Sing', 'mood': 'Pot'},
        'auttanet',
    ),
    (
        {'token': 'auttaa', 'tense': 'Pres', 'person': '3', 'number': 'Sing', 'mood': 'Pot'},
        'auttanee',
    ),
    (
        {'token': 'auttaa', 'tense': 'Pres', 'person': '1', 'number': 'Plur', 'mood': 'Pot'},
        'auttanemme',
    ),
    (
        {'token': 'auttaa', 'tense': 'Pres', 'person': '2', 'number': 'Plur', 'mood': 'Pot'},
        'auttanette',
    ),
    (
        {'token': 'auttaa', 'tense': 'Pres', 'person': '3', 'number': 'Plur', 'mood': 'Pot'},
        'auttanevat',
    ),
    (
        {'token': 'nousta', 'tense': 'Pres', 'person': '1', 'number': 'Sing', 'mood': 'Pot'},
        'noussen',
    ),
    (
        {'token': 'nousta', 'tense': 'Pres', 'person': '2', 'number': 'Sing', 'mood': 'Pot'},
        'nousset',
    ),
    (
        {'token': 'nousta', 'tense': 'Pres', 'person': '3', 'number': 'Sing', 'mood': 'Pot'},
        'noussee',
    ),
    (
        {'token': 'nousta', 'tense': 'Pres', 'person': '1', 'number': 'Plur', 'mood': 'Pot'},
        'noussemme',
    ),
    (
        {'token': 'nousta', 'tense': 'Pres', 'person': '2', 'number': 'Plur', 'mood': 'Pot'},
        'noussette',
    ),
    (
        {'token': 'nousta', 'tense': 'Pres', 'person': '3', 'number': 'Plur', 'mood': 'Pot'},
        'noussevat',
    ),
    (
        {'token': 'olla', 'tense': 'Pres', 'person': '1', 'number': 'Sing', 'mood': 'Pot'},
        'lienen',
    ),
    (
        {'token': 'olla', 'tense': 'Pres', 'person': '2', 'number': 'Sing', 'mood': 'Pot'},
        'lienet',
    ),
    (
        {'token': 'olla', 'tense': 'Pres', 'person': '3', 'number': 'Sing', 'mood': 'Pot'},
        'lienee',
    ),
    (
        {'token': 'olla', 'tense': 'Pres', 'person': '1', 'number': 'Plur', 'mood': 'Pot'},
        'lienemme',
    ),
    (
        {'token': 'olla', 'tense': 'Pres', 'person': '2', 'number': 'Plur', 'mood': 'Pot'},
        'lienette',
    ),
    (
        {'token': 'olla', 'tense': 'Pres', 'person': '3', 'number': 'Plur', 'mood': 'Pot'},
        'lienevät',
    ),
]

PASSIVE_EXAMPLES = [
    (
        {'token': 'voittaa', 'tense': 'Pres', 'person': '4', 'number': 'Sing', 'mood': 'Ind'},
        'voitetaan',
    ),
    (
        {'token': 'voittaa', 'tense': 'Past', 'person': '4', 'number': 'Sing', 'mood': 'Ind'},
        'voitettiin',
    ),
    (
        {'token': 'voittaa', 'tense': 'Pres', 'person': '4', 'number': 'Sing', 'mood': 'Cnd'},
        'voitettaisiin',
    ),
    (
        {'token': 'voittaa', 'tense': 'Past', 'person': '4', 'number': 'Sing', 'mood': 'Cnd'},
        'voitettaisiin',
    ),
    (
        {'token': 'voittaa', 'tense': 'Pres', 'person': '4', 'number': 'Sing', 'mood': 'Imp'},
        'voitettakoon',
    ),
    (
        {'token': 'voittaa', 'tense': 'Past', 'person': '4', 'number': 'Sing', 'mood': 'Imp'},
        'voitettakoon',
    ),
    (
        {'token': 'voittaa', 'tense': 'Pres', 'person': '4', 'number': 'Sing', 'mood': 'Pot'},
        'voitettaneen',
    ),
    (
        {'token': 'voittaa', 'tense': 'Past', 'person': '4', 'number': 'Sing', 'mood': 'Pot'},
        'voitettaneen',
    ),
    (
        {'token': 'syödä', 'tense': 'Pres', 'person': '4', 'number': 'Sing', 'mood': 'Ind'},
        'syödään',
    ),
    (
        {'token': 'syödä', 'tense': 'Past', 'person': '4', 'number': 'Sing', 'mood': 'Ind'},
        'syötiin',
    ),
    (
        {'token': 'syödä', 'tense': 'Pres', 'person': '4', 'number': 'Sing', 'mood': 'Cnd'},
        'syötäisiin',
    ),
    (
        {'token': 'syödä', 'tense': 'Pres', 'person': '4', 'number': 'Sing', 'mood': 'Imp'},
        'syötäköön',
    ),
    (
        {'token': 'syödä', 'tense': 'Pres', 'person': '4', 'number': 'Sing', 'mood': 'Pot'},
        'syötäneen',
    ),
    (
        {'token': 'purra', 'tense': 'Pres', 'person': '4', 'number': 'Sing', 'mood': 'Ind'},
        'purraan',
    ),
    (
        {'token': 'purra', 'tense': 'Past', 'person': '4', 'number': 'Sing', 'mood': 'Ind'},
        'purtiin',
    ),
    (
        {'token': 'purra', 'tense': 'Pres', 'person': '4', 'number': 'Sing', 'mood': 'Cnd'},
        'purtaisiin',
    ),
    (
        {'token': 'purra', 'tense': 'Pres', 'person': '4', 'number': 'Sing', 'mood': 'Imp'},
        'purtakoon',
    ),
    (
        {'token': 'purra', 'tense': 'Pres', 'person': '4', 'number': 'Sing', 'mood': 'Pot'},
        'purtaneen',
    ),
    (
        {'token': 'mennä', 'tense': 'Pres', 'person': '4', 'number': 'Sing', 'mood': 'Ind'},
        'mennään',
    ),
    (
        {'token': 'mennä', 'tense': 'Past', 'person': '4', 'number': 'Sing', 'mood': 'Ind'},
        'mentiin',
    ),
    (
        {'token': 'mennä', 'tense': 'Pres', 'person': '4', 'number': 'Sing', 'mood': 'Cnd'},
        'mentäisiin',
    ),
    (
        {'token': 'mennä', 'tense': 'Pres', 'person': '4', 'number': 'Sing', 'mood': 'Imp'},
        'mentäköön',
    ),
    (
        {'token': 'mennä', 'tense': 'Pres', 'person': '4', 'number': 'Sing', 'mood': 'Pot'},
        'mentäneen',
    ),
    (
        {'token': 'kietaista', 'tense': 'Pres', 'person': '4', 'number': 'Sing', 'mood': 'Ind'},
        'kietaistaan',
    ),
    (
        {'token': 'kietaista', 'tense': 'Past', 'person': '4', 'number': 'Sing', 'mood': 'Ind'},
        'kietaistiin',
    ),
    (
        {'token': 'kietaista', 'tense': 'Pres', 'person': '4', 'number': 'Sing', 'mood': 'Cnd'},
        'kietaistaisiin',
    ),
    (
        {'token': 'kietaista', 'tense': 'Pres', 'person': '4', 'number': 'Sing', 'mood': 'Imp'},
        'kietaistakoon',
    ),
    (
        {'token': 'kietaista', 'tense': 'Pres', 'person': '4', 'number': 'Sing', 'mood': 'Pot'},
        'kietaistaneen',
    ),
    (
        {'token': 'edetä', 'tense': 'Pres', 'person': '4', 'number': 'Sing', 'mood': 'Ind'},
        'edetään',
    ),
    (
        {'token': 'edetä', 'tense': 'Past', 'person': '4', 'number': 'Sing', 'mood': 'Ind'},
        'edettiin',
    ),
    (
        {'token': 'edetä', 'tense': 'Pres', 'person': '4', 'number': 'Sing', 'mood': 'Cnd'},
        'edettäisiin',
    ),
    (
        {'token': 'edetä', 'tense': 'Pres', 'person': '4', 'number': 'Sing', 'mood': 'Imp'},
        'edettäköön',
    ),
    (
        {'token': 'edetä', 'tense': 'Pres', 'person': '4', 'number': 'Sing', 'mood': 'Pot'},
        'edettäneen',
    ),
    (
        {'token': 'olla', 'tense': 'Pres', 'person': '4', 'number': 'Sing', 'mood': 'Ind'},
        'ollaan',
    ),
    (
        {'token': 'olla', 'tense': 'Past', 'person': '4', 'number': 'Sing', 'mood': 'Ind'},
        'oltiin',
    ),
    (
        {'token': 'olla', 'tense': 'Pres', 'person': '4', 'number': 'Sing', 'mood': 'Cnd'},
        'oltaisiin',
    ),
    (
        {'token': 'olla', 'tense': 'Pres', 'person': '4', 'number': 'Sing', 'mood': 'Imp'},
        'oltakoon',
    ),
    (
        {'token': 'olla', 'tense': 'Pres', 'person': '4', 'number': 'Sing', 'mood': 'Pot'},
        'oltaneen',
    ),
]

PARTICIPLE_EXAMPLES = [
    # VA participle
    (
        {'token': 'kertoa', 'person': '1', 'number': 'Sing', 'partform': 'Pres'},
        'kertova',
    ),
    (
        {'token': 'säilyä', 'person': '1', 'number': 'Sing', 'partform': 'Pres'},
        'säilyvä',
    ),
    (
        {'token': 'hakea', 'person': '1', 'number': 'Sing', 'partform': 'Pres'},
        'hakeva',
    ),
    (
        {'token': 'tupakoida', 'person': '1', 'number': 'Sing', 'partform': 'Pres'},
        'tupakoiva',
    ),
    (
        {'token': 'tupakoida', 'person': '4', 'number': 'Sing', 'partform': 'Pres'},
        'tupakoitava',
    ),
    (
        {'token': 'uida', 'person': '4', 'number': 'Sing', 'partform': 'Pres'},
        'uitava',
    ),
    (
        {'token': 'nähdä', 'person': '4', 'number': 'Sing', 'partform': 'Pres'},
        'nähtävä',
    ),
    (
        {'token': 'lukea', 'person': '4', 'number': 'Sing', 'partform': 'Pres'},
        'luettava',
    ),
    (
        {'token': 'hypätä', 'person': '4', 'number': 'Sing', 'partform': 'Pres'},
        'hypättävä',
    ),
    
    # NUT participle
    (
        {'token': 'olla', 'person': '1', 'number': 'Sing', 'partform': 'Past'},
        'ollut',
    ),
    (
        {'token': 'olla', 'person': '1', 'number': 'Plur', 'partform': 'Past'},
        'olleet',
    ),
    (
        {'token': 'olla', 'person': '4', 'partform': 'Past'},
        'oltu',
    ),
    (
        {'token': 'nähdä', 'person': '1', 'number': 'Sing', 'partform': 'Past'},
        'nähnyt',
    ),
    (
        {'token': 'nähdä', 'person': '1', 'number': 'Plur', 'partform': 'Past'},
        'nähneet',
    ),
    (
        {'token': 'nähdä', 'person': '4', 'partform': 'Past'},
        'nähty',
    ),
    (
        {'token': 'yrittää', 'person': '1', 'number': 'Sing', 'partform': 'Past'},
        'yrittänyt',
    ),
    (
        {'token': 'yrittää', 'person': '1', 'number': 'Plur', 'partform': 'Past'},
        'yrittäneet',
    ),
    (
        {'token': 'yrittää', 'person': '4', 'partform': 'Past'},
        'yritetty',
    ),
    (
        {'token': 'kaivata', 'person': '1', 'number': 'Sing', 'partform': 'Past'},
        'kaivannut',
    ),
    (
        {'token': 'kaivata', 'person': '1', 'number': 'Plur', 'partform': 'Past'},
        'kaivanneet',
    ),
    (
        {'token': 'kaivata', 'person': '4', 'partform': 'Past'},
        'kaivattu',
    ),
    (
        {'token': 'nousta', 'person': '1', 'number': 'Sing', 'partform': 'Past'},
        'noussut',
    ),
    (
        {'token': 'nousta', 'person': '1', 'number': 'Plur', 'partform': 'Past'},
        'nousseet',
    ),
    (
        {'token': 'nousta', 'person': '4', 'partform': 'Past'},
        'noustu',
    ),
    (
        {'token': 'vaieta', 'person': '1', 'number': 'Sing', 'partform': 'Past'},
        'vaiennut',
    ),
    (
        {'token': 'vaieta', 'person': '1', 'number': 'Plur', 'partform': 'Past'},
        'vaienneet',
    ),
    (
        {'token': 'vaieta', 'person': '4', 'partform': 'Past'},
        'vaiettu',
    ),

    # MA participle
    (
        {'token': 'leipoa', 'person': '1', 'number': 'Sing', 'partform': 'Agt'},
        'leipoma',
    ),
    (
        {'token': 'leipoa', 'person': '4', 'partform': 'Agt'},
        'leipoma',
    ),
    (
        {'token': 'havaita', 'person': '1', 'number': 'Sing', 'partform': 'Agt'},
        'havaitsema',
    ),
    (
        {'token': 'kähveltää', 'person': '1', 'number': 'Sing', 'partform': 'Agt'},
        'kähveltämä',
    ),
    (
        {'token': 'löytää', 'person': '1', 'number': 'Sing', 'partform': 'Agt'},
        'löytämä',
    ),
]

INFINITE_EXAMPLES = [
    (
        {'token': 'haluta', 'infform': '1'},
        'haluta',
    ),
    (
        {'token': 'esittää', 'infform': '1'},
        'esittää',
    ),
]
    
NOUN_EXAMPLES = [
    # sijamuodot
    (
        {'token': 'kissa', 'case': 'Nom', 'number': 'Sing'},
        'kissa'
    ),
    (
        {'token': 'kissa', 'case': 'Gen', 'number': 'Sing'},
        'kissan'
    ),
    (
        {'token': 'kissa', 'case': 'Par', 'number': 'Sing'},
        'kissaa'
    ),
    (
        {'token': 'kissa', 'case': 'Ess', 'number': 'Sing'},
        'kissana'
    ),
    (
        {'token': 'kissa', 'case': 'Tra', 'number': 'Sing'},
        'kissaksi'
    ),
    (
        {'token': 'kissa', 'case': 'Ine', 'number': 'Sing'},
        'kissassa'
    ),
    (
        {'token': 'kissa', 'case': 'Ela', 'number': 'Sing'},
        'kissasta'
    ),
    (
        {'token': 'kissa', 'case': 'Ill', 'number': 'Sing'},
        'kissaan'
    ),
    (
        {'token': 'kissa', 'case': 'Ade', 'number': 'Sing'},
        'kissalla'
    ),
    (
        {'token': 'kissa', 'case': 'Abl', 'number': 'Sing'},
        'kissalta'
    ),
    (
        {'token': 'kissa', 'case': 'All', 'number': 'Sing'},
        'kissalle'
    ),
    (
        {'token': 'kissa', 'case': 'Abe', 'number': 'Sing'},
        'kissatta'
    ),
    (
        {'token': 'kissa', 'case': 'Nom', 'number': 'Plur'},
        'kissat'
    ),
    (
        {'token': 'kissa', 'case': 'Gen', 'number': 'Plur'},
        'kissojen'
    ),
    (
        {'token': 'kissa', 'case': 'Par', 'number': 'Plur'},
        'kissoja'
    ),
    (
        {'token': 'kissa', 'case': 'Ess', 'number': 'Plur'},
        'kissoina'
    ),
    (
        {'token': 'kissa', 'case': 'Tra', 'number': 'Plur'},
        'kissoiksi'
    ),
    (
        {'token': 'kissa', 'case': 'Ine', 'number': 'Plur'},
        'kissoissa'
    ),
    (
        {'token': 'kissa', 'case': 'Ela', 'number': 'Plur'},
        'kissoista'
    ),
    (
        {'token': 'kissa', 'case': 'Ill', 'number': 'Plur'},
        'kissoihin'
    ),
    (
        {'token': 'kissa', 'case': 'Ade', 'number': 'Plur'},
        'kissoilla'
    ),
    (
        {'token': 'kissa', 'case': 'Abl', 'number': 'Plur'},
        'kissoilta'
    ),
    (
        {'token': 'kissa', 'case': 'All', 'number': 'Plur'},
        'kissoille'
    ),
    (
        {'token': 'kissa', 'case': 'Abe', 'number': 'Plur'},
        'kissoitta'
    ),
    (
        {'token': 'kissa', 'case': 'Ins', 'number': 'Plur'},
        'kissoin'
    ),

    # vokaalisointu
    (
        {'token': 'pää', 'case': 'Par', 'number': 'Sing'},
        'päätä'
    ),
    (
        {'token': 'pää', 'case': 'Ill', 'number': 'Sing'},
        'päähän'
    ),
    (
        {'token': 'pää', 'case': 'Ade', 'number': 'Sing'},
        'päällä'
    ),
    (
        {'token': 'pää', 'case': 'Abl', 'number': 'Sing'},
        'päältä'
    ),
    (
        {'token': 'pää', 'case': 'Abe', 'number': 'Sing'},
        'päättä'
    ),
    (
        {'token': 'pää', 'case': 'Par', 'number': 'Plur'},
        'päitä'
    ),
    (
        {'token': 'pää', 'case': 'Ill', 'number': 'Plur'},
        'päihin'
    ),
    (
        {'token': 'pää', 'case': 'Ade', 'number': 'Plur'},
        'päillä'
    ),
    (
        {'token': 'pää', 'case': 'Abl', 'number': 'Plur'},
        'päiltä'
    ),
    (
        {'token': 'pää', 'case': 'Abe', 'number': 'Plur'},
        'päittä'
    ),

    # monikon genetiivin päätteet
    (
        {'token': 'perhe', 'case': 'Gen', 'number': 'Plur'},
        'perheiden'
    ),
    (
        {'token': 'poika', 'case': 'Gen', 'number': 'Plur'},
        'poikien'
    ),
    (
        {'token': 'nainen', 'case': 'Gen', 'number': 'Plur'},
        'naisten'
    ),

    # possessive suffixes
    (
        {'token': 'talo', 'case': 'Nom', 'number': 'Sing', 'person_psor': '1'},
        'taloni'
    ),
    (
        {'token': 'talo', 'case': 'Nom', 'number': 'Sing', 'person_psor': '2'},
        'talosi'
    ),
    (
        {'token': 'talo', 'case': 'Nom', 'number': 'Sing', 'person_psor': '3'},
        'talonsa'
    ),
    (
        {'token': 'talo', 'case': 'Nom', 'number': 'Sing', 'person_psor': '1', 'number_psor': 'Plur'},
        'talomme'
    ),
    (
        {'token': 'talo', 'case': 'Nom', 'number': 'Sing', 'person_psor': '2', 'number_psor': 'Plur'},
        'talonne'
    ),
    (
        {'token': 'talo', 'case': 'Nom', 'number': 'Sing', 'person_psor': '3', 'number_psor': 'Plur'},
        'talonsa'
    ),
    (
        {'token': 'talo', 'case': 'Nom', 'number': 'Plur', 'person_psor': '1'},
        'taloni'
    ),
    (
        {'token': 'talo', 'case': 'Nom', 'number': 'Plur', 'person_psor': '2'},
        'talosi'
    ),
    (
        {'token': 'talo', 'case': 'Nom', 'number': 'Plur', 'person_psor': '3'},
        'talonsa'
    ),
    (
        {'token': 'talo', 'case': 'Nom', 'number': 'Plur', 'person_psor': '1', 'number_psor': 'Plur'},
        'talomme'
    ),
    (
        {'token': 'talo', 'case': 'Nom', 'number': 'Plur', 'person_psor': '2', 'number_psor': 'Plur'},
        'talonne'
    ),
    (
        {'token': 'talo', 'case': 'Nom', 'number': 'Plur', 'person_psor': '3', 'number_psor': 'Plur'},
        'talonsa'
    ),
    (
        {'token': 'keksintö', 'case': 'Gen', 'number': 'Plur', 'person_psor': '3'},
        'keksintöjensä'
    ),
    (
        {'token': 'keksintö', 'case': 'Ela', 'number': 'Plur', 'person_psor': '3'},
        'keksinnöistään'
    ),
    (
        {'token': 'keksintö', 'case': 'Ela', 'number': 'Plur', 'person_psor': '3', 'number_psor': 'Plur'},
        'keksinnöistään'
    ),
    (
        {'token': 'keksintö', 'case': 'Par', 'number': 'Plur', 'person_psor': '3'},
        'keksintöjään'
    ),
    (
        {'token': 'keisarinna', 'case': 'Nom', 'number': 'Sing', 'person_psor': '1'},
        'keisarinnani'
    ),
    (
        {'token': 'keisarinna', 'case': 'Gen', 'number': 'Sing', 'person_psor': '1'},
        'keisarinnani'
    ),
    (
        {'token': 'luoto', 'case': 'Gen', 'number': 'Sing', 'person_psor': '1'},
        'luotoni'
    ),
    (
        {'token': 'luoto', 'case': 'Ade', 'number': 'Sing', 'person_psor': '1'},
        'luodollani'
    ),
    (
        {'token': 'luoto', 'case': 'Gen', 'number': 'Plur', 'person_psor': '1', 'number_psor': 'Plur'},
        'luotojemme'
    ),
    (
        {'token': 'perhe', 'case': 'Nom', 'number': 'Plur', 'person_psor': '2', 'number_psor': 'Plur'},
        'perheenne'
    ),
    (
        {'token': 'tytär', 'case': 'Nom', 'number': 'Sing', 'person_psor': '1'},
        'tyttäreni'
    ),
    (
        {'token': 'vanhempi', 'case': 'Gen', 'number': 'Plur', 'person_psor': '1', 'number_psor': 'Plur'},
        'vanhempiemme'
    ),

    # the translative marker -ksi turns into -kse in front of a possessive suffix
    (
        {'token': 'hyöty', 'case': 'Tra', 'number': 'Sing', 'person_psor': '1'},
        'hyödykseni'
    ),
    (
        {'token': 'hyöty', 'case': 'Tra', 'number': 'Sing', 'person_psor': '2'},
        'hyödyksesi'
    ),
    (
        {'token': 'hyöty', 'case': 'Tra', 'number': 'Sing', 'person_psor': '3'},
        'hyödykseen'
    ),
    (
        {'token': 'hyöty', 'case': 'Tra', 'number': 'Sing', 'person_psor': '1', 'number_psor': 'Plur'},
        'hyödyksemme'
    ),
    (
        {'token': 'hyöty', 'case': 'Tra', 'number': 'Plur', 'person_psor': '1', 'number_psor': 'Plur'},
        'hyödyiksemme'
    ),

    # Compound words which do not appear in WORD_CLASSES
    (
        {'token': 'toimituskyky', 'case': 'Par', 'number': 'Sing', 'person_psor': '1', 'number_psor': 'Plur'},
        'toimituskykyämme'
    ),
    (
        {'token': 'silmänpohja', 'case': 'Gen', 'number': 'Plur', 'person_psor': '2'},
        'silmänpohjiesi'
    ),
    (
        {'token': 'mustakynsi', 'case': 'Par', 'number': 'Plur', 'person_psor': '1', 'number_psor': 'Plur'},
        'mustakynsiämme'
    ),
    (
        {'token': 'maailmanjärjestys', 'case': 'Ine', 'number': 'Sing', 'person_psor': '1'},
        'maailmanjärjestyksessäni'
    ),
]

ADJECTIVE_EXAMPLES = [
    # sijamuodot
    (
        {'token': 'virkeä', 'case': 'Nom', 'number': 'Sing'},
        'virkeä'
    ),
    (
        {'token': 'virkeä', 'case': 'Gen', 'number': 'Sing'},
        'virkeän'
    ),
    (
        {'token': 'virkeä', 'case': 'Par', 'number': 'Sing'},
        'virkeää'
    ),
    (
        {'token': 'virkeä', 'case': 'Ess', 'number': 'Sing'},
        'virkeänä'
    ),
    (
        {'token': 'virkeä', 'case': 'Tra', 'number': 'Sing'},
        'virkeäksi'
    ),
    (
        {'token': 'virkeä', 'case': 'Ine', 'number': 'Sing'},
        'virkeässä'
    ),
    (
        {'token': 'virkeä', 'case': 'Ela', 'number': 'Sing'},
        'virkeästä'
    ),
    (
        {'token': 'virkeä', 'case': 'Ill', 'number': 'Sing'},
        'virkeään'
    ),
    (
        {'token': 'virkeä', 'case': 'Ade', 'number': 'Sing'},
        'virkeällä'
    ),
    (
        {'token': 'virkeä', 'case': 'Abl', 'number': 'Sing'},
        'virkeältä'
    ),
    (
        {'token': 'virkeä', 'case': 'All', 'number': 'Sing'},
        'virkeälle'
    ),
    (
        {'token': 'virkeä', 'case': 'Nom', 'number': 'Plur'},
        'virkeät'
    ),
    (
        {'token': 'virkeä', 'case': 'Gen', 'number': 'Plur'},
        'virkeiden'
    ),
    (
        {'token': 'virkeä', 'case': 'Par', 'number': 'Plur'},
        'virkeitä'
    ),
    (
        {'token': 'virkeä', 'case': 'Ess', 'number': 'Plur'},
        'virkeinä'
    ),
    (
        {'token': 'virkeä', 'case': 'Tra', 'number': 'Plur'},
        'virkeiksi'
    ),
    (
        {'token': 'virkeä', 'case': 'Ine', 'number': 'Plur'},
        'virkeissä'
    ),
    (
        {'token': 'virkeä', 'case': 'Ela', 'number': 'Plur'},
        'virkeistä'
    ),
    (
        {'token': 'virkeä', 'case': 'Ill', 'number': 'Plur'},
        'virkeisiin'
    ),
    (
        {'token': 'virkeä', 'case': 'Ade', 'number': 'Plur'},
        'virkeillä'
    ),
    (
        {'token': 'virkeä', 'case': 'Abl', 'number': 'Plur'},
        'virkeiltä'
    ),
    (
        {'token': 'virkeä', 'case': 'All', 'number': 'Plur'},
        'virkeille'
    ),
    (
        {'token': 'virkeä', 'case': 'Ins', 'number': 'Plur'},
        'virkein'
    ),

    # komparaatio
    (
        {'token': 'ohut', 'case': 'Nom', 'number': 'Sing', 'degree': 'Cmp'},
        'ohuempi'
    ),
    (
        {'token': 'ohut', 'case': 'Nom', 'number': 'Sing', 'degree': 'Sup'},
        'ohuin'
    ),
    (
        {'token': 'ohut', 'case': 'Nom', 'number': 'Plur', 'degree': 'Cmp'},
        'ohuemmat'
    ),
    (
        {'token': 'ohut', 'case': 'Nom', 'number': 'Plur', 'degree': 'Sup'},
        'ohuimmat'
    ),
    (
        {'token': 'punainen', 'case': 'Gen', 'number': 'Sing', 'degree': 'Cmp'},
        'punaisemman'
    ),
    (
        {'token': 'punainen', 'case': 'Gen', 'number': 'Sing', 'degree': 'Sup'},
        'punaisimman'
    ),
    (
        {'token': 'punainen', 'case': 'Par', 'number': 'Sing', 'degree': 'Cmp'},
        'punaisempaa'
    ),
    (
        {'token': 'punainen', 'case': 'Par', 'number': 'Sing', 'degree': 'Sup'},
        'punaisimpaa'
    ),
    (
        {'token': 'punainen', 'case': 'Par', 'number': 'Plur', 'degree': 'Sup'},
        'punaisimpia'
    ),
    (
        {'token': 'punainen', 'case': 'Ela', 'number': 'Sing', 'degree': 'Cmp'},
        'punaisemmasta'
    ),
    (
        {'token': 'punainen', 'case': 'Ela', 'number': 'Plur', 'degree': 'Cmp'},
        'punaisemmista'
    ),
    (
        {'token': 'punainen', 'case': 'Ela', 'number': 'Sing', 'degree': 'Sup'},
        'punaisimmasta'
    ),
    (
        {'token': 'punainen', 'case': 'Ela', 'number': 'Plur', 'degree': 'Sup'},
        'punaisimmista'
    ),
    (
        {'token': 'vanha', 'case': 'Nom', 'number': 'Sing', 'degree': 'Cmp'},
        'vanhempi'
    ),
    (
        {'token': 'myyvä', 'case': 'Nom', 'number': 'Sing', 'degree': 'Cmp'},
        'myyvempi'
    ),
    (
        {'token': 'myyvä', 'case': 'Nom', 'number': 'Sing', 'degree': 'Sup'},
        'myyvin'
    ),
    (
        {'token': 'matala', 'case': 'Nom', 'number': 'Sing', 'degree': 'Sup'},
        'matalin'
    ),
    (
        {'token': 'terve', 'case': 'Nom', 'number': 'Sing', 'degree': 'Sup'},
        'tervein'
    ),
    (
        {'token': 'kallis', 'case': 'Nom', 'number': 'Sing', 'degree': 'Sup'},
        'kallein'
    ),
    (
        {'token': 'falski', 'case': 'Nom', 'number': 'Sing', 'degree': 'Sup'},
        'falskein'
    ),
    (
        {'token': 'seikkaileva', 'case': 'Nom', 'number': 'Sing', 'degree': 'Cmp'},
        'seikkailevampi'
    ),
    (
        {'token': 'seikkaileva', 'case': 'Nom', 'number': 'Sing', 'degree': 'Sup'},
        'seikkailevin'
    ),
    (
        {'token': 'valloittava', 'case': 'Nom', 'number': 'Sing', 'degree': 'Cmp'},
        'valloittavampi'
    ),
    (
        {'token': 'valloittava', 'case': 'Nom', 'number': 'Sing', 'degree': 'Sup'},
        'valloittavin'
    ),
    (
        {'token': 'hämärtävä', 'case': 'Nom', 'number': 'Sing', 'degree': 'Cmp'},
        'hämärtävämpi'
    ),
    (
        {'token': 'hämärtävä', 'case': 'Nom', 'number': 'Sing', 'degree': 'Sup'},
        'hämärtävin'
    ),
    (
        {'token': 'uusi', 'case': 'Nom', 'number': 'Sing', 'degree': 'Cmp'},
        'uudempi'
    ),
    (
        {'token': 'uusi', 'case': 'Nom', 'number': 'Sing', 'degree': 'Sup'},
        'uusin'
    ),
    (
        {'token': 'uusi', 'case': 'Ela', 'number': 'Sing', 'degree': 'Sup'},
        'uusimmasta'
    ),
    (
        {'token': 'uusi', 'case': 'Nom', 'number': 'Plur', 'degree': 'Sup'},
        'uusimmat'
    ),
    (
        {'token': 'hyvä', 'case': 'Nom', 'number': 'Sing', 'degree': 'Cmp'},
        'parempi'
    ),
    (
        {'token': 'hyvä', 'case': 'Tra', 'number': 'Sing', 'degree': 'Cmp'},
        'paremmaksi'
    ),
    (
        {'token': 'hyvä', 'case': 'Nom', 'number': 'Sing', 'degree': 'Sup'},
        'paras'
    ),
]

NUMERAL_EXAMPLES = [
    (
        {'token': 'yksi', 'case': 'Gen', 'number': 'Sing'},
        'yhden'
    ),
    (
        {'token': 'nolla', 'case': 'Ela', 'number': 'Sing'},
        'nollasta'
    ),
]

PRONOUN_EXAMPLES = [
    (
        {'token': 'minä', 'case': 'Nom', 'number': 'Sing'},
        'minä'
    ),
    (
        {'token': 'minä', 'case': 'Gen', 'number': 'Sing'},
        'minun'
    ),
    (
        {'token': 'minä', 'case': 'Ill', 'number': 'Sing'},
        'minuun'
    ),
    (
        {'token': 'minä', 'case': 'Abl', 'number': 'Sing'},
        'minulta'
    ),
    (
        {'token': 'sinä', 'case': 'Nom', 'number': 'Sing'},
        'sinä'
    ),
    (
        {'token': 'sinä', 'case': 'Gen', 'number': 'Sing'},
        'sinun'
    ),
    (
        {'token': 'sinä', 'case': 'Ill', 'number': 'Sing'},
        'sinuun'
    ),
    (
        {'token': 'sinä', 'case': 'Abl', 'number': 'Sing'},
        'sinulta'
    ),
    (
        {'token': 'hän', 'case': 'Nom', 'number': 'Sing'},
        'hän'
    ),
    (
        {'token': 'hän', 'case': 'Gen', 'number': 'Sing'},
        'hänen'
    ),
    (
        {'token': 'hän', 'case': 'Ill', 'number': 'Sing'},
        'häneen'
    ),
    (
        {'token': 'hän', 'case': 'Abl', 'number': 'Sing'},
        'häneltä'
    ),
    (
        {'token': 'minä', 'case': 'Nom', 'number': 'Plur'},
        'me'
    ),
    (
        {'token': 'minä', 'case': 'Gen', 'number': 'Plur'},
        'meidän'
    ),
    (
        {'token': 'minä', 'case': 'Ill', 'number': 'Plur'},
        'meihin'
    ),
    (
        {'token': 'minä', 'case': 'Abl', 'number': 'Plur'},
        'meiltä'
    ),
    (
        {'token': 'sinä', 'case': 'Nom', 'number': 'Plur'},
        'te'
    ),
    (
        {'token': 'sinä', 'case': 'Gen', 'number': 'Plur'},
        'teidän'
    ),
    (
        {'token': 'sinä', 'case': 'Ill', 'number': 'Plur'},
        'teihin'
    ),
    (
        {'token': 'sinä', 'case': 'Abl', 'number': 'Plur'},
        'teiltä'
    ),
    (
        {'token': 'hän', 'case': 'Nom', 'number': 'Plur'},
        'he'
    ),
    (
        {'token': 'hän', 'case': 'Gen', 'number': 'Plur'},
        'heidän'
    ),
    (
        {'token': 'hän', 'case': 'Ill', 'number': 'Plur'},
        'heihin'
    ),
    (
        {'token': 'hän', 'case': 'Abl', 'number': 'Plur'},
        'heiltä'
    ),
    (
        {'token': 'se', 'case': 'Nom', 'number': 'Plur'},
        'ne'
    ),
    (
        {'token': 'se', 'case': 'Gen', 'number': 'Plur'},
        'niiden'
    ),
    (
        {'token': 'se', 'case': 'Ill', 'number': 'Plur'},
        'niihin'
    ),
    (
        {'token': 'se', 'case': 'Abl', 'number': 'Plur'},
        'niiltä'
    ),
    (
        {'token': 'joka', 'case': 'Nom', 'number': 'Sing'},
        'joka'
    ),
    (
        {'token': 'joka', 'case': 'Gen', 'number': 'Sing'},
        'jonka'
    ),
    (
        {'token': 'joka', 'case': 'Ill', 'number': 'Sing'},
        'johon'
    ),
    (
        {'token': 'joka', 'case': 'Abl', 'number': 'Sing'},
        'jolta'
    ),
    (
        {'token': 'kuka', 'case': 'Nom', 'number': 'Sing'},
        'kuka'
    ),
    (
        {'token': 'kuka', 'case': 'Gen', 'number': 'Sing'},
        'kenen'
    ),
    (
        {'token': 'kuka', 'case': 'Ill', 'number': 'Sing'},
        'kehen'
    ),
    (
        {'token': 'kuka', 'case': 'Abl', 'number': 'Sing'},
        'keneltä'
    ),
]

NOT_YET_IMPLEMENTED_NOUN_EXAMPLES = [
    # inflections of numerals
    (
        {'token': 'kuusi', 'case': 'Ill', 'number': 'Sing'},
        'kuuteen'
    ),
    (
        {'token': 'tuhat', 'case': 'Ade', 'number': 'Sing'},
        'tuhannella'
    ),
    (
        {'token': 'ensimmäinen', 'case': 'Ela', 'number': 'Sing'},
        'ensimmäistä'
    ),

    # the comitative case
    (
        {'token': 'puoliso', 'case': 'Com', 'number': 'Sing'},
        'puolisoineen'
    ),

    # inflections of the superlative "paras"
    (
        {'token': 'hyvä', 'case': 'Ade', 'number': 'Sing', 'degree': 'Sup'},
        'parhaalla'
    ),
]

NOT_YET_IMPLEMENTED_PRONOUN_EXAMPLES = [
    # quantifier pronouns
    (
        {'token': 'joku', 'case': 'Gen', 'number': 'Sing'},
        'jonkun'
    ),
    (
        {'token': 'eräs', 'case': 'Gen', 'number': 'Plur'},
        'eräiden'
    ),
    (
        {'token': 'moni', 'case': 'Ine', 'number': 'Sing'},
        'monessa'
    ),

    # reflexive pronouns
    (
        {'token': 'itse', 'case': 'Ade', 'number': 'Sing', 'person_psor': '1'},
        'itselleni'
    )
]

NOT_YET_IMPLEMENTED_VERB_EXAMPLES = [
    # E-infinite
    (
        {'token': 'muistella', 'case': 'Ine', 'infform': '2'},
        'muistellessa'
    ),
    (
        {'token': 'muistella', 'case': 'Ins', 'infform': '2'},
        'muistellen'
    ),
    (
        {'token': 'muistella', 'case': 'Ine', 'person_psor': '1', 'infform': '2'},
        'muistellessani'
    ),
    (
        {'token': 'muistella', 'case': 'Ine', 'infform': '2'},
        'muistellessa'
    ),

    # MA-infinite
    (
        {'token': 'hypätä', 'case': 'Ine', 'infform': '3'},
        'hyppäämässä'
    ),
    (
        {'token': 'hypätä', 'case': 'Ela', 'infform': '3'},
        'hyppäämästä'
    ),
    (
        {'token': 'hypätä', 'case': 'Ill', 'infform': '3'},
        'hyppäämään'
    ),
    (
        {'token': 'hypätä', 'case': 'Ade', 'infform': '3'},
        'hyppäämällä'
    ),
    (
        {'token': 'hypätä', 'case': 'Abe', 'infform': '3'},
        'hyppäämättä'
    ),
    (
        {'token': 'hypätä', 'case': 'Ins', 'infform': '3'},
        'hyppäämän'
    ),
]


@pytest.mark.parametrize("inflection,expected", ACTIVE_INDICATIVE_EXAMPLES)
def test_conjugate_verb_active_indicative(inflection, expected):
    assert conjugate_verb(**inflection) == expected


@pytest.mark.parametrize("inflection,expected", ACTIVE_CONDITIONAL_EXAMPLES)
def test_conjugate_verb_active_conditional(inflection, expected):
    assert conjugate_verb(**inflection) == expected


@pytest.mark.parametrize("inflection,expected", ACTIVE_IMPERATIVE_EXAMPLES)
def test_conjugate_verb_active_imperative(inflection, expected):
    assert conjugate_verb(**inflection) == expected


@pytest.mark.parametrize("inflection,expected", ACTIVE_POTENTIAL_EXAMPLES)
def test_conjugate_verb_active_potential(inflection, expected):
    assert conjugate_verb(**inflection) == expected


@pytest.mark.parametrize("inflection,expected", PASSIVE_EXAMPLES)
def test_conjugate_verb_passive(inflection, expected):
    assert conjugate_verb(**inflection) == expected


@pytest.mark.parametrize("inflection,expected", PARTICIPLE_EXAMPLES)
def test_conjugate_verb_participle(inflection, expected):
    assert conjugate_verb(**inflection) == expected


@pytest.mark.parametrize("inflection,expected", INFINITE_EXAMPLES)
def test_conjugate_verb_infinite(inflection, expected):
    assert conjugate_verb(**inflection) == expected


@pytest.mark.parametrize("inflection,expected", NOUN_EXAMPLES)
def test_inflect_noun(inflection, expected):
    assert inflect_nominal(**inflection) == expected


@pytest.mark.parametrize("inflection,expected", ADJECTIVE_EXAMPLES)
def test_inflect_adjective(inflection, expected):
    assert inflect_nominal(**inflection) == expected


@pytest.mark.parametrize("inflection,expected", NUMERAL_EXAMPLES)
def test_inflect_numeral(inflection, expected):
    assert inflect_nominal(**inflection) == expected


@pytest.mark.parametrize("inflection,expected", PRONOUN_EXAMPLES)
def test_inflect_pronoun(inflection, expected):
    assert inflect_pronoun(**inflection) == expected


@pytest.mark.xfail
@pytest.mark.parametrize("inflection,expected", NOT_YET_IMPLEMENTED_NOUN_EXAMPLES)
def test_inflect_not_implemented_noun(inflection, expected):
    assert inflect_nominal(**inflection) == expected


@pytest.mark.xfail
@pytest.mark.parametrize("inflection,expected", NOT_YET_IMPLEMENTED_PRONOUN_EXAMPLES)
def test_inflect_not_implemented_pronoun(inflection, expected):
    assert inflect_pronoun(**inflection) == expected


@pytest.mark.xfail
@pytest.mark.parametrize("inflection,expected", NOT_YET_IMPLEMENTED_VERB_EXAMPLES)
def test_inflect_not_implemented_verb(inflection, expected):
    assert conjugate_verb(**inflection) == expected
