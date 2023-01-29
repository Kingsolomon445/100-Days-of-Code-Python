from turtle import Turtle

x1, y1 = 0, 0


class Snake(Turtle):

    def __init__(self):
        super().__init__()
        self.snake_body = []
        self.x, self.y = 0, 0
        self.create()

    def create(self):
        """This  creates the starting snake bodyparts"""
        for i in range(3):
            self.add_body()

    def add_body(self):
        """This adds to the snake_body"""
        segment = Turtle()
        segment.speed(0)
        segment.shape("square")
        segment.color("white")
        segment.penup()
        segment.goto(self.x, self.y)
        self.snake_body.append(segment)
        self.x -= 20

    def restart(self):
        """This restarts the game after collission with wall or tail"""
        self.snake_body = [body.goto(1200, 1200) for body in self.snake_body]  # removes old snake from screen
        self.snake_body.clear()
        self.create()

    def move(self):
        """This basically makes preceding snake body-part replace positions of their front counterpart."""
        global x1, y1
        for body in self.snake_body:
            if self.snake_body.index(body) == 0:
                x1, y1 = body.pos()
                body.forward(20)
            else:
                x2, y2 = body.pos()
                body.goto(x1, y1)
                x1, y1 = x2, y2

    # These are for movement controls
    def up(self):
        if self.snake_body[0].heading() != 270:
            self.snake_body[0].setheading(90)

    def down(self):
        if self.snake_body[0].heading() != 90:
            self.snake_body[0].setheading(270)

    def left(self, **kwargs):
        if self.snake_body[0].heading() != 0:
            self.snake_body[0].setheading(180)

    def right(self, **kwargs):
        if self.snake_body[0].heading() != 180:
            self.snake_body[0].setheading(0)
