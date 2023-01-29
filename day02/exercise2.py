# A program that calculates body mass index(BMI)

height = float(input("enter your height: "))
weight = float(input("enter your weight: "))

bmi = weight / (height * height)
print(round(bmi))