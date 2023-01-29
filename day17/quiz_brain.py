class QuizBrain:

    def __init__(self, q_list):
        self.pos = 0
        self.q_list = q_list
        self.user_score = 0
        self.q_number = 1

    def next(self):
        self.pos += 1
        self.q_number += 1

    def process(self):
        answer = input(f"Q.{self.q_number}: {self.q_list[self.pos].text} (True/False) ")
        if answer == self.q_list[self.pos].answer:
            print("You got it right!")
            self.user_score += 1
        else:
            print("That is wrong.")
        print(f"The correct answer was: {self.q_list[self.pos].answer}")
        print(f"Your current score is: {self.user_score}/{self.q_number}\n")
