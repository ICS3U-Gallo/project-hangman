# Hangman (Pseudocode)

```
player 1 chooses a word
create blank variable 
for letter count in secret word add "_ " to blank variable
create wrong letter variable
create wrong letter counter
start while loop
player 2 guesses letter in word
if letter is in the word replace blank with coresponding letter
if letter is not in the word add letter to wrong variable and add 1 to counter
if counter hits 5 you lose and end loop
if you guess all letters in word you win and end loop
```
