import sys
import json
from typing import Union
from difflib import SequenceMatcher, get_close_matches


def translate(word: str) -> Union[list, None]:
    """Gets a word returns its meaning based on a json dictionary.

    Parameters
    ----------
    word : str
        the word that the user wants a definition for.

    Returns
    -------
    list
        a list that contains the translation for a word if that word
        is found in the json dictionary.
    None
        if the word is not found within a dictionary
    """
    if word.lower() in data:
        return data[word.lower()]
    elif  word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    else:
        return


def print_noun_and_verb(translated_word: list) -> None:
    """Gets a translated word and print its 'noun' and, if also available, 
    its 'verb'.

    Parameters
    ----------
    translated_word : list
        the list contaning the noun and the verb for a translated word.

    Returns
    -------
    None
        a list that contains the translation for a word if that word
        is found in the json dictionary.
    """
    print('')
    if len(translated_word) == 1:
        noun = (translated_word)[0]
        print(f'Noun.\n{noun}\n')
    else:
        noun = (translated_word)[0]
        verb = translated_word[1]
        print(f'Noun.\n{noun}\n')
        print(f'Verb.\n{verb}\n')
    return


data = json.load(open('data.json'))

while True:
    inputed_word = input('Please, enter your word or "999" to leave: ')
    print('')
    if any(str.isdigit(character) for character in inputed_word) \
        and inputed_word != '999':
        print('This not a valid input.')
        continue
    elif inputed_word == '999':
        print('Okay, leaving. See ya!')
        sys.exit()
    else:
        inputed_word = inputed_word
        break

translated_word = translate(inputed_word)
if translated_word is None:
    print('Sorry, the typed word does not exist in our dictionary.')
    # The cutoff is a score threshold value of similarity between the typed word and the similar one.
    # 'n' is the number of elements that the function 'get_close_matches' will return in a list.
    # Because we are only interested in the most similar element, n=1 is enough.
    close_matches = get_close_matches(inputed_word, data.keys(), cutoff=0.7, n=1)
    if len(close_matches) > 0:
        close_matches = close_matches[0]
        print(f'Did you mean: {close_matches}?\n')
        while True:
            close_match_user_response = input('Type your answer [Yes/No]: ')
            if close_match_user_response.title().replace(' ', '') not in ['Yes', 'No']:
                print('\nSorry, did not understand your answer. Please type "Yes" or "No" only.\n')
                continue
            else:
                break
        if close_match_user_response.title().replace(' ', '') == 'Yes':
            inputed_word = close_match_user_response
            translated_word = translate(close_matches)
            print_noun_and_verb(translated_word)
        else:
            print('Please, check it again.\n')
    else:
        print('Please, check the word again.\n')
else:
    print_noun_and_verb(translated_word)
