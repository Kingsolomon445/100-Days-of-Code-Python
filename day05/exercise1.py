# A simple program to calculate average height from a list of heights

heights = input("Input a list of student heights ").split()
total = 0
length = 0

for height in heights:
    total += int(height)
    length += 1

print(round(total / length))
