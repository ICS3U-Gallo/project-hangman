# Hangman (Pseudocode)
```
word = random word
correct_guesses = " "
worng_guesses = ""

while not solved and not dead:
  display the word.
  display the platform

  guess = get guess
  
  Check if guess is a word:
      check if guess is the word: win
      else: lose

  if guess is correct:
    add guess to correct_guesses
  else:
    add guess to wrong_guesses

if body is complete: desplay loser
if the word is fully guess: 
  display winner 
  end game

```
