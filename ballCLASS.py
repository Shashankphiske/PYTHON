from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.add1 = 10
        self.add2 = 10

    def move(self):
        x = self.xcor() + self.add1
        y = self.ycor() + self.add2
        self.goto(x,y)    

    def collison(self):
        self.add2 *= -1

    def collisionx(self):
        self.add1 *= -1    