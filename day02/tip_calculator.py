# If the bill was $150.00, split between 5 people, with 12% tip.
# Each person should pay (150.00 / 5) * 1.12 = 33.6
# Format the result to 2 decimal places = 33.60

print("Welcome to the tip calculator!")
total_bill = int(input("What was teh total bill? $"))
tip_percentage = int(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bills? "))

pay_per_person = round((total_bill + (tip_percentage / 100 * total_bill)) / people, 2)
print(f"Each person should pay: ${pay_per_person}")
