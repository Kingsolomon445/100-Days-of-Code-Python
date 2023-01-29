# A simple turtle race program

from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(500, 400)
user_player = screen.textinput("Make Your Bet", "Which turtle(Color) is gonna win?")

colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
players = []
x, y = -230, 150
for color in colors:
    turtle = Turtle()
    turtle.shape("turtle")
    turtle.penup()
    turtle.goto(x, y)
    turtle.color(color)
    players.append(turtle)
    y -= 50

game_on = True
while game_on:
    for i in range(len(players)):
        player = players[i]
        player.forward(random.randint(1, 10))
        if player.pos()[0] >= 225:
            winner_pos = i
            game_on = False
turtle = Turtle()
turtle.hideturtle()
if user_player == colors[winner_pos]:
    turtle.write(f"YOU WIN!", align="center", font=('Arial', 15, 'normal'))
else:
    turtle.write(f"YOU LOSE! {colors[winner_pos].upper()} WINS!", align="center", font=('Arial', 15, 'normal'))

screen.exitonclick()
