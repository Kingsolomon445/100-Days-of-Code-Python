from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class UserInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score = 0
        self.score_label = Label(text=f"Score: {self.score}", bg=THEME_COLOR, fg="white", font=("Arial", 15, "bold"))
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(height=250, width=300, bg="white")
        q_text = self.quiz.next_question()
        self.question_text = self.canvas.create_text(150, 150, width=280, text=q_text, font=("Arial", 20, "italic"),
                                                     fill=THEME_COLOR)
        self.canvas.grid(row=1, column=0, columnspan=2, rowspan=2, pady=50)

        right_img = PhotoImage(file="images/true.png")
        self.right_button = Button(image=right_img, highlightthickness=0, bd=0,
                                   command=lambda: [self.feedback_and_update_score("True")])
        self.right_button.grid(row=3, column=0)

        wrong_img = PhotoImage(file="images/false.png")
        self.wrong_button = Button(image=wrong_img, highlightthickness=0,
                                   bd=0, command=lambda: [self.feedback_and_update_score("False")])
        self.wrong_button.grid(row=3, column=1)

        self.window.mainloop()

    def display_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            next_que = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=next_que)
        else:
            self.canvas.itemconfig(self.question_text, text="You've ended the Quiz!")
            self.right_button.config(state="disabled")
            self.wrong_button.config(state="disabled")

    def feedback_and_update_score(self, args):
        answer = self.quiz.get_answer()
        if answer == args:
            self.score += 1
            self.score_label.config(text=f"Score: {self.score}")
            self.canvas.config(bg="green")
        elif answer != args:
            self.canvas.config(bg="red")
        self.window.after(1000, self.display_next_question)



