# A program that selects a random name from a list of names to pay everyone's food bill.

from random import randint, seed

names = input("Give me everybody's names, separated by a comma. ").split(",")
seed(10)
index = randint(0, len(names) - 1)
print(f"{names[index]} is going to buy the meal today!")
