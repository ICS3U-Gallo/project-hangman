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

1. create new drawing of a post with a hanging noose (head on top)
2. ask player for a word
3. split word into seperate letters
4. prompt player two to guess the letters
5. if more than 2 total players, alternate turns between guessers
6. for every incorrect guess, add one of five body parts to the noose (chest, left and right arms, left and right legs)
7. continue process until either players gets the correct letters, or loses all five body parts 

```




