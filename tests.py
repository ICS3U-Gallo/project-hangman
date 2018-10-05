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
    assert display_letters("hello", "hello") == "h e l l o", "Should reveal entire word"
    assert display_letters("hello", "wptrk") == "_ _ _ _ _", "Should reveal nothing of the word"
    assert display_letters("hello john", "hlljoenh") == "h e l l o  j o h n", "Should reveal whole phrase"
    assert display_letters("hello john", "eljh") == "_ e l l _  j _ h _", "Should reveal most characters"
    assert display_letters("wow", "w") == "w _ w", "Should only reveal w's"
    assert display_letters("yesterday", "ystd") == "y _ s t _ _ d _ y", "Should reveal most characters"
    assert display_letters("wow thats cool" "") == "_ _ _  _ _ _ _ _  _ _ _ _", "Should reveal nothing but underscores"
    assert display_letters("wow thats cool", "woclthas") == "w o w  t h a t s  c o o l", "Should reveal entire phrase"
    assert display_letters("josh is the best", "osh") == "_ o s h  _ s  _ h _  _ _s_", "Should reveal most characters"
    assert display_letters("wowie" "abcdfghjklmnpqrstuvxyz") == "_ _ _ _ _", "Should only reveal underscores"
    assert display_letters("handy", "ad") == "_ a _ d _", "Should reveal ad"
    assert display_letters("tiredness", "tnsd") == "t _ _ _ d n _ s s", "Should reveal some characters"


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
