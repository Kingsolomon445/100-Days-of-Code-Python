# A coffee maker program

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

profit = 0


def is_resources_sufficient(coffee_type):
    is_resources_enough = 1
    for key, value in resources.items():
        if value < MENU[coffee_type]["ingredients"][key]:
            print(f"Sorry there is no enough {key}")
            is_resources_enough = 0
    if not is_resources_enough:
        return False
    return True


def process_payment(coffee_type):
    global profit

    print("Please insert coins")
    quarters = int(input("How many quarters? ")) * 0.25
    dimes = int(input("How many dimes? ")) * 0.10
    nickles = int(input("How many nickles? ")) * 0.05
    pennies = int(input("How many pennies? ")) * 0.01
    money = quarters + dimes + nickles + pennies
    if money > MENU[coffee_type]["cost"]:
        change = round(money - MENU[coffee_type]["cost"], 2)
        print(f"Here is {change} in change.")
    elif money < MENU[coffee_type]["cost"]:
        print("Sorry that is not enough money, ,money refunded.")
        return False
    profit += MENU[coffee_type]["cost"]
    return True


def make_coffee(coffee_type):
    global resources

    for key, value in resources.items():
        resources[key] = value - MENU[coffee_type]["ingredients"][key]
    print(f"Here is your {coffee_type}. Enjoy!")


def report():
    for key, value in resources.items():
        if key == "coffee":
            print(f"{key}: {value}g")
        else:
            print(f"{key}: {value}ml")
    print(f"Money: ${profit}")


while True:
    coffee = input("What would you like? (espresso, latte, cappuccino): ").lower()
    if coffee == "off":
        break
    elif coffee == "report":
        report()
    elif coffee not in ("espresso", "latte", "cappuccino"):
        print("Invalid choice!")
    else:
        if is_resources_sufficient(coffee):
            if process_payment(coffee):
                make_coffee(coffee)
