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

ask user for a word
for each letter in the word:
  print out a dash
  
print out gallows
print out empty word bank 
win is false

while man is not fully hanged:
  ask user to guess a letter
  
  if the input is longer than one character and the input is not the word:
    draw a body part on the man on the gallows
    add input to the word bank
    
  if the letter is part of the word:
    for each letter in the word:
      if the two letters are equal:
        replace the respective dash with the letter
        
  if the letter is not in the word:
    add the letter to the word bank
    draw another body part to the man on the gallows
  
  if all letters are guessed or input is the same as the word:
    win is true
    replace the dashes with the word
    end the loop
    
if player wins:
  print out a congratulation message to the user
  
else:
  print out a message saying the user loses
  print the word entered at the beginning

if player wants to play again:
  clear screen
  loop back to the start
else:
  close game
```
