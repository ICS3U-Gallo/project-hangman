# Hangman (Pseudocode)

```
Input a word
display hangman and underscores
output("/n/n/n")
for i in length of string word
if i is a space, output space
otherwise you output an underscore

Input a letter
for i in a set of word
if letter == i
    replace all instances of i in the underscore
    remove i from set
    repeat

elif no underscores
then print 'Winner, winner, chicken dinner"
 
else i != letter in the input 
    add to incorrect set
    print set
    print graphic on hangman
if hangman == max
    print("Game Over")
```
