from turtle import Turtle
import random

class FOOD(Turtle):
    def __init__(self):
        super().__init__()

        self.shape("circle")
        self.color("red")
        self.penup()
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.speed("fastest")
        self.reset_apple()
    def reset_apple(self):
        t = random.randint(-270,270)
        z = random.randint(-270,270)   
        self.goto(t,z)         
