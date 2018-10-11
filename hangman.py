# hangman.py


def main():
    show_title_screen()
    secret_word = get_secret_word()
    correct_guesses = ""
    wrong_guesses = ""

    while (not word_is_solved(secret_word, correct_guesses) and
            not player_is_dead(wrong_guesses)):
        display_platform(wrong_guesses)
        print(get_blanked_word(secret_word, correct_guesses))
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
    import random
    word_bank = ['apple', 'banana', 'orange', 'pear', 'mango', 'grapes']
    secret_word = random.choice(word_bank)
    return secret_word


def word_is_solved(word, guesses):
    """Will check to see if a word has been completely solved.
    Args:
        word (str): The secret word
        guesses (str): The string containing all correct guesses
    Returns:
        bool: True if word is solved, False if word is not.
    """

    for letter in word.lower():
        if letter not in guesses and letter != ' ':
            return False

    return True


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


def get_blanked_word(word, guesses):
    """Displays (prints) the letter-board,
    underscores (_) for letters not yet guessed.
    Args:
        word (str): The secret word
        guesses (str): A string of correct guesses
    """
    letters = list(word)
    guesses = list(set(guesses))
    word_list = list(word)
    for k in range(len(word)):
        if(letters[k] != " "):
            letters[k] = "_"
    for guess_letter in guesses:
      num_of_guess_letters = word.count(guess_letter)
      for j in range(num_of_guess_letters):
          if(guess_letter in word):
              ind = word_list.index(guess_letter)
              letters[ind] = guess_letter
              word_list[ind] = "_"
    return " ".join(letters)

def get_guess():
    """Will take the user's guess. Ensures the input is valid.
    """

    while True:
        guess = input("Enter your guess: ")
        if all(letter.isalpha() or letter.isspace() for letter in guess):
            return guess.lower()
        print("Invalid guess! Please make sure your guess only contains letters or spaces. ")


def show_win_screen():
    """Will display ASCII art for a win screen"""
    print("""
 ▄         ▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄         ▄       ▄         ▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄        ▄  ▄ 
▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░▌       ▐░▌     ▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░░▌      ▐░▌▐░▌
▐░▌       ▐░▌▐░█▀▀▀▀▀▀▀█░▌▐░▌       ▐░▌     ▐░▌       ▐░▌ ▀▀▀▀█░█▀▀▀▀ ▐░▌░▌     ▐░▌▐░▌
▐░▌       ▐░▌▐░▌       ▐░▌▐░▌       ▐░▌     ▐░▌       ▐░▌     ▐░▌     ▐░▌▐░▌    ▐░▌▐░▌
▐░█▄▄▄▄▄▄▄█░▌▐░▌       ▐░▌▐░▌       ▐░▌     ▐░▌   ▄   ▐░▌     ▐░▌     ▐░▌ ▐░▌   ▐░▌▐░▌
▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░▌       ▐░▌     ▐░▌  ▐░▌  ▐░▌     ▐░▌     ▐░▌  ▐░▌  ▐░▌▐░▌
 ▀▀▀▀█░█▀▀▀▀ ▐░▌       ▐░▌▐░▌       ▐░▌     ▐░▌ ▐░▌░▌ ▐░▌     ▐░▌     ▐░▌   ▐░▌ ▐░▌▐░▌
     ▐░▌     ▐░▌       ▐░▌▐░▌       ▐░▌     ▐░▌▐░▌ ▐░▌▐░▌     ▐░▌     ▐░▌    ▐░▌▐░▌ ▀ 
     ▐░▌     ▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌     ▐░▌░▌   ▐░▐░▌ ▄▄▄▄█░█▄▄▄▄ ▐░▌     ▐░▐░▌ ▄ 
     ▐░▌     ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌     ▐░░▌     ▐░░▌▐░░░░░░░░░░░▌▐░▌      ▐░░▌▐░▌
      ▀       ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀       ▀▀       ▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀        ▀▀  ▀ 
""")


def show_lose_screen():
    """Will display ASCII art for a lose screen"""
    print("""
 ▓██   ██▓ ▒█████   █    ██     ██▓     ▒█████    ██████ ▓█████                
 ▒██  ██▒▒██▒  ██▒ ██  ▓██▒   ▓██▒    ▒██▒  ██▒▒██    ▒ ▓█   ▀                
  ▒██ ██░▒██░  ██▒▓██  ▒██░   ▒██░    ▒██░  ██▒░ ▓██▄   ▒███                  
  ░ ▐██▓░▒██   ██░▓▓█  ░██░   ▒██░    ▒██   ██░  ▒   ██▒▒▓█  ▄                
  ░ ██▒▓░░ ████▓▒░▒▒█████▓    ░██████▒░ ████▓▒░▒██████▒▒░▒████▒ ██▓  ██▓  ██▓ 
   ██▒▒▒ ░ ▒░▒░▒░ ░▒▓▒ ▒ ▒    ░ ▒░▓  ░░ ▒░▒░▒░ ▒ ▒▓▒ ▒ ░░░ ▒░ ░ ▒▓▒  ▒▓▒  ▒▓▒ 
 ▓██ ░▒░   ░ ▒ ▒░ ░░▒░ ░ ░    ░ ░ ▒  ░  ░ ▒ ▒░ ░ ░▒  ░ ░ ░ ░  ░ ░▒   ░▒   ░▒  
 ▒ ▒ ░░  ░ ░ ░ ▒   ░░░ ░ ░      ░ ░   ░ ░ ░ ▒  ░  ░  ░     ░    ░    ░    ░   
 ░ ░         ░ ░     ░            ░  ░    ░ ░        ░     ░  ░  ░    ░    ░  
 ░ ░                                                             ░    ░    ░  
""")


def show_title_screen():
    """Will display ASCII art for a title screen, pauses until user continue"""
    print("""
              (#/                  
               (,                  
               (*                  
              .(,                  ____    ____      _     ___      ___   ____   ___       ___      _     ___      ___
          ,// .#,                  `MM'    `MM'     dM.    `MM\     `M'  6MMMMb/ `MMb     dMM'     dM.    `MM\     `M'
            (//##%,                 MM      MM     ,MMb     MMM\     M  8P    YM  MMM.   ,PMM     ,MMb     MMM\     M 
            /%%(%(/                 MM      MM     d'YM.    M\MM\    M 6M      Y  M`Mb   d'MM     d'YM.    M\MM\    M 
            /(%(/                   MM      MM    ,P `Mb    M \MM\   M MM         M YM. ,P MM    ,P `Mb    M \MM\   M 
            /##%/#(                 MMMMMMMMMM    d'  YM.   M  \MM\  M MM         M `Mb d' MM    d'  YM.   M  \MM\  M 
           /%&(*(%                  MM      MM   ,P   `Mb   M   \MM\ M MM     ___ M  YM.P  MM   ,P   `Mb   M   \MM\ M 
           (%%%#(,                  MM      MM   d'    YM.  M    \MM\M MM     `M' M  `Mb'  MM   d'    YM.  M    \MM\M 
             ###(                   MM      MM  ,MMMMMMMMb  M     \MMM YM      M  M   YP   MM  ,MMMMMMMMb  M     \MMM 
            (%  #(                  MM      MM  d'      YM. M      \MM  8b    d9  M   `'   MM  d'      YM. M      \MM 
           *#    *#*               _MM_    _MM_dM_     _dMM_M_      \M   YMMMM9  _M_      _MM_dM_     _dMM_M_      \M 
         /##       ##              
        ,(          ,#(            
       (*             (,           
      /(               ((          
     /(                 ##         
    //                   (*        
   *(                    .*.       
   #/                     (/       
   /,                     ((       
   *,                     */       
    /*                   //        
     #*                 (#         
      ##,             /((          
        //*,.    ,,,*%             
            .### .                 
                                   
""")
    input("Press enter to continue...")

if __name__ == "__main__":
    main()
