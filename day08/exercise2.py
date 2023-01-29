# A program that checks if a number is a prime number

number = int(input("Check this number: "))
is_prime = 1
for nbr in range(2, int(number / 2)):
    if number % nbr == 0:
        is_prime = 0
        break

if is_prime:
    print("It's a prime number.")
else:
    print("It's not a prime number.")
