from turtle import Turtle
import time


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt", "r") as hs:
            self.highscore = int(hs.read())
        self.hideturtle()
        self.color("white")

    def track_score(self):
        """Keep track of score"""
        self.score += 1

    def final_score(self):
        """Updates high score"""
        if self.score > self.highscore:
            self.highscore = self.score
            with open("data.txt", "w") as hs:
                hs.write(str(self.score))
        self.write(f"Score: {self.score}\nHigh Score: {self.highscore}", align="center", font=('Arial', 15, 'normal'))
        time.sleep(2)

    def reset_score(self):
        """Resets score after collision"""
        self.clear()
        self.score = 0

    def game_over(self):
        """After 3 trials end"""
        self.write(f"Game Over!\nHigh Score: {self.highscore}", align="center", font=('Arial', 15, 'normal'))
