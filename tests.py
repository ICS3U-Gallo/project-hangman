def get_secret_word():
    # Gallo will do a couple.
    # do the following:


def test_word_is_solved():
    assert word_is_solved("hello", "eh") == False, "Should not be solved guesses: 'eh' for word: 'hello'."
    assert word_is_solved("world", "dorlw") == True, "Should be solved"
    
def test_display_letters():
    assert display_letters("hello", "h") == "h _ _ _ _", "Should reveal only first letter"

    
# Test display_platform(wrong_guesses)
# display_platform("a") -> display with head


