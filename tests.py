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
    assert display_letters("hello", "he") == "h e _ _ _", "Should reveal first and second letters"
    assert display_letters("hello", "heo") == "h e _ _ o", "Should reveal first, second, and last letters"
    assert display_letters("hello", "hoel") == "h e l l o", "Should reveal all letters"    


def test_display_platform():
    # Test display_platform(wrong_guesses)
    # display_platform("a") -> display with head
    # display_platform("serw") -> display with head, body, 2 arms
    # display_platform("qwertyiop") -> display with head, body, 2 arms, 2 legs (final diplay)
    # display_platform("")-> display blank platform
    pass


def test_get_guess():
    # Test case 1: 
    # input: "AB", 
    # expected result: 'Character is invalid. Enter a letter:'

    # Test case 2: 
    # input: "A", 
    # expected result: The letter is returned (testable by assigning a variable and printing.)

    # Test case 3: 
    # input: An apostrophe,
    # expected result: 'Character is invalid. Enter a letter:'

    # Test case 4: 
    # input: "1",
    # expected result: 'Character is invalid. Enter a letter:'

    # Test case 5: 
    # input: "d",
    # expected result: the letter is returned (testable by assigning a variable and printing.)
    pass
