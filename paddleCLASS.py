from turtle import Turtle

class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.shape('square')
        self.penup()
        self.shapesize(stretch_len = 0.8,stretch_wid = 5)

    def UP(self):
        y = self.ycor() + 20
        self.goto(self.xcor(),y)
    def DOWN(self):
        y = self.ycor() - 20
        self.goto(self.xcor(),y)  