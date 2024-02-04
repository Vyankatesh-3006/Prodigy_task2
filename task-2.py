import random
number=random.randint(1,100)
guesses=0
guess=0
while number != guess:
    guesses += 1
    
    guess= int(input("Guess the number:"))
    
    if guess<number :
        print("The guess is to low")
    elif guess>number :
        print("The guess is to high")
    else :
        print("You won the game")   
        print("you guess the number in" ,guesses ,"guesses")