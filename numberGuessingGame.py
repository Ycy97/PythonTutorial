#Number Guessing Game, computer gen rand number btwn 1-10, takes in user input to guess the number

from random import randrange
import random

def randNumber():
   return random.randrange(1,11)
#end of function randNumber

while True:
    guessNumber = int(input("Enter number ranging from 1 to 10 : "))
    sNumber = randNumber()
    #print("Secret Number : " + str(sNumber))
    
    if (guessNumber == sNumber):
        print("Congratulations you got the right number")
        break
    else:
        print("Try again!")