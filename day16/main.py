# A Coffee Maker program

from coffee_maker import CoffeeMaker
from menu import Menu
from money_machine import MoneyMachine

menu = Menu()
coffeemaker = CoffeeMaker()
money_machine = MoneyMachine()

while True:
    order = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if order == "off":  # To shut off machine.
        print("Coffee machine shutting off.....")
        break
    elif order == "report":     # A secret input for employees to check how much money has been made.
        coffeemaker.report()
        money_machine.report()
        continue
    elif order not in ("latte", "cappuccino", "espresso"):
        print("invalid choice!")
        continue
    order_items = menu.find_drink(order)
    if coffeemaker.is_resource_sufficient(order_items):
        if money_machine.make_payment(order_items.cost):
            coffeemaker.make_coffee(order_items)
