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
        {'token': 'l??hte??', 'tense': 'Pres', 'person': '1', 'number': 'Sing', 'mood': 'Ind'},
        'l??hden'
    ),
    (
        {'token': 'l??hte??', 'tense': 'Pres', 'person': '2', 'number': 'Sing', 'mood': 'Ind'},
        'l??hdet'
    ),
    (
        {'token': 'l??hte??', 'tense': 'Pres', 'person': '3', 'number': 'Sing', 'mood': 'Ind'},
        'l??htee'
    ),
    (
        {'token': 'l??hte??', 'tense': 'Pres', 'person': '1', 'number': 'Plur', 'mood': 'Ind'},
        'l??hdemme'
    ),
    (
        {'token': 'l??hte??', 'tense': 'Pres', 'person': '2', 'number': 'Plur', 'mood': 'Ind'},
        'l??hdette'
    ),
    (
        {'token': 'l??hte??', 'tense': 'Pres', 'person': '3', 'number': 'Plur', 'mood': 'Ind'},
        'l??htev??t'
    ),
    (
        {'token': 'l??hte??', 'tense': 'Past', 'person': '1', 'number': 'Sing', 'mood': 'Ind'},
        'l??hdin'
    ),
    (
        {'token': 'l??hte??', 'tense': 'Past', 'person': '2', 'number': 'Sing', 'mood': 'Ind'},
        'l??hdit'
    ),
    (
        {'token': 'l??hte??', 'tense': 'Past', 'person': '3', 'number': 'Sing', 'mood': 'Ind'},
        'l??hti'
    ),
    (
        {'token': 'l??hte??', 'tense': 'Past', 'person': '1', 'number': 'Plur', 'mood': 'Ind'},
        'l??hdimme'
    ),
    (
        {'token': 'l??hte??', 'tense': 'Past', 'person': '2', 'number': 'Plur', 'mood': 'Ind'},
        'l??hditte'
    ),
    (
        {'token': 'l??hte??', 'tense': 'Past', 'person': '3', 'number': 'Plur', 'mood': 'Ind'},
        'l??htiv??t'
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
        {'token': 'n??hd??', 'tense': 'Past', 'person': '2', 'number': 'Sing', 'mood': 'Ind'},
        'n??it'
    ),
    (
        {'token': 'n??hd??', 'tense': 'Past', 'person': '3', 'number': 'Sing', 'mood': 'Ind'},
        'n??ki'
    ),
    (
        {'token': 'n??hd??', 'tense': 'Past', 'person': '2', 'number': 'Plur', 'mood': 'Ind'},
        'n??itte'
    ),
    (
        {'token': 'n??hd??', 'tense': 'Past', 'person': '3', 'number': 'Plur', 'mood': 'Ind'},
        'n??kiv??t'
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

    # p????verbin kieltomuoto
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
        {'token': 'k??vell??', 'tense': 'Pres', 'person': '1', 'number': 'Sing', 'mood': 'Ind', 'connegative': True},
        'k??vele'
    ),
    (
        {'token': 'k??vell??', 'tense': 'Pres', 'person': '2', 'number': 'Sing', 'mood': 'Ind', 'connegative': True},
        'k??vele'
    ),
    (
        {'token': 'k??vell??', 'tense': 'Pres', 'person': '3', 'number': 'Sing', 'mood': 'Ind', 'connegative': True},
        'k??vele'
    ),
    (
        {'token': 'k??vell??', 'tense': 'Pres', 'person': '1', 'number': 'Plur', 'mood': 'Ind', 'connegative': True},
        'k??vele'
    ),
    (
        {'token': 'k??vell??', 'tense': 'Pres', 'person': '2', 'number': 'Plur', 'mood': 'Ind', 'connegative': True},
        'k??vele'
    ),
    (
        {'token': 'k??vell??', 'tense': 'Pres', 'person': '3', 'number': 'Plur', 'mood': 'Ind', 'connegative': True},
        'k??vele'
    ),
    (
        {'token': 'k??vell??', 'tense': 'Pres', 'person': '2', 'number': 'Sing', 'mood': 'Cnd', 'connegative': True},
        'k??velisi'
    ),
    (
        {'token': 'k??vell??', 'tense': 'Pres', 'person': '2', 'number': 'Sing', 'mood': 'Imp', 'connegative': True},
        'k??vele'
    ),
    (
        {'token': 'k??vell??', 'tense': 'Past', 'person': '2', 'number': 'Sing', 'mood': 'Ind', 'connegative': True},
        'k??vellyt'
    ),
    (
        {'token': 'k??vell??', 'tense': 'Past', 'person': '2', 'number': 'Plur', 'mood': 'Ind', 'connegative': True},
        'k??velleet'
    ),
    (
        {'token': 'k??vell??', 'tense': 'Past', 'person': '2', 'number': 'Sing', 'mood': 'Cnd', 'connegative': True},
        'k??velisi'
    ),
    (
        {'token': 'olla', 'tense': 'Pres', 'person': '4', 'number': 'Sing', 'mood': 'Ind', 'connegative': True},
        'olla'
    ),
    (
        {'token': 'k??vell??', 'tense': 'Pres', 'person': '4', 'number': 'Sing', 'mood': 'Ind', 'connegative': True},
        'k??vell??'
    ),
    (
        {'token': 'hautoa', 'tense': 'Pres', 'person': '4', 'number': 'Sing', 'mood': 'Ind', 'connegative': True},
        'haudota'
    ),
    (
        {'token': 'sy??d??', 'tense': 'Pres', 'person': '4', 'number': 'Sing', 'mood': 'Ind', 'connegative': True},
        'sy??d??'
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
        {'token': 'n??ytt????', 'tense': 'Pres', 'person': '1', 'number': 'Sing', 'mood': 'Cnd'},
        'n??ytt??isin',
    ),
    (
        {'token': 'n??ytt????', 'tense': 'Pres', 'person': '2', 'number': 'Sing', 'mood': 'Cnd'},
        'n??ytt??isit',
    ),
    (
        {'token': 'n??ytt????', 'tense': 'Pres', 'person': '3', 'number': 'Sing', 'mood': 'Cnd'},
        'n??ytt??isi',
    ),
    (
        {'token': 'n??ytt????', 'tense': 'Pres', 'person': '1', 'number': 'Plur', 'mood': 'Cnd'},
        'n??ytt??isimme',
    ),
    (
        {'token': 'n??ytt????', 'tense': 'Pres', 'person': '2', 'number': 'Plur', 'mood': 'Cnd'},
        'n??ytt??isitte',
    ),
    (
        {'token': 'n??ytt????', 'tense': 'Pres', 'person': '3', 'number': 'Plur', 'mood': 'Cnd'},
        'n??ytt??isiv??t',
    ),
    (
        {'token': 'n??ytt????', 'tense': 'Past', 'person': '1', 'number': 'Sing', 'mood': 'Cnd'},
        'n??ytt??isin',
    ),
    (
        {'token': 'n??ytt????', 'tense': 'Past', 'person': '2', 'number': 'Sing', 'mood': 'Cnd'},
        'n??ytt??isit',
    ),
    (
        {'token': 'n??ytt????', 'tense': 'Past', 'person': '3', 'number': 'Sing', 'mood': 'Cnd'},
        'n??ytt??isi',
    ),
    (
        {'token': 'n??ytt????', 'tense': 'Past', 'person': '1', 'number': 'Plur', 'mood': 'Cnd'},
        'n??ytt??isimme',
    ),
    (
        {'token': 'n??ytt????', 'tense': 'Past', 'person': '2', 'number': 'Plur', 'mood': 'Cnd'},
        'n??ytt??isitte',
    ),
    (
        {'token': 'n??ytt????', 'tense': 'Past', 'person': '3', 'number': 'Plur', 'mood': 'Cnd'},
        'n??ytt??isiv??t',
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
        {'token': 'lyk??t??', 'tense': 'Pres', 'person': '1', 'number': 'Sing', 'mood': 'Cnd'},
        'lykk??isin',
    ),
    (
        {'token': 'lyk??t??', 'tense': 'Pres', 'person': '2', 'number': 'Sing', 'mood': 'Cnd'},
        'lykk??isit',
    ),
    (
        {'token': 'lyk??t??', 'tense': 'Pres', 'person': '3', 'number': 'Sing', 'mood': 'Cnd'},
        'lykk??isi',
    ),
    (
        {'token': 'lyk??t??', 'tense': 'Pres', 'person': '1', 'number': 'Plur', 'mood': 'Cnd'},
        'lykk??isimme',
    ),
    (
        {'token': 'lyk??t??', 'tense': 'Pres', 'person': '2', 'number': 'Plur', 'mood': 'Cnd'},
        'lykk??isitte',
    ),
    (
        {'token': 'lyk??t??', 'tense': 'Pres', 'person': '3', 'number': 'Plur', 'mood': 'Cnd'},
        'lykk??isiv??t',
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
        {'token': 'h??vet??', 'tense': 'Pres', 'person': '2', 'number': 'Sing', 'mood': 'Imp'},
        'h??pe??',
    ),
    (
        {'token': 'h??vet??', 'tense': 'Pres', 'person': '3', 'number': 'Sing', 'mood': 'Imp'},
        'h??vetk????n',
    ),
    (
        {'token': 'h??vet??', 'tense': 'Pres', 'person': '1', 'number': 'Plur', 'mood': 'Imp'},
        'h??vetk????mme',
    ),
    (
        {'token': 'h??vet??', 'tense': 'Pres', 'person': '2', 'number': 'Plur', 'mood': 'Imp'},
        'h??vetk????',
    ),
    (
        {'token': 'h??vet??', 'tense': 'Pres', 'person': '3', 'number': 'Plur', 'mood': 'Imp'},
        'h??vetk????t',
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
        'lienev??t',
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
        {'token': 'sy??d??', 'tense': 'Pres', 'person': '4', 'number': 'Sing', 'mood': 'Ind'},
        'sy??d????n',
    ),
    (
        {'token': 'sy??d??', 'tense': 'Past', 'person': '4', 'number': 'Sing', 'mood': 'Ind'},
        'sy??tiin',
    ),
    (
        {'token': 'sy??d??', 'tense': 'Pres', 'person': '4', 'number': 'Sing', 'mood': 'Cnd'},
        'sy??t??isiin',
    ),
    (
        {'token': 'sy??d??', 'tense': 'Pres', 'person': '4', 'number': 'Sing', 'mood': 'Imp'},
        'sy??t??k????n',
    ),
    (
        {'token': 'sy??d??', 'tense': 'Pres', 'person': '4', 'number': 'Sing', 'mood': 'Pot'},
        'sy??t??neen',
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
        {'token': 'menn??', 'tense': 'Pres', 'person': '4', 'number': 'Sing', 'mood': 'Ind'},
        'menn????n',
    ),
    (
        {'token': 'menn??', 'tense': 'Past', 'person': '4', 'number': 'Sing', 'mood': 'Ind'},
        'mentiin',
    ),
    (
        {'token': 'menn??', 'tense': 'Pres', 'person': '4', 'number': 'Sing', 'mood': 'Cnd'},
        'ment??isiin',
    ),
    (
        {'token': 'menn??', 'tense': 'Pres', 'person': '4', 'number': 'Sing', 'mood': 'Imp'},
        'ment??k????n',
    ),
    (
        {'token': 'menn??', 'tense': 'Pres', 'person': '4', 'number': 'Sing', 'mood': 'Pot'},
        'ment??neen',
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
        {'token': 'edet??', 'tense': 'Pres', 'person': '4', 'number': 'Sing', 'mood': 'Ind'},
        'edet????n',
    ),
    (
        {'token': 'edet??', 'tense': 'Past', 'person': '4', 'number': 'Sing', 'mood': 'Ind'},
        'edettiin',
    ),
    (
        {'token': 'edet??', 'tense': 'Pres', 'person': '4', 'number': 'Sing', 'mood': 'Cnd'},
        'edett??isiin',
    ),
    (
        {'token': 'edet??', 'tense': 'Pres', 'person': '4', 'number': 'Sing', 'mood': 'Imp'},
        'edett??k????n',
    ),
    (
        {'token': 'edet??', 'tense': 'Pres', 'person': '4', 'number': 'Sing', 'mood': 'Pot'},
        'edett??neen',
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
        {'token': 's??ily??', 'person': '1', 'number': 'Sing', 'partform': 'Pres'},
        's??ilyv??',
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
        {'token': 'n??hd??', 'person': '4', 'number': 'Sing', 'partform': 'Pres'},
        'n??ht??v??',
    ),
    (
        {'token': 'lukea', 'person': '4', 'number': 'Sing', 'partform': 'Pres'},
        'luettava',
    ),
    (
        {'token': 'hyp??t??', 'person': '4', 'number': 'Sing', 'partform': 'Pres'},
        'hyp??tt??v??',
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
        {'token': 'n??hd??', 'person': '1', 'number': 'Sing', 'partform': 'Past'},
        'n??hnyt',
    ),
    (
        {'token': 'n??hd??', 'person': '1', 'number': 'Plur', 'partform': 'Past'},
        'n??hneet',
    ),
    (
        {'token': 'n??hd??', 'person': '4', 'partform': 'Past'},
        'n??hty',
    ),
    (
        {'token': 'yritt????', 'person': '1', 'number': 'Sing', 'partform': 'Past'},
        'yritt??nyt',
    ),
    (
        {'token': 'yritt????', 'person': '1', 'number': 'Plur', 'partform': 'Past'},
        'yritt??neet',
    ),
    (
        {'token': 'yritt????', 'person': '4', 'partform': 'Past'},
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
        {'token': 'k??hvelt????', 'person': '1', 'number': 'Sing', 'partform': 'Agt'},
        'k??hvelt??m??',
    ),
    (
        {'token': 'l??yt????', 'person': '1', 'number': 'Sing', 'partform': 'Agt'},
        'l??yt??m??',
    ),
]

INFINITE_EXAMPLES = [
    (
        {'token': 'haluta', 'infform': '1'},
        'haluta',
    ),
    (
        {'token': 'esitt????', 'infform': '1'},
        'esitt????',
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
        {'token': 'p????', 'case': 'Par', 'number': 'Sing'},
        'p????t??'
    ),
    (
        {'token': 'p????', 'case': 'Ill', 'number': 'Sing'},
        'p????h??n'
    ),
    (
        {'token': 'p????', 'case': 'Ade', 'number': 'Sing'},
        'p????ll??'
    ),
    (
        {'token': 'p????', 'case': 'Abl', 'number': 'Sing'},
        'p????lt??'
    ),
    (
        {'token': 'p????', 'case': 'Abe', 'number': 'Sing'},
        'p????tt??'
    ),
    (
        {'token': 'p????', 'case': 'Par', 'number': 'Plur'},
        'p??it??'
    ),
    (
        {'token': 'p????', 'case': 'Ill', 'number': 'Plur'},
        'p??ihin'
    ),
    (
        {'token': 'p????', 'case': 'Ade', 'number': 'Plur'},
        'p??ill??'
    ),
    (
        {'token': 'p????', 'case': 'Abl', 'number': 'Plur'},
        'p??ilt??'
    ),
    (
        {'token': 'p????', 'case': 'Abe', 'number': 'Plur'},
        'p??itt??'
    ),

    # monikon genetiivin p????tteet
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
        {'token': 'keksint??', 'case': 'Gen', 'number': 'Plur', 'person_psor': '3'},
        'keksint??jens??'
    ),
    (
        {'token': 'keksint??', 'case': 'Ela', 'number': 'Plur', 'person_psor': '3'},
        'keksinn??ist????n'
    ),
    (
        {'token': 'keksint??', 'case': 'Ela', 'number': 'Plur', 'person_psor': '3', 'number_psor': 'Plur'},
        'keksinn??ist????n'
    ),
    (
        {'token': 'keksint??', 'case': 'Par', 'number': 'Plur', 'person_psor': '3'},
        'keksint??j????n'
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
        {'token': 'tyt??r', 'case': 'Nom', 'number': 'Sing', 'person_psor': '1'},
        'tytt??reni'
    ),
    (
        {'token': 'vanhempi', 'case': 'Gen', 'number': 'Plur', 'person_psor': '1', 'number_psor': 'Plur'},
        'vanhempiemme'
    ),

    # the translative marker -ksi turns into -kse in front of a possessive suffix
    (
        {'token': 'hy??ty', 'case': 'Tra', 'number': 'Sing', 'person_psor': '1'},
        'hy??dykseni'
    ),
    (
        {'token': 'hy??ty', 'case': 'Tra', 'number': 'Sing', 'person_psor': '2'},
        'hy??dyksesi'
    ),
    (
        {'token': 'hy??ty', 'case': 'Tra', 'number': 'Sing', 'person_psor': '3'},
        'hy??dykseen'
    ),
    (
        {'token': 'hy??ty', 'case': 'Tra', 'number': 'Sing', 'person_psor': '1', 'number_psor': 'Plur'},
        'hy??dyksemme'
    ),
    (
        {'token': 'hy??ty', 'case': 'Tra', 'number': 'Plur', 'person_psor': '1', 'number_psor': 'Plur'},
        'hy??dyiksemme'
    ),

    # Compound words which do not appear in WORD_CLASSES
    (
        {'token': 'toimituskyky', 'case': 'Par', 'number': 'Sing', 'person_psor': '1', 'number_psor': 'Plur'},
        'toimituskyky??mme'
    ),
    (
        {'token': 'silm??npohja', 'case': 'Gen', 'number': 'Plur', 'person_psor': '2'},
        'silm??npohjiesi'
    ),
    (
        {'token': 'mustakynsi', 'case': 'Par', 'number': 'Plur', 'person_psor': '1', 'number_psor': 'Plur'},
        'mustakynsi??mme'
    ),
    (
        {'token': 'maailmanj??rjestys', 'case': 'Ine', 'number': 'Sing', 'person_psor': '1'},
        'maailmanj??rjestyksess??ni'
    ),
]

ADJECTIVE_EXAMPLES = [
    # sijamuodot
    (
        {'token': 'virke??', 'case': 'Nom', 'number': 'Sing'},
        'virke??'
    ),
    (
        {'token': 'virke??', 'case': 'Gen', 'number': 'Sing'},
        'virke??n'
    ),
    (
        {'token': 'virke??', 'case': 'Par', 'number': 'Sing'},
        'virke????'
    ),
    (
        {'token': 'virke??', 'case': 'Ess', 'number': 'Sing'},
        'virke??n??'
    ),
    (
        {'token': 'virke??', 'case': 'Tra', 'number': 'Sing'},
        'virke??ksi'
    ),
    (
        {'token': 'virke??', 'case': 'Ine', 'number': 'Sing'},
        'virke??ss??'
    ),
    (
        {'token': 'virke??', 'case': 'Ela', 'number': 'Sing'},
        'virke??st??'
    ),
    (
        {'token': 'virke??', 'case': 'Ill', 'number': 'Sing'},
        'virke????n'
    ),
    (
        {'token': 'virke??', 'case': 'Ade', 'number': 'Sing'},
        'virke??ll??'
    ),
    (
        {'token': 'virke??', 'case': 'Abl', 'number': 'Sing'},
        'virke??lt??'
    ),
    (
        {'token': 'virke??', 'case': 'All', 'number': 'Sing'},
        'virke??lle'
    ),
    (
        {'token': 'virke??', 'case': 'Nom', 'number': 'Plur'},
        'virke??t'
    ),
    (
        {'token': 'virke??', 'case': 'Gen', 'number': 'Plur'},
        'virkeiden'
    ),
    (
        {'token': 'virke??', 'case': 'Par', 'number': 'Plur'},
        'virkeit??'
    ),
    (
        {'token': 'virke??', 'case': 'Ess', 'number': 'Plur'},
        'virkein??'
    ),
    (
        {'token': 'virke??', 'case': 'Tra', 'number': 'Plur'},
        'virkeiksi'
    ),
    (
        {'token': 'virke??', 'case': 'Ine', 'number': 'Plur'},
        'virkeiss??'
    ),
    (
        {'token': 'virke??', 'case': 'Ela', 'number': 'Plur'},
        'virkeist??'
    ),
    (
        {'token': 'virke??', 'case': 'Ill', 'number': 'Plur'},
        'virkeisiin'
    ),
    (
        {'token': 'virke??', 'case': 'Ade', 'number': 'Plur'},
        'virkeill??'
    ),
    (
        {'token': 'virke??', 'case': 'Abl', 'number': 'Plur'},
        'virkeilt??'
    ),
    (
        {'token': 'virke??', 'case': 'All', 'number': 'Plur'},
        'virkeille'
    ),
    (
        {'token': 'virke??', 'case': 'Ins', 'number': 'Plur'},
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
        {'token': 'myyv??', 'case': 'Nom', 'number': 'Sing', 'degree': 'Cmp'},
        'myyvempi'
    ),
    (
        {'token': 'myyv??', 'case': 'Nom', 'number': 'Sing', 'degree': 'Sup'},
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
        {'token': 'h??m??rt??v??', 'case': 'Nom', 'number': 'Sing', 'degree': 'Cmp'},
        'h??m??rt??v??mpi'
    ),
    (
        {'token': 'h??m??rt??v??', 'case': 'Nom', 'number': 'Sing', 'degree': 'Sup'},
        'h??m??rt??vin'
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
        {'token': 'hyv??', 'case': 'Nom', 'number': 'Sing', 'degree': 'Cmp'},
        'parempi'
    ),
    (
        {'token': 'hyv??', 'case': 'Tra', 'number': 'Sing', 'degree': 'Cmp'},
        'paremmaksi'
    ),
    (
        {'token': 'hyv??', 'case': 'Nom', 'number': 'Sing', 'degree': 'Sup'},
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
        {'token': 'min??', 'case': 'Nom', 'number': 'Sing'},
        'min??'
    ),
    (
        {'token': 'min??', 'case': 'Gen', 'number': 'Sing'},
        'minun'
    ),
    (
        {'token': 'min??', 'case': 'Ill', 'number': 'Sing'},
        'minuun'
    ),
    (
        {'token': 'min??', 'case': 'Abl', 'number': 'Sing'},
        'minulta'
    ),
    (
        {'token': 'sin??', 'case': 'Nom', 'number': 'Sing'},
        'sin??'
    ),
    (
        {'token': 'sin??', 'case': 'Gen', 'number': 'Sing'},
        'sinun'
    ),
    (
        {'token': 'sin??', 'case': 'Ill', 'number': 'Sing'},
        'sinuun'
    ),
    (
        {'token': 'sin??', 'case': 'Abl', 'number': 'Sing'},
        'sinulta'
    ),
    (
        {'token': 'h??n', 'case': 'Nom', 'number': 'Sing'},
        'h??n'
    ),
    (
        {'token': 'h??n', 'case': 'Gen', 'number': 'Sing'},
        'h??nen'
    ),
    (
        {'token': 'h??n', 'case': 'Ill', 'number': 'Sing'},
        'h??neen'
    ),
    (
        {'token': 'h??n', 'case': 'Abl', 'number': 'Sing'},
        'h??nelt??'
    ),
    (
        {'token': 'min??', 'case': 'Nom', 'number': 'Plur'},
        'me'
    ),
    (
        {'token': 'min??', 'case': 'Gen', 'number': 'Plur'},
        'meid??n'
    ),
    (
        {'token': 'min??', 'case': 'Ill', 'number': 'Plur'},
        'meihin'
    ),
    (
        {'token': 'min??', 'case': 'Abl', 'number': 'Plur'},
        'meilt??'
    ),
    (
        {'token': 'sin??', 'case': 'Nom', 'number': 'Plur'},
        'te'
    ),
    (
        {'token': 'sin??', 'case': 'Gen', 'number': 'Plur'},
        'teid??n'
    ),
    (
        {'token': 'sin??', 'case': 'Ill', 'number': 'Plur'},
        'teihin'
    ),
    (
        {'token': 'sin??', 'case': 'Abl', 'number': 'Plur'},
        'teilt??'
    ),
    (
        {'token': 'h??n', 'case': 'Nom', 'number': 'Plur'},
        'he'
    ),
    (
        {'token': 'h??n', 'case': 'Gen', 'number': 'Plur'},
        'heid??n'
    ),
    (
        {'token': 'h??n', 'case': 'Ill', 'number': 'Plur'},
        'heihin'
    ),
    (
        {'token': 'h??n', 'case': 'Abl', 'number': 'Plur'},
        'heilt??'
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
        'niilt??'
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
        'kenelt??'
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
        {'token': 'ensimm??inen', 'case': 'Ela', 'number': 'Sing'},
        'ensimm??ist??'
    ),

    # the comitative case
    (
        {'token': 'puoliso', 'case': 'Com', 'number': 'Sing'},
        'puolisoineen'
    ),

    # inflections of the superlative "paras"
    (
        {'token': 'hyv??', 'case': 'Ade', 'number': 'Sing', 'degree': 'Sup'},
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
        {'token': 'er??s', 'case': 'Gen', 'number': 'Plur'},
        'er??iden'
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
        {'token': 'hyp??t??', 'case': 'Ine', 'infform': '3'},
        'hypp????m??ss??'
    ),
    (
        {'token': 'hyp??t??', 'case': 'Ela', 'infform': '3'},
        'hypp????m??st??'
    ),
    (
        {'token': 'hyp??t??', 'case': 'Ill', 'infform': '3'},
        'hypp????m????n'
    ),
    (
        {'token': 'hyp??t??', 'case': 'Ade', 'infform': '3'},
        'hypp????m??ll??'
    ),
    (
        {'token': 'hyp??t??', 'case': 'Abe', 'infform': '3'},
        'hypp????m??tt??'
    ),
    (
        {'token': 'hyp??t??', 'case': 'Ins', 'infform': '3'},
        'hypp????m??n'
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
