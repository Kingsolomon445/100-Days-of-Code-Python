# A blackjack game

# Create a two list to store dealer and user cards
# Create a function that checks if card points is not over 21
# Create a function that checks if there is a blackjack win
# Create a function that checks for winner
# Use two while loops, one for the ongoing game and the outer to replay if player wants

from art import logo
from random import choice
from os import system

# The ace counts as 1
# The Jack, Queen and King all counts as 10
cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def check_if_bust(hands):
    if sum(hands) > 21:
        return True
    return False


def check_blackjack_wins(hands):
    if sum(hands) == 21:
        return True


def check_winner(dealer_hands, player_hands):
    if sum(player_hands) == sum(dealer_hands):
        return "draw"
    elif sum(player_hands) > sum(dealer_hands):
        return "win"
    else:
        return "lose"


restart = 1
choices = [0, 1]
while restart:
    print(logo)
    dealer_cards = [choice(cards) for i in range(2)]
    player_cards = [choice(cards) for i in range(2)]
    game_is_on = 1
    if check_if_bust(dealer_cards) or check_if_bust(player_cards) or check_blackjack_wins(dealer_cards) or \
            check_blackjack_wins(player_cards):
        continue
    print(f"Your cards are {player_cards}, current score is: {sum(player_cards)}")
    while game_is_on:
        print(f"Dealer first card is: {dealer_cards[0]}")
        player_choice = int(input("Type 0 if you want to stand, 1 to hit : "))
        if player_choice:
            player_cards.append(choice(cards))
            print(f"Your cards are {player_cards}, current score is: {sum(player_cards)}")
            if check_if_bust(player_cards):
                print("It is a bust for player. Dealer wins!")
                break
            elif check_blackjack_wins(player_cards):
                print("It is a blackjack! You win!")
                break
        dealer_choice = choice(choices)
        if dealer_choice:
            dealer_cards.append(choice(cards))
            if check_if_bust(dealer_cards):
                print(f"Dealer cards are {dealer_cards}, Score is: {sum(dealer_cards)}")
                print("It is a bust for dealer. You win!")
                break
            elif check_blackjack_wins(dealer_cards):
                print("It is a blackjack! Dealer wins!")
                break
        if not player_choice:
            print(f"Dealer cards are {dealer_cards}, Score is: {sum(dealer_cards)}")
            if check_winner(dealer_cards, player_cards) == "win":
                print("You win!")
            elif check_winner(dealer_cards, player_cards) == "lose":
                print("Dealer wins!")
            else:
                print("It is a draw!")
            break
    if input("Do you want to replay? Type 'yes' else 'no': ") == "no":
        restart = 0
    system('clear')
