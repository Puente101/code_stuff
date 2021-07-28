from math import *
import sympy as sp
import random
# Random Number 1-100 Computer Guessing Game
number = int(input("Pick A Number 1-100: "))
list_one_through_100 = []
for i in range(100):
    i = i + 1
    list_one_through_100.append(i)
guess = int(random.randint(0, 100))
print(guess)
if guess == list_one_through_100:
    print("Computer Wins!")
tries = 1
while guess != number:
    if guess < number:
        guess = random.randint(guess, 100)
        tries += 1
        print(guess)
    if guess > number:
        guess = random.randint(0, guess)
        tries += 1
        print(guess)
    if guess == number:
        print("Computer Wins After " + str(tries) + " Attempts!\n"
        "The Number is: " + str(guess))    
# blah blah check check
