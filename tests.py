from hangman import *

def test_get_secret_word():
    words = {get_secret_word() for _ in range(100)}
    assert len(words) >= 5, "Should contain a list of at least 5 words."
    
    # do the following:
    assert what secret word returns is a string, "Should return a string"


def test_word_is_solved():
    assert word_is_solved("hello", "eh") == False, "Should not be solved guesses: 'eh' for word: 'hello'."
    assert word_is_solved("world", "dorlw") == True, "Should be solved"
    # Multiple occurences of letter
    assert word_is_solved("aaaabbbb", "ab") == True, "Should be solved: 'ab' for word 'aaaabbbb'."
    assert word_is_solved("aaabbbccc", "bc") == False, "Should not be solved: 'bc' for word 'aaabbbccc'"
    # Multiple words
    assert word_is_solved("aaabb bcc c", "abc") == True, "Should solve multiple words."
    # Multiple words, mixed case
    assert word_is_solved("CaPiTaL lEtTeRs", "capitlers") == True, "Should be solved: 'capitlers' for word 'CaPiTaL lEtTeRs'."
    assert word_is_solved("UPPER lower", "uper") == False, "Should not be solved: 'uper' for word 'UPPER lower'."

    
def test_get_blanked_word():
    assert get_blanked_word("hello", "h") == "h _ _ _ _", "Should reveal only first letter"
    assert get_blanked_word("hello", "l") == "_ _ l l _", "Should display both characters"
    assert get_blanked_word("aaa", "bca") == "a a a", "Should display all characters"
    assert get_blanked_word("world", "yqae") == "_ _ _ _ _", "Should display no letters"
    assert get_blanked_word(" ", "guess") == " ", "Should display the space"
    assert get_blanked_word("hello ", "gueso") == "_ e _ _ o  ", "should display e and o"
    assert get_blanked_word("ppap", "pp") == "p p _ p", "Should print three p's"
    assert get_blanked_word("bye bye", " ") == "_ _ _   _ _ _", "Should print proper blanks"
    assert get_blanked_word("", "aswe") == "", "Should not print anything"
    assert get_blanked_word("he llo", "a a a h") == "h _   _ _ _", "Should print the space and the h"
    
# Test display_platform(wrong_guesses)
# display_platform("a") -> display with head


