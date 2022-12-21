from turtle import Turtle
import random

class apple(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_len = 0.5,stretch_wid = 0.5)
        self.color('red')
        self.speed('fastest')
        self.refresh()    
    def refresh(self):
        t = random.randint(-200,200)
        z = random.randint(-200,200)
        self.goto(t,z)
