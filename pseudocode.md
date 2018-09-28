# Hangman (Pseudocode)

```
#Insert the code between the backticks
  
input secret word
get the length of the word
declare guess count
make string of underscores for number of characters in word
declare guess wariable

while number of guesses is less than 6 and number of guesses is not = "win":
  get guess input
  find length of input
  
  if length of guess is greater than 1:
    if guess == word:
      guess count = "win"
  else:
    number of guesses += 1
   
  if length of guess == 1:
    if guess is in word:
      for each instance of guess in word:
        replace the underscores in guess string with the letter
    else:
      number of guesses += 1
  
  if number of guesses = "win"
    print("You Win!")
    break()
  elif number of guesses >= 6:
    print('You LOSE')
    print('the word was', secret word)
    break()
  else:
    print("So far, your guess turn out to be:", Underscore guesses)
    print("You have", 6 - number of guesses, "left")

```
