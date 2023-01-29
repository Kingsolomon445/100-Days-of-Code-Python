# Paint Area Calculator

import math

height = int(input("Height of wall: "))
weight = int(input("Width of wall: "))

area = height * weight
num_of_cans = math.ceil(area / 5)
print(f"You'll need {num_of_cans} cans of paint.")