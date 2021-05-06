import re
from typing import Literal, Optional
from voikko import libvoikko
from voikko.inflect_word import inflect_word, WORD_CLASSES
from voikko.voikkoutils import VOWEL_BACK, get_wordform_infl_vowel_type

case_affixes = {
    'Nom': '',
    'Gen': 'n',
    'Acc': 't',
    'Par': 'A',
    'Ess': 'nA',
    'Tra': 'ksi',
    'Ine': 'ssA',
    'Ela': 'stA',
    'Ill': 'hin',
    'Ade': 'llA',
    'Abl': 'ltA',
    'All': 'lle',
    'Ins': 'in',
    'Com': 'ne',
}
expand_case_name = {
    'Nom': 'nominatiivi',
    'Gen': 'genetiivi',
    'Par': 'partitiivi',
    'Ess': 'essiivi',
    'Tra': 'translatiivi',
    'Ine': 'inessiivi',
    'Ela': 'elatiivi',
    'Ill': 'illatiivi',
    'Ade': 'adessiivi',
    'Abl': 'ablatiivi',
    'All': 'allatiivi',
    'Abe': 'abessiivi',
    'Acc': 'akkusatiivi',
    'Com': 'komitatiivi',
    'Ins': 'instruktiivi'
}
verb_person_number_affix = {
    '1_Sing': 'n',
    '2_Sing': 't',
    '3_Sing': '',
    '1_Plur': 'mme',
    '2_Plur': 'tte',
    '3_Plur': 'vAt',
}
verb_imperative_person_number_affix = {
    '1_Sing': '', # Does not exist
    '2_Sing': '',
    '3_Sing': 'kOOn',
    '1_Plur': 'kAAmme',
    '2_Plur': 'kAA',
    '3_Plur': 'kOOt',
}
verb_potential_person_number_affix = {
    '1_Sing': 'nen',
    '2_Sing': 'net',
    '3_Sing': 'nee',
    '1_Plur': 'nemme',
    '2_Plur': 'nette',
    '3_Plur': 'nevAt',
}
possessive_suffixes = {
    '1_Sing': 'ni',
    '2_Sing': 'si',
    '1_Plur': 'mme',
    '2_Plur': 'nne',
    # See the code for the third person possessive
}
pronoun_stems = {
    'minä_Sing': 'minu',
    'minä_Plur': 'mei',
    'sinä_Sing': 'sinu',
    'sinä_Plur': 'tei',
    'hän_Sing': 'häne',
    'hän_Plur': 'hei',
    'se_Sing': 'si',
    'se_Plur': 'nii',
    'tämä_Sing': 'tä',
    'tämä_Plur': 'näi',
    'tuo_Plur': 'noi',
    'joka_Sing': 'jo',
    'joka_Plur': 'joi',
    'kuka_Sing': 'kene',
    'kuka_Plur': 'kei',
    'mikä_Sing': 'mi',
    'mikä_Plur': 'mi',
}
pronoun_exceptions = {
    'minä_Sing_Nom': 'minä',
    'minä_Sing_Ill': 'minuun',
    'minä_Plur_Nom': 'me',
    'minä_Plur_Gen': 'meidän',
    'minä_Plur_Acc': 'meidät',
    'minä_Plur_Par': 'meitä',
    'sinä_Sing_Nom': 'sinä',
    'sinä_Sing_Ill': 'sinuun',
    'sinä_Plur_Nom': 'te',
    'sinä_Plur_Gen': 'teidän',
    'sinä_Plur_Acc': 'teidät',
    'sinä_Plur_Par': 'teitä',
    'hän_Sing_Nom': 'hän',
    'hän_Sing_Par': 'häntä',
    'hän_Sing_Ill': 'häneen',
    'hän_Plur_Nom': 'he',
    'hän_Plur_Gen': 'heidän',
    'hän_Plur_Acc': 'heidät',
    'hän_Plur_Par': 'heitä',
    'se_Sing_Nom': 'se',
    'se_Sing_Ine': 'siinä',
    'se_Sing_Ela': 'siitä',
    'se_Sing_Ill': 'siihen',
    'se_Plur_Nom': 'ne',
    'se_Plur_Gen': 'niiden',
    'tämä_Sing_Nom': 'tämä',
    'tämä_Sing_Gen': 'tämän',
    'tämä_Sing_Ill': 'tähän',
    'tämä_Plur_Nom': 'nämä',
    'tämä_Plur_Gen': 'näiden',
    'tuo_Sing_Ill': 'tuohon',
    'tuo_Plur_Nom': 'nuo',
    'tuo_Plur_Gen': 'noiden',
    'joka_Sing_Nom': 'joka',
    'joka_Sing_Gen': 'jonka',
    'joka_Sing_Par': 'jota',
    'joka_Sing_Ill': 'johon',
    'joka_Plur_Nom': 'jotka',
    'joka_Plur_Gen': 'joiden',
    'joka_Plur_Par': 'joita',
    'kuka_Sing_Nom': 'kuka',
    'kuka_Sing_Par': 'ketä',
    'kuka_Sing_Ill': 'kehen',
    'kuka_Plur_Nom': 'ketkä',
    'kuka_Plur_Gen': 'keiden',
    'mikä_Sing_Nom': 'mikä',
    'mikä_Sing_Gen': 'minkä',
    'mikä_Sing_Par': 'mitä',
    'mikä_Plur_Nom': 'mitkä',
    'mikä_Plur_Gen': 'minkä',
    'mikä_Plur_Par': 'mitä',
}
ei_conjugation = {
    '1_Sing_Ind': 'en',
    '2_Sing_Ind': 'et',
    '3_Sing_Ind': 'ei',
    '4_Sing_Ind': 'ei',
    '1_Plur_Ind': 'emme',
    '2_Plur_Ind': 'ette',
    '3_Plur_Ind': 'eivät',
    '4_Plur_Ind': 'ei',
    '1_Sing_Imp': '', # not used
    '2_Sing_Imp': 'älä',
    '3_Sing_Imp': 'älköön',
    '4_Sing_Imp': 'älköön',
    '1_Plur_Imp': 'alkäämme',
    '2_Plur_Imp': 'älkää',
    '3_Plur_Imp': 'älkööt',
    '4_Plur_Imp': 'älköön',
}

voikko = libvoikko.Voikko('fi')

def conjugate_verb(token: str,
                   *,
                   tense: Literal['Pres', 'Past']='Pres',
                   person: Literal['1', '2', '3', '4']='1',
                   number: Literal['Sing', 'Plur']='Sing',
                   mood: Literal['Ind', 'Cnd', 'Imp', 'Pot']='Ind',
                   infform: Optional[Literal['1', '2', '3']]=None,
                   partform: Optional[Literal['Pres', 'Past', 'Agt']]=None,
                   connegative: bool=False) -> str:
    if token == 'ei':
        return _conjugate_negation_verb(person, number, mood)

    elif connegative:
        return _conjugate_verb_connegative(token, tense, person, mood, number)

    elif infform:
        return _conjugate_verb_infinite(token, infform)

    elif partform:
        return _conjugate_verb_participle(token, person, number, partform)

    elif person == '4':
        return _conjugate_verb_passive(token, tense, number, mood)

    elif mood == 'Cnd':
        return _conjugate_verb_conditional(token, person, number)

    elif mood == 'Imp':
        return _conjugate_verb_imperative(token, person, number)

    elif mood == 'Pot':
        return _conjugate_verb_potential(token, person, number)

    else: # mood == 'Ind'
        return _conjugate_verb_indicative(token, tense, person, number)


def inflect_nominal(token: str,
                    *,
                    case: Literal['Abe', 'Abl', 'Acc', 'Ade', 'All', 'Com', 'Ela', 'Ess',
                                  'Gen', 'Ill', 'Ine', 'Ins', 'Nom', 'Par', 'Tra']='Nom',
                    number: Literal['Sing', 'Plur']='Sing',
                    degree: Optional[Literal['Pos', 'Cmp', 'Sup']] = None,
                    person_psor: Optional[Literal['1', '2', '3']] = None,
                    number_psor: Optional[Literal['Sing', 'Plur']] = None):
    if token not in WORD_CLASSES:
        modifier, element = _split_compound_word(token)
    else:
        modifier = ''
        element = token

    inflected_element = _inflect_nominal_simple_stem(element, case, number, degree, person_psor, number_psor)
    return modifier + inflected_element


def _inflect_nominal_simple_stem(token, case, number, degree, person_psor, number_psor):
    # FIXME: numerals
    
    forms = inflect_word(token, required_wclass='subst')

    # Degree (adjectives only)
    # https://kaino.kotus.fi/visk/sisallys.php?p=300
    form = token
    if degree in ['Cmp', 'Sup'] and 'genetiivi' in forms:
        inflection_classes = None
        if token == 'hyvä':
            affix = ''
            if degree == 'Cmp':
                root = 'parempi'
                inflection_classes = ['subst-suurempi-av1']
            else:
                # FIXME: correct cases for the superlative "paras"
                root = 'paras'
                inflection_classes = ['subst-vieras'] # this is wrong!
        else:
            root = forms['genetiivi'][:-1]
            if degree == 'Cmp':
                if _has_two_syllables_inaccurate(token) and root[-1] in 'aä':
                    root = root[:-1] + 'e'
            else: # degree == 'Sup'
                if token in ('uusi', 'täysi', 'tosi'):
                    root = token[:-1]
                elif len(root) >= 2 and not is_vowel(root[-2]) and root[-1] in 'aeä':
                    root = root[:-1]
                elif len(root) >= 2 and is_vowel(root[-2]) and is_vowel(root[-1]):
                    root = root[:-1]

                if root[-1] == 'i':
                    root = root[:-1] + 'e'

            if case == 'Nom' and number == 'Sing':
                if degree == 'Cmp':
                    affix = 'mpi'
                else:
                    affix = 'in'
            elif number == 'Sing' or (number == 'Plur' and case == 'Nom'):
                if degree == 'Cmp':
                    affix = 'mpA'
                else:
                    affix = 'impA'
            else: # number == 'Plur'
                if degree == 'Cmp':
                    affix = 'mpi'
                else:
                    affix = 'impi'

        vowel_type = get_wordform_infl_vowel_type(forms['genetiivi'])
        affix = replace_vowel_placeholders(affix, vowel_type)
        form = root + affix
        forms = inflect_word(form, classes=inflection_classes, required_wclass='subst')

    # Case
    # https://kaino.kotus.fi/visk/sisallys.php?p=81
    # FIXME: komitatiivi
    key = expand_case_name.get(case, 'nominatiivi')
    if number == 'Plur':
        key = key + '_mon'
    form = forms.get(key, form)

    # Possessive suffix
    # https://kaino.kotus.fi/visk/sisallys.php?p=95
    if person_psor:
        if case  == 'Nom' or (case == 'Gen' and number == 'Sing'):
            form = _vowel_stem(forms, strong=True) or form
        if number == 'Plur' and form.endswith('t'):
            form = form[:-1]
        elif case == 'Tra':
            # -ksi -> -kse
            form = form[:-1] + 'e'

        if person_psor in ['1', '2']:
            if form.endswith('n'):
                form = form[:-1]
            psor_key = person_psor + '_' + (number_psor or 'Sing')
            form = form + possessive_suffixes[psor_key]
        elif person_psor == '3':
            if form.endswith('n'):
                suffix = 'sA' # nsA, but the 'n' is merged with the root form
            elif case == 'Nom' or (case == 'Par' and token.endswith('a')):
                suffix = 'nsA'
            elif is_vowel(form[-1]):
                suffix = form[-1] + 'n'
            else:
                suffix = 'nsA'

            form = _append_affix_with_vowel_harmony(form, suffix)

    return form


def inflect_pronoun(token: str,
                    *,
                    case: Literal['Abe', 'Abl', 'Acc', 'Ade', 'All', 'Com', 'Ela', 'Ess',
                                  'Gen', 'Ill', 'Ine', 'Ins', 'Nom', 'Par', 'Tra']='Nom',
                    number: Literal['Sing', 'Plur']='Sing'):
    # https://kaino.kotus.fi/visk/sisallys.php?p=100

    key = token + '_' + number
    key_case = key + '_' + case
    if key_case in pronoun_exceptions:
        return pronoun_exceptions[key_case]

    stem = pronoun_stems.get(key, token)
    affix = case_affixes.get(case, '')
    return _append_affix_with_vowel_harmony(stem, affix)


def _conjugate_verb_passive(token: str,
                            tense: Literal['Pres', 'Past'],
                            number: Literal['Sing', 'Plur'],
                            mood: Literal['Ind', 'Cnd', 'Imp', 'Pot'],
                            include_person_affix: bool = True) -> str:
    # https://kaino.kotus.fi/visk/sisallys.php?p=110

    forms = inflect_word(token, required_wclass='verbi')
    if 'imperfekti_pass' in forms:
        root = forms['imperfekti_pass'][:-4]
    else:
        # Guess the root
        root = token[:-2]

    affix = ''
    if mood == 'Cnd':
        affix = 'tAisi'
    elif mood == 'Pot':
        affix ='tAne'
    elif mood == 'Imp':
        affix = 'tAkO'
    elif tense == 'Past':
        affix = 'ti'
    elif len(root) >= 2 and is_vowel(root[-2]) and is_vowel(root[-1]):
        affix = 'dA'
    elif root and root[-1] in 'lrn':
        affix = root[-1] + 'A'
    elif root and root[-1] == 't':
        affix = 'A'
    else: # is_vowel(root[-1]) or root[-1] == 's':
        affix = 'tA'

    if include_person_affix:
        person_affix = affix[-1] + 'n'
        affix = affix + person_affix

    return _append_affix_with_vowel_harmony(root, affix)


def _conjugate_verb_indicative(token, tense, person, number):
    # https://kaino.kotus.fi/visk/sisallys.php?p=107
    forms = inflect_word(token, required_wclass='verbi')
    if tense == 'Pres' and token == 'olla':
        if person == '3':
            stem = 'on' if number == 'Sing' else 'ovat'
            affix = ''
        else:
            stem = forms['preesens_yks_1'][:-1]
            affix = verb_person_number_affix[person + '_' + number]
    elif tense == 'Pres':
        if 'preesens_yks_1' in forms:
            if person == '3':
                stem = _vowel_stem(forms, strong=True)
            else:
                stem = forms['preesens_yks_1'][:-1]
        else:
            # A very crude guess for the stem
            stem = token[:-1]
            while stem and not is_vowel(stem[-1]):
                stem = stem[:-1]

        if person == '3' and number == 'Sing':
            if _is_diphthong_or_long_vowel(stem[-2:]):
                affix = ''
            elif ((len(stem) >= 2 and not is_vowel(stem[-2]) and is_vowel(stem[-1])) or
                  _is_supistuma_verbi(forms)):
                affix = stem[-1]
            else:
                affix = ''
        else:
            affix = verb_person_number_affix[person + '_' + number]
    else: # tense = 'Past'
        if 'imperfekti_yks_3' in forms:
            if person == '3':
                stem = forms['imperfekti_yks_3']
            else:
                stem = forms['preesens_yks_1'][:-1]
                if (token.endswith('ltaa') or token.endswith('ltää') or
                    token.endswith('rtaa') or token.endswith('rtää') or
                    token.endswith('ntaa') or token.endswith('ntää') or
                    _is_supistuma_verbi(forms)):
                    stem = forms['imperfekti_yks_3']
                elif len(stem) >= 2 and stem[-1] == stem[-2] and is_vowel(stem[-1]):
                    stem = stem[:-1] + 'i'
                elif stem.endswith('e') or stem.endswith('ä'):
                    stem = stem[:-1] + 'i'
                elif _has_one_syllable_inaccurate(stem) and (stem[-2:] == 'ie' or
                                                             re.match('[uy][oö]', stem[-2:])):
                    stem = stem[:-2] + stem[-1] + 'i'
                elif _has_two_syllables_inaccurate(token) and stem[-1] == 'a':
                    fst_vowel = _first_vowel(stem)
                    if fst_vowel == 'a':
                        stem = stem[:-1] + 'oi'
                    elif fst_vowel in ['o', 'u']:
                        stem = stem[:-1] + 'i'
                    else:
                        stem = stem + 'i'
        else:
            # A very crude guess
            stem = token[:-1]
            if stem and stem[-1] != 'i' and is_vowel(stem[-1]):
                stem = stem + 'si'

        affix = verb_person_number_affix[person + '_' + number]

    return _append_affix_with_vowel_harmony(stem, affix)


def _conjugate_negation_verb(person, number, mood):
    if mood != 'Imp':
        mood = 'Ind'

    return ei_conjugation[f'{person}_{number}_{mood}']


def _conjugate_verb_connegative(token, tense, person, mood, number):
    # pääverbin kieltomuoto
    # https://kaino.kotus.fi/visk/sisallys.php?p=109
    if mood == 'Cnd':
        forms = inflect_word(token, required_wclass='verbi')
        return forms.get('kondit_yks_3', token)

    elif mood == 'Imp':
        # Note: imperative first person singular should never occur
        forms = inflect_word(token, required_wclass='verbi')
        if person in ('1', '2') and number == 'Sing':
            form = forms.get('preesens_yks_1')
            return form[:-1] if forms else token
        elif person == '3' or (person in ('1', '2') and number == 'Plur'):
            if 'imperatiivi_yks_3' in forms:
                stem = forms['imperatiivi_yks_3'][:-4]
            else:
                stem = token[:-2]
            return _append_affix_with_vowel_harmony(stem, 'kO')
        else: # person == '4'
            return _conjugate_verb_passive(token, tense, number, 'Imp', include_person_affix = False)

    elif mood == 'Pot':
        return _conjugate_verb_potential(token, person, number)

    else: # mood == 'Ind'
        forms = inflect_word(token, required_wclass='verbi')
        if person == '4' and tense == 'Pres':
            return _conjugate_verb_passive(token, tense, number, 'Ind', include_person_affix = False)
        if person == '4' and tense == 'Past':
            return _conjugate_verb_participle(token, '4', number, partform='Past')
        elif tense == 'Pres': # and person in ('1', '2', '3')
            form = forms.get('preesens_yks_1')
            return form[:-1] if form else token
        else: # tense == 'Past'
            if 'partisiippi_2' not in forms:
                return token

            if number == 'Sing':
                return forms['partisiippi_2']
            else: # number == 'Plur'
                return forms['partisiippi_2'][:-2] + 'eet'

    # should not be reached
    return token


def _conjugate_verb_infinite(token, infform):
    if infform == '1':
        return token

    # TODO: other infinite forms
    return token


def _conjugate_verb_participle(token, person, number, partform):
    # https://kaino.kotus.fi/visk/sisallys.php?p=122
    forms = inflect_word(token, required_wclass='verbi')
    if partform == 'Pres':
        if person == '4':
            form = forms.get('imperfekti_pass')
            if form:
                return _append_affix_with_vowel_harmony(form[:-4], 'tAvA')
        else:
            stem = _vowel_stem(forms, strong=True) or token
            return _append_affix_with_vowel_harmony(stem, 'vA')

    elif partform == 'Past':
        if person == '4':
            form = forms.get('imperfekti_pass')
            if form:
                return _append_affix_with_vowel_harmony(form[:-4], 'tU')
        elif 'partisiippi_2' in forms:
            form = forms['partisiippi_2']
            if number == 'Plur':
                return form[:-2] + 'eet'
            else:
                return form

    elif partform == 'Agt':
        stem = _vowel_stem(forms, strong=True) or token
        return _append_affix_with_vowel_harmony(stem, 'mA')

    else:
        raise ValueError(f'Invalid partform: {partform}')

    # should not be reached
    return token

def _conjugate_verb_conditional(token, person, number):
    # https://kaino.kotus.fi/visk/sisallys.php?p=116
    forms = inflect_word(token, required_wclass='verbi')
    stem = forms.get('kondit_yks_3', token)
    affix = verb_person_number_affix[person + '_' + number]
    return _append_affix_with_vowel_harmony(stem, affix)


def _conjugate_verb_imperative(token, person, number):
    # https://kaino.kotus.fi/visk/sisallys.php?p=118
    forms = inflect_word(token, required_wclass='verbi')
    if person == '2' and number == 'Sing':
        if 'preesens_yks_1' in forms:
            stem = forms['preesens_yks_1'][:-1]
        else:
            stem = token[:-2] + 'e'
    else:
        if 'imperatiivi_yks_3' in forms:
            stem = forms['imperatiivi_yks_3'][:-4]
        else:
            stem = token[:-2]
    affix = verb_imperative_person_number_affix[person + '_' + number]
    return _append_affix_with_vowel_harmony(stem, affix)


def _conjugate_verb_potential(token, person, number):
    # https://kaino.kotus.fi/visk/sisallys.php?p=117
    if token == 'olla':
        stem = 'lie'
    else:
        forms = inflect_word(token, required_wclass='verbi')
        stem = _consonant_or_vowel_stem_verb(forms, strong=True)
    if not stem:
        stem = token[:-2]

    affix = verb_potential_person_number_affix[person + '_' + number]
    if stem and stem[-1] in 'lrs':
        affix = stem[-1] + affix[1:]
    return _append_affix_with_vowel_harmony(stem, affix)


def _is_supistuma_verbi(forms):
    # https://kaino.kotus.fi/visk/sisallys.php?p=330

    inf = forms.get('infinitiivi_1', '')
    vowel_stem = _vowel_stem(forms, strong=True) or inf
    return ((inf.endswith('ta') or inf.endswith('tä')) and
            len(vowel_stem) >= 2 and is_vowel(vowel_stem[-2]) and
            (vowel_stem[-1] in 'aä' or vowel_stem[-2] == vowel_stem[-1]))


def _gradation_type(token):
    classes = WORD_CLASSES.get(token)
    if classes:
        fields = classes[0].split('-')
        if len(fields) == 3:
            return fields[-1]
    return None


def _consonant_or_vowel_stem_verb(forms, *, strong):
    """Return the consonant root of a verb if it exists, otherwise the vowel root"""
    # https://kaino.kotus.fi/visk/sisallys.php?p=55
    return forms.get('imperatiivi_yks_3', '')[:-4]


def _vowel_stem(forms, *, strong):
    """Return the vowel stem of a word.

    Return the strong vowel stem if strong is True, otherwise the weak
    vowel stem.
    """
    if 'preesens_yks_1' in forms: # verb
        inf1 = forms.get('infinitiivi_1', '')
        suora_astevaihtelu = _has_suora_astevaihtelu(inf1)
        if suora_astevaihtelu and strong:
            return inf1[:-1]
        elif not suora_astevaihtelu and not strong:
            stem = forms.get('imperfekti_pass')[:-4]
            while stem and not is_vowel(stem[-1]):
                stem = stem[:-1]
            return stem
        else:
            return forms['preesens_yks_1'][:-1]

    else: # nominal
        if strong and 'essiivi' in forms:
            return forms['essiivi'][:-2]
        elif not strong and 'genetiivi' in forms:
            return forms['genetiivi'][:-1]

    # Should not be reached
    return None


def _has_suora_astevaihtelu(token):
    return _gradation_type(token) in ['av1', 'av3', 'av5']


def _append_affix_with_vowel_harmony(stem, affix):
    """Append affix to stem and replace vowel placeholders (AOU) in the affix."""
    vowel_type = get_wordform_infl_vowel_type(stem)
    affix = replace_vowel_placeholders(affix, vowel_type)
    return stem + affix


def _has_one_syllable_inaccurate(word):
    return len(word) <= 3


diphthong_expression = 'aa|ee|ii|oo|uu|yy|ää|öö|ai|ei|oi|ui|yi|äi|öi|au|eu|iu|ou|äy|öy|iy|ey|ie|uo|yö'
def _has_two_syllables_inaccurate(word):
    """Does the word have two syllables?

    Inaccurate: misdetects some of the less common syllable types."""
    # the most syllables include CV, VV, or VC
    syllable_elements = [
        '[bcdfghjklmnpqrstvwxz][aeiouyäö]',
        diphthong_expression,
        '[aeiouyäö][bcdfghjklmnpqrstvwxz]',
    ]
    x = sum(1 for _ in re.finditer('|'.join(syllable_elements), word, re.IGNORECASE))
    return x <= 2


def _is_diphthong_or_long_vowel(two_character_string):
    return re.fullmatch(diphthong_expression, two_character_string) is not None


def replace_vowel_placeholders(s, vowel_type):
    def vowel_repl(vowel_class):
        if vowel_class.group(0) == 'A':
            return 'a' if vowel_type == VOWEL_BACK else 'ä'
        elif vowel_class.group(0) == 'O':
            return 'o' if vowel_type == VOWEL_BACK else 'ö'
        elif vowel_class.group(0) == 'U':
            return 'u' if vowel_type == VOWEL_BACK else 'y'
    return re.sub('[AOU]', vowel_repl, s)


def _first_vowel(word):
    for c in word:
        if is_vowel(c):
            return c
    return None


def is_vowel(c):
    return c.lower() in ['a', 'e', 'i', 'o', 'u', 'y', 'ä', 'ö', 'å']


def _split_compound_word(compound_word):
    """Split a compound word into modifier and element parts.

    Works only on compound words recognized by Voikko.
    """
    analyses = voikko.analyze(compound_word)
    if analyses:
        analysis = analyses[0]
        structure = analysis.get('STRUCTURE', '')
        i = structure.rfind('=')
        if i != 0 and i != len(structure) - 1:
            k = i - len(structure) + 1
            return compound_word[:k], compound_word[k:]

    return '', compound_word


# Hot patch to make libvoikko's vocabulary more compatible with voikko-fi 2.4
for key, val in WORD_CLASSES.items():
    if 'subst-kaunis' in val:
        WORD_CLASSES[key] = ['subst-vieras' if x == 'subst-kaunis' else x for x in val]
    if 'subst-tosi' in val:
        WORD_CLASSES[key] = ['subst-susi' if x == 'subst-tosi' else x for x in val]
    if 'verbi-taitaa' in val:
        WORD_CLASSES[key] = ['verbi-hohtaa-av1' if x == 'verbi-taitaa' else x for x in val]
