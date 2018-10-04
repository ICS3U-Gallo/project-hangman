# Hangman (Pseudocode)
def display_letters(word, guesses):
  guessed_word = ""
  counter = 1
  if guessed_word == "":
    guessed_word = "_ " * len(word)
  for i in range(len(guesses)):
    if word.count(guesses[i]) > 1:
      index = word.find(guesses[i])
      for j in range(word.count(guesses[i])):
        slice1 = guessed_word[ : index * 2]
        slice2 = guessed_word[index * 2: ]
        replaced = slice2.replace("_", guesses[i], 1)
        guessed_word = slice1 + replaced
        if word.count(guesses[i]) > 1:
          replaced = word.replace(guesses[i], "*", counter)
          index = replaced.find(guesses[i])
        counter += 1
    elif word.count(guesses[i]) == 1:
      index = word.find(guesses[i])
      slice1 = guessed_word[ : index * 2]
      slice2 = guessed_word[index * 2 : ]
      replaced = slice2.replace("_", guesses[i], 1)
      guessed_word = slice1 + replaced
  return guessed_word
