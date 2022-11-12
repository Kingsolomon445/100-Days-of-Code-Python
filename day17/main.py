# A simple quiz program

from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = [Question(que["text"], que["answer"]) for que in question_data]

quizbrain = QuizBrain(question_bank)

while True:
    quizbrain.process()
    if quizbrain.q_number == len(question_bank):
        print("Quiz ended")
        print(f"Your final score is {quizbrain.user_score}/{quizbrain.q_number}")
        break
    quizbrain.next()
