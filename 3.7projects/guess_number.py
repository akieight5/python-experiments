'''
Created on 20 Dec 2020

@author: aki
'''

import random as rm

def guess(x):
    random_number = rm.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and {x}: "))
        if guess < random_number:
            print("Sorry, guess again.  Too low.")
        elif guess > random_number:
            print("Sorry guesss again.  Too high.")
    
guess(10)