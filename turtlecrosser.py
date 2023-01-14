from turtle import Turtle

class crosser(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.shape('turtle')
        self.penup()
        self.left(90)
        self.goto(0,-280)

    def move(self):
        self.forward(10)

    def crosser_reset(self):
        self.goto(0,-280)