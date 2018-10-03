# hangman.py 

def main():
    secret_word = get_secret_word()
    correct_guesses = ""
    wrong_guesses = ""

    while (not word_is_solved(secret_word, correct_guesses) and
            not player_is_dead(wrong_guesses)):
        display_platform(wrong_guesses)
        display_letters(secret_word, correct_guesses)
        guess = get_guess()
        
        if len(guess) > 1:
            if guess == secret_word:
                correct_guessses = guess
                break
            else:
                wrong_guesses = wrong_guesses + "*"
        else:
            if guess in secret_word:
                correct_guesses = correct_guesses + guess
            else:
                wrong_guesses = wrong_guesses + guess 


    if word_is_solved(secret_word, correct_guesses):
        show_win_screen()
    else:
        show_lose_screen()


def get_secret_word():
    """Will return a single word from a list of words.
    Returns:
        Single word from a list
    """
    pass


def word_is_solved(word, guesses):
    """Will check to see if a word has been completely solved.
    Args:
        word (str): The secret word
        guesses (str): The string containing all correct guesses
    Returns:
        bool: True if word is solved, False if word is not.
    """
    pass


def player_is_dead(wrong_guesses):
    """Determines if the player is dead (too many guesses).
    Args:
        bad_guesses (str): A string containing all of the wrong guesses
    Returns
        bool: True if dead, False otherwise
    """
    pass


def display_platform(wrong_guesses):
    """
    Displays (prints) hanging platform based on how many incorrect guesses.
    Args: 
        wrong_guesses (str): A string containing all wrong guesses.
    """
    if len(wrong_guesses) == 0: 
        display_platform0 = '''        
                          _______________
                          |             |            
                                        |
                                        |
                                        |
                                        |
                                        |
                                        |
                                        | 
                                        |
                                        |
                             |====================|  ''' 
        print(display_platform0)

    if len(wrong_guesses) == 1:
        display_platform1 = '''   
                        _______________
                        |             |
                       ____           |
                      { * *}          |
                       ----           |
                                      |
                                      |
                                      |
                                      |
                                      | 
                                      |
                                      |
                          |====================|  '''
        print(display_platform1)

    if len(wrong_guesses) == 2:
        display_platform2 = '''   
                        _______________
                        |             |
                       ____           |
                      { * *}          |
                       ----           |
                        []            |
                        []            |
                        []            |
                                      |
                                      | 
                                      |
                          |====================|  '''
        print(display_platform2)

    if len(wrong_guesses) == 3:
        display_platform3 = '''   
                        _______________
                        |             |
                       ____           |
                      { * *}          |
                       ----           |
                        [] \          |
                        []  \         |
                        []   O        |
                                      |
                                      | 
                                      |
                                      |
                          |====================|  '''
        print(display_platform3)

    if len(wrong_guesses) == 4:
        display_platform4 = '''   
                        _______________
                        |             |
                       ____           |
                      { * *}          |
                       ----           |
                      / [] \          |
                     /  []  \         |
                    O   []   O        |
                                      |
                                      |
                                      |
                                      |
                          |====================|   '''
        print(display_platform4)

    if len(wrong_guesses) == 5:
        display_platform5 = '''   
                        _______________
                        |             |
                       ____           |
                      { * *}          |
                       ----           |
                      / [] \          |
                    /   []  \         |
                    O   []   O        |
                        |             |
                        |             | 
                      ==|             |
                                      |
                          |====================|  '''
        print(display_platform5)

    if len(wrong_guesses) == 6:
        display_platform6 = '''   
                        _______________
                        |             |
                       ____           |
                      { * *}          |
                       ----           |
                      / [] \          |
                     /  []  \         |
                    O   []   O        |
                        ||            |
                        ||            | 
                      ==||==          |
                                      |
                          |====================|  '''
        print(display_platform6)


def display_letters(word, guesses):
    """Displays (prints) the letter-board,
    underscores (_) for letters not yet guessed.
    Args:
        word (str): The secret word
        guesses (str): A string of correct guesses
    """
    pass


def get_guess():
    """Will take the user's guess. Ensures the input is valid.
    """
    pass


def show_win_screen():
    """Will display ASCII art for a win screen"""
    pass


def show_lose_screen():
    """Will display ASCII art for a lose screen"""
    pass


if __name__ == "__main__":
    main()
