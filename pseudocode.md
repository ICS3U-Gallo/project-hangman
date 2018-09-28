# Hangman (Pseudocode)
```
Computer chooses a word from a list
word = random word
Add the players guess into two variables based on result
correct_guesses = " "
worng_guesses = " "

loop if not solved and not dead:
  Computer displays as many underscores as the number of letters in the word
  display the word.
  display the platform

  Player guesses a letter
  guess = get guess
  Check if guess is the word

  Replace letter in the designated spot when right
  if guess is correct:
    add guess to correct_guesses
  Draw updated platform when the guess is wrong.
  else:
    add guess to wrong_guesses

if body is complete: desplay loser
if the word is fully guess: 
  display winner 
  end game

```
