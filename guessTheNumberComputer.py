import random

#function to take in max guessing val

def guess(x):
    secret_number = random.randint(1,x)
    guess = -1
    #while loop to loop as long as user's input != secret number
    while guess != secret_number:
        guess = int(input(f'Guess a number between 1 and {x} : '))

        if guess > secret_number:
            print('Number is too big! Try again.')
        elif guess < secret_number:
            print('Number is too small! Try again.')
        else:
            print(f'You got it right! The secret number is {secret_number} which is the same as ur guess {guess}')


guess(10)