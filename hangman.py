def get_guess():
    for i in range(7):
        print("what is your guess bro?")
        guess = str(input())#get input
        if guess in list("qwertyuiopasdfghjklzxcvbnm"):
                 break
                 return guess
  
get_guess()
