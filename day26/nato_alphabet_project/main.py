# This program prints out the list of phonetic words matching each alphabet in a word taken as input

# TODO 1. Create a dictionary in this format: {"A":"Alpha", "B":"Bravo"}
# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
import pandas as pd

df = pd.read_csv('nato_phonetic_alphabet.csv')
print(df)
nato_alpha = {row.letter: row.code for index, row in df.iterrows()}
print(nato_alpha)

user_input = input("Enter a word: ").upper()

phonetic_list = [nato_alpha[letter] for letter in user_input]
print(phonetic_list)
