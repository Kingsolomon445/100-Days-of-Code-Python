# A simple program that prints out the max score out of a list of scores

scores = input("Input a list of student scores ").split()

max_score = 0
for score in scores:
    if int(score) > max_score:
        max_score = int(score)

print(f"The highest score in the class is: {max_score}")
