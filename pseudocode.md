# Hangman (Pseudocode)

```
One of the players inputs a word 
Draw the number of lines that corresponds to the number of letters in the word 
draw a hangman base 
player 2 guesses a letter
if it's included in the word, insert the letter on the right line
if not, write the letter at the bottom under the lines and add the sequencial body part: 
1. head
2. body
3. right arm
4. left arm
5. right leg
6. left leg 
loop back to the 4th step until either: 
the hangman is complete (6 incorrect letters guessed) 
  show winner 
or the word is complete 
  show winner
```
