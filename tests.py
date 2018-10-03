from hangman import *

def test_get_secret_word():
    words = {get_secret_word() for _ in range(100)}
    assert len(words) >= 5, "Should contain a list of at least 5 words."
    
    # do the following:
    assert what secret word returns is a string, "Should return a string"


def test_word_is_solved():
    assert word_is_solved("hello", "eh") == False, "Should not be solved guesses: 'eh' for word: 'hello'."
    assert word_is_solved("world", "dorlw") == True, "Should be solved"

    
def test_display_letters():
    assert display_letters("hello", "h") == "h _ _ _ _", "Should reveal only first letter"
    assert display_letters("hello", "l") == "_ _ l l _", "Should display both characters"
    assert display_letters("aaa", "bca") == "a a a", "Should display all characters"
    assert display_letters("world", "yqae") == "_ _ _ _ _", "Should display no letters"
    assert display_letters(" ", "guess") == " ", "Should display the space"
    assert display_letters("hello ", "gueso") == "_ e _ _ o  ", "should display e and o"
    assert display_letters("ppap", "pp") == "p p _ p", "Should print three p's"
    assert display_letters("bye bye", " ") == "_ _ _   _ _ _", "Should print proper blanks"
    assert display_letters("", "aswe") == "", "Should not print anything"
    assert display_letters("he llo", "a a a h") == "h _   _ _ _", "Should print the space and the h"

    
# Test display_platform(wrong_guesses)
# display_platform("a") -> display with head


