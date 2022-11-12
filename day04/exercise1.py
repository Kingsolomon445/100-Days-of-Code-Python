# A virtual coin toss program

from random import randint

side = randint(0, 1)
if side:
    print("Heads")
else:
    print("Tails")