# hangman.py 
"""
replaces words with the underscores and changes underscores back into characters
"""

def display_letters(word, guesses):
    word_bank = list(word)
    guess = list(set(guesses))
    charac = list(word)
    lengguess = len(guesses)
    lengword = len(word)
    for l in range(0, lengword):
        if(charac[l] != " "):
           charac[l] = " _"
        for a in range(0, lengguess):
            for l in range(0, word.count(guesses[a])):
                if(guess[a] in word):
                    und = word_bank.index(guesses[a])
                    word_bank[und] = " _"
                    charac[und] = guesses[a]
        return " ".join(charac)

