# A simple rock, paper and scissors game

from random import choice

choices = ['''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

Rock
''',

           '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)

Paper
''',

           '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

Scissors
'''
           ]

computer_choice = choice([0, 1, 2])
is_user_win = 0
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if user_choice - computer_choice == 1 or computer_choice - user_choice == 2:
    is_user_win = 1

print(choices[user_choice])
print("Computer choose:\n")
print(choices[computer_choice])
if computer_choice == user_choice:
    print("Draw!")
elif is_user_win:
    print("You win!")
else:
    print("You lose!")
