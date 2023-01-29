# A blind auction program

from art import logo
from os import system

print(logo)
bid = {}


def check_bid_winner(bidders):
    max_amount = 0
    winner = ""
    for key, value in bidders.items():
        if value > max_amount:
            winner = key
            max_amount = value
    print(f"The winner is {winner} with an amount of ${max_amount}!")


bid_is_on = 1
while bid_is_on:
    name = input("What is your name? ")
    amount = int(input("What's your bid? $"))
    bid[name] = amount
    if input("Are there any other bidders? Type 'yes' or 'no' ").lower() == "no":
        check_bid_winner(bid)
        bid_is_on = 0
    else:
        system('clear')
