# Hangman (Pseudocode)

```
get user input for the theme
get user input for the word (based on the theme)
clear the screen

while player has not won *and* incorrect guesses are less than 10
  print (10 - incorrect guesses) guesses remaining
  print guessed letters and replace not guessed letters with underscores
  accept user input
  compare letter with letters in word
  if correct, add to guessed letters
  otherwise increment incorect guesses
  if all letters guessed, declare winner
end loop
print winner if winner is true otherwise print loser

```
