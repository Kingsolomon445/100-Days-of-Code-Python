# A simple snake game

import time
from turtle import Screen

from food import Food
from scoreboard import ScoreBoard
from snake import Snake

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

trials = 0
while True:  # You have 3 trials per game start
    screen.update()
    time.sleep(0.1)

    snake.move()
    # Detect collision with food
    if snake.snake_body[0].distance(food) <= 18:
        food.go_to()
        scoreboard.track_score()
        snake.add_body()
        snake.move()
    # Detect collision with wall
    if snake.snake_body[0].xcor() > 280 or snake.snake_body[0].xcor() < -280 or snake.snake_body[0].ycor() > 280 or \
            snake.snake_body[0].ycor() < -280:
        scoreboard.final_score()
        scoreboard.reset_score()
        snake.restart()
        trials += 1

    # Detect collision with own tail
    for body in snake.snake_body[2:]:
        if snake.snake_body[0].distance(body) <= 10:
            scoreboard.final_score()
            scoreboard.reset_score()
            snake.restart()
            trials += 1
    if trials == 3:
        scoreboard.game_over()
        break

screen.exitonclick()
