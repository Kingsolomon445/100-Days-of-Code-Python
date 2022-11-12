from turtle import Turtle
import time

FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.level = 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.goto(-280, 265)
        self.clear()
        self.write(f"level: {self.level}", align="left", font=FONT)

    def level_track(self):
        self.level += 1
        self.update_scoreboard()

    def reset_score(self):
        self.goto(0, 0)
        self.write(f"Game Over", align="center", font=FONT)
        time.sleep(1)
        self.clear()
        self.level = 1
        self.update_scoreboard()
