# A number guessing game

from random import randrange
from art import logo
from os import system


def check_guess(guess_number, correct_number):
    if guess_number < correct_number:
        print("Too low.\nGuess agaain.")
    elif guess_number > correct_number:
        print("Too high.\nGuess again.")
    elif guess_number == correct_number:
        print(f"You got it! The correct answer was {correct_number}")
        return True
    return False


replay = 1
while replay:
    game_is_on = 1
    print(logo)
    print("Welcome to the number guessing game!")
    print("I am thinking of a number between 1 and 100")
    chosen_number = randrange(1, 101)
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if difficulty == "easy":
        tries = 10
    else:
        tries = 5
    while game_is_on:
        print(f"You have {tries} tries left")
        guess = int(input("Make a guess: "))
        tries -= 1
        if check_guess(guess, chosen_number):
            game_is_on = 0
        if tries == 0:
            print("Game over! No tries left!")
            game_is_on = 0
    if input("Do you want to replay? Type 'y' for yes and 'n' for no: ") == "n":
        replay = 0
    system('clear')
