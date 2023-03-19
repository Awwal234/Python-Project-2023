# creating a guessing game with numbers
import random


def guess_function():
    user_guess = int(input('Enter a number: '))
    computed_guess = random.randint(1, 100)

    # loop
    while True:
        if (user_guess == computed_guess):
            print('Hey!, Good work.')
            break
        elif (user_guess < computed_guess):
            print('Your predicted number is low')
            guess_function()
        else:
            print('Your predicted number is too high!')
            guess_function()


guess_function()
