# An automatic pizza order program

print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
bill = 0

if extra_cheese == "Y":
    bill += 1
if size == "S":
    bill += 15
    if pepperoni == "Y":
        bill += 2
else:
    if size == "M":
        bill += 20
    elif size == "L":
        bill += 25
    if pepperoni == "Y":
        bill += 3

print(f"Your final bill is: ${bill}.")
