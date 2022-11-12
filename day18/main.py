# A simple program that extracts colors from an image and then make a spot drawing with the colors

import colorgram
import turtle as t
from turtle import Turtle, Screen
import random

# Extracts color from image and save it in list in rgb mode.
colors = colorgram.extract("hirst.png", 33)
rgb_list = [(color.rgb.r, color.rgb.g, color.rgb.b) for color in colors]

screen = Screen()
screen.screensize(600, 600)
t.colormode(255)
turtle = Turtle()
turtle.penup()
turtle.hideturtle()
turtle.speed(10)
turtle.goto(-200, 200)

# Recreate a hirst spot painting
for i in range(10):
    for j in range(10):
        turtle.dot(20, random.choice(rgb_list[2:]))  # Using slicing to remove the extracted bg colors from list.
        if j == 9:
            continue
        turtle.forward(50)
    if turtle.heading() == 0:
        turtle.right(90)
        turtle.forward(50)
        turtle.right(90)
    else:
        turtle.left(90)
        turtle.forward(50)
        turtle.left(90)

screen.exitonclick()
