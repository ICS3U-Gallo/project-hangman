# Hangman (Pseudocode)

```
1. P1 Chooses a word or series of words
2. Break up word into seperate letters
3. Start loop
4. P2 Chooses letter or word
5. if P1 chooses a letter and the letter is in the word, reveal all spots where it is found
6. elif player chooses a letter and letter is not in the word, add a body part to the hangman
7. elif the player chooses the wrong word, add a body part
8. elif the player chooses the right word and the hangman isn't finished yet, P1 loses, P2 wins, loop ends
9. If the hangman is finished, loop ends and P1 wins, P2 loses
10. Repeat steps 2-7 until game ends
```
