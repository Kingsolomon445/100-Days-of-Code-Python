# A calculator program

from art import logo
from os import system

operations = ["+", "-", "/", "*"]


def operation(operator, nb1, nb2):
    if operator == "+":
        return nb1 + nb2
    elif operator == "-":
        return nb1 - nb2
    elif operator == "/":
        return nb1 / nb2
    elif operator == "*":
        return nb1 * nb2


restart = 1
print(logo)
operand1 = float(input("What is the first operand? "))
while restart:
    for i in operations:
        print(i)
    symbol = input("Pick and type an operator from above: ")
    operand2 = float(input("What is the second operand? "))
    result = operation(symbol, operand1, operand2)
    print(f"The result of {operand1} {symbol} {operand2} = {result}")
    response = input(f"Type 'yes' to continue calculating with {result}, 'no' to start a new calculation: ").lower()
    if response == "yes":
        system('clear')
        print(logo)
        operand1 = result
    elif response == "no":
        system('clear')
        print(logo)
        operand1 = float(input("What is the first operand? "))
    else:
        print("Goodbye!")
        restart = 0