# A Love Calculator

print("Welcome to the Love Calculator!")
name1 = input("What is your name?\n").lower()
name2 = input("What is their name?\n").lower()

count1 = 0
count2 = 0

for letter in name1 + name2:
    if letter in "true":
        count1 += 1
    if letter in "love":
        count2 += 1

love_score = int(str(count1) + str(count2))
if love_score < 10 or love_score > 90:
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif 40 <= love_score <= 50:
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}")
