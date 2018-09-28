# Hangman (Pseudocode)

```
Generate a word
Display letters in the word as underscore 
Display the platform
Ask player for a letter
Player chooses a letter
Check if the letter is found in the word
  If the letter is in the word, display the letter
    Add letter to string of correct guesses
  If the letter is not in the word, display a (new) part of the body and the letter in a separate list
    Add letter to string of incorrect guesses
Continue choosing and checking a letter
  If player chooses all the letters in the word, they win
  If the whole body is displayed before player 2 chooses all the letter, they lose
Game ends


```
