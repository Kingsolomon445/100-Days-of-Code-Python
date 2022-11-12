# A higher lower game, compares two entities, and you decide which has more followers on instagram

from art import logo, vs
from game_data import data
from random import choice
from os import system


def compare(choice_1, choice_2):
    global score

    print(f"Compare A: {choice_1['name']}, a {choice_1['description']}, from {choice_1['country']}.")
    print(vs)
    print(f"Against B: {choice_2['name']}, a {choice_2['description']}, from {choice_2['country']}.")
    user_choice = input("Who has more followers? Type 'A' or 'B': ").upper()
    system('clear')
    print(logo)
    if user_choice == 'A':
        if choice_1['follower_count'] > choice_2['follower_count']:
            score += 1
            print(f"You are right! current score: {score}")
            return True
    elif user_choice == 'B':
        if choice_2['follower_count'] > choice_1['follower_count']:
            score += 1
            print(f"You are right! current score: {score}")
            return True
    else:
        print("Invalid Choice")
        return False
    print(f"Sorry, that is wrong! Final score: {score}")
    return False


game_is_on = 1
score = 0
print(logo)
choice1 = choice(data)
while game_is_on:
    choice2 = choice(data)
    while choice1 == choice2:
        choice2 = choice(data)
    if not compare(choice1, choice2):
        game_is_on = 0
    choice1 = choice2
