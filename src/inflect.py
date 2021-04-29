import re
from typing import Literal, Optional
from voikko.inflect_word import inflect_word, WORD_CLASSES
from voikko.voikkoinfl import __apply_gradation
from voikko.voikkoutils import VOWEL_BACK, get_wordform_infl_vowel_type

vowels = 'aeiouyäöå'
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

def conjugate_verb(token: str,
                   *,
                   tense: Literal['Pres', 'Past'],
                   person: Literal['1', '2', '3', '4'],
                   number: Literal['Sing', 'Plur'],
                   mood: Literal['Ind', 'Cnd', 'Imp', 'Pot'],
                   connegative: bool=False) -> str:
    if token == 'ei':
        return _conjugate_negation_verb(person, number, mood)

    elif connegative:
        return _conjugate_verb_connegative(token, tense, person, mood, number)

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
                    case: str,
                    number: Literal['Sing', 'Plur'],
                    degree: Optional[Literal['Pos', 'Cmp', 'Sup']] = None,
                    person_psor: Optional[Literal['1', '2', '3']] = None,
                    number_psor: Optional[Literal['Sing', 'Plur']] = None):
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
                elif len(root) >= 2 and root[-2] not in vowels and root[-1] in 'aeä':
                    root = root[:-1]
                elif len(root) >= 2 and root[-2] in vowels and root[-1] in vowels:
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
            elif form[-1] in vowels:
                suffix = form[-1] + 'n'
            else:
                suffix = 'nsA'

            form = _append_affix_with_vowel_harmony(form, suffix)

    return form


def inflect_pronoun(token: str,
                    *,
                    case: str,
                    number: Literal['Sing', 'Plur']):
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
    elif len(root) >= 2 and root[-2] in vowels and root[-1] in vowels:
        affix = 'dA'
    elif root and root[-1] in 'lrn':
        affix = root[-1] + 'A'
    elif root and root[-1] == 't':
        affix = 'A'
    else: # root[-1] in vowels or root[-1] == 's':
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
            stem = forms['preesens_yks_1'][:-1]
            grad = _gradation_type(token)
            if grad in ['av1', 'av3', 'av5'] and person == '3':
                # Suora astevaihtelu, tarvitaan heikko vartalo
                grad_tuple = __apply_gradation(forms['preesens_yks_1'], grad)
                if grad_tuple is not None:
                    stem = grad_tuple[0][:-1]
        else:
            # A very crude guess for the stem
            stem = token[:-1]
            while stem and stem[-1] not in vowels:
                stem = stem[:-1]

        if (person == '3' and number == 'Sing' and
            ((len(stem) >= 2 and stem[-2] not in vowels and stem[-1] in vowels) or
             _is_supistuma_verbi(forms))):
            affix = stem[-1]
        else:
            affix = verb_person_number_affix[person + '_' + number]
    else:
        if 'imperfekti_yks_3' in forms:
            stem = forms['imperfekti_yks_3']
            grad = _gradation_type(token)
            if grad in ['av1', 'av3', 'av5'] and person in ['1', '2']:
                # Suora astevaihtelu, tarvitaan vahva vartalo
                grad_tuple = __apply_gradation(stem, grad)
                if grad_tuple:
                    stem = grad_tuple[1]
        else:
            # A very crude guess
            stem = token[:-1]
            if stem and stem[-1] != 'i' and stem[-1] in vowels:
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
        if person == '4':
            return _conjugate_verb_passive(token, tense, number, 'Ind', include_person_affix = False)
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
        stem = _consonant_or_vowel_stem(forms)
    if not stem:
        stem = token[:-2]

    affix = verb_potential_person_number_affix[person + '_' + number]
    if stem and stem[-1] in 'lrs':
        affix = stem[-1] + affix[1:]
    return _append_affix_with_vowel_harmony(stem, affix)


def _is_supistuma_verbi(forms):
    # https://kaino.kotus.fi/visk/sisallys.php?p=330

    inf = forms.get('infinitiivi_1', '')
    preesens_yks_1 = forms.get('preesens_yks_1', '---')
    return ((inf.endswith('ta') or inf.endswith('tä')) and
            ((preesens_yks_1[-2] == 'a') or
             (len(preesens_yks_1) >= 3 and preesens_yks_1[-2] in vowels and preesens_yks_1[-3] in vowels)))


def _gradation_type(token):
    classes = WORD_CLASSES.get(token)
    if classes:
        fields = classes[0].split('-')
        if len(fields) == 3:
            return fields[-1]
    return None


def _consonant_or_vowel_stem(forms):
    """Return the consonant root of a verb if it exists, otherwise the vowel root"""
    # https://kaino.kotus.fi/visk/sisallys.php?p=55

    candidate_form = forms.get('imperatiivi_yks_3', '')[:-4]
    return candidate_form or None


def _vowel_stem(forms, *, strong):
    """Return the vowel stem of a nominal word.

    Return the strong vowel stem is strong is True, otherwise the weak
    vowel stem.
    """
    if strong and 'essiivi' in forms:
        return forms['essiivi'][:-2]
    elif not strong and 'genetiivi':
        return forms['genetiivi'][:-1]
    else:
        return None


def _append_affix_with_vowel_harmony(stem, affix):
    """Append affix to stem and replace vowel placeholders (AOU) in the affix."""
    vowel_type = get_wordform_infl_vowel_type(stem)
    affix = replace_vowel_placeholders(affix, vowel_type)
    return stem + affix


def _has_two_syllables_inaccurate(word):
    """Does the word have two syllables?

    Inaccurate: misdetects some of the less common syllable types."""
    # the most syllables include CV, VV, or VC
    syllable_elements = [
        '[bcdfghjklmnpqrstvwxz][aeiouyäö]',
        'aa|ee|ii|oo|uu|yy|ää|öö|ai|ei|oi|ui|yi|äi|öi|au|eu|iu|ou|äy|öy|iy|ey|ie|uo|yö',
        '[aeiouyäö][bcdfghjklmnpqrstvwxz]',
    ]
    x = sum(1 for _ in re.finditer('|'.join(syllable_elements), word, re.IGNORECASE))
    return x <= 2


def replace_vowel_placeholders(s, vowel_type):
    def vowel_repl(vowel_class):
        if vowel_class.group(0) == 'A':
            return 'a' if vowel_type == VOWEL_BACK else 'ä'
        elif vowel_class.group(0) == 'O':
            return 'o' if vowel_type == VOWEL_BACK else 'ö'
        elif vowel_class.group(0) == 'U':
            return 'u' if vowel_type == VOWEL_BACK else 'y'
    return re.sub('[AOU]', vowel_repl, s)


# Hot patch to make libvoikko's vocabulary more compatible with voikko-fi 2.4
for key, val in WORD_CLASSES.items():
    if 'subst-kaunis' in val:
        WORD_CLASSES[key] = ['subst-vieras' if x == 'subst-kaunis' else x for x in val]
    if 'subst-tosi' in val:
        WORD_CLASSES[key] = ['subst-susi' if x == 'subst-tosi' else x for x in val]
