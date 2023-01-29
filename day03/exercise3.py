# A program that determines if a year given is a leap or a common year.

year = int(input("Which year do you want to check? "))

if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    print("Leap year.")
else:
    print("Not leap year.")
