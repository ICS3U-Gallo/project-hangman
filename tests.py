from hangman import *


def test_get_secret_word():
    words = {get_secret_word() for _ in range(100)}
    assert len(words) >= 5, "Should contain a list of at least 5 words."
    
    # do the following:
    assert what secret word returns is a string, "Should return a string"


def test_word_is_solved():
    assert word_is_solved("hello", "eh") == False,"Should not be solved guesses: 'eh' for word: 'hello'."
    assert word_is_solved("world", "dorlw") == True,"Should be solved"
    assert word_is_solved("paper", "ptaru") == False,"Should not be solved guesses: 'ptaru' for word: 'paper'."
    assert word_is_solved("table", "aeotbhl") == True,"Should be solved"
    assert word_is_solved("hello world", "eawldhotr") == True,"Should be solved"
    assert word_is_solved("hello world", "eawdhotr") == False,"Should not be solved guesses: 'eawl dhotr' for word:'hello world'."

    
def test_display_letters():
    assert display_letters("hello", "h") == "h _ _ _ _", "Should reveal only first letter"

    
# Test display_platform(wrong_guesses)
# display_platform("a") -> display with head
