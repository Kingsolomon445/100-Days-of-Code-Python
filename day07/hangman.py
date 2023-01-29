# A Hangman Game

# Choose a random word from a list fo words
# Take users guess
# Check users guess against all letters from chosen word
# Update display if correct or lose a life if incorrect
# Keep track of lives and displas when game ends

from random import choice
from hangman_art import stages, logo
from hangman_words import word_list

chosen_word = choice(word_list)
print(logo)
print(f"The choose word is {chosen_word}")
display = ["_" for ch in chosen_word]
lives = 6


def check_letter(letter, word):
    return True if letter in word else False


def update_display(letter, display_lst, word):
    for i in range(len(word)):
        if word[i] == letter:
            display_lst[i] = letter


game_is_on = 1
while game_is_on:
    guess = input("Guess a letter: ").lower()
    if guess in display:
        print(f"You've already guessed {guess}")
    elif check_letter(guess, chosen_word):
        update_display(guess, display, chosen_word)
    else:
        lives -= 1
        print(f"You guessed {guess}, that is not in the word, You lose a life!")
        print(stages[lives])
        if lives == 0:
            print("You lose!")
            break
    print(''.join(display))
    if "_" not in display:
        print("You have guessed all letters correctly.You Won!")
        game_is_on = 0
