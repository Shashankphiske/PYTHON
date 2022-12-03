import turtle
import time

positions = [(0,0),(-20,0),(-40,0)]

class Snake:
    def __init__(self):
        self.segments =[]
        self.create_snake()
    def create_snake(self):
        for i in positions:
            bob = turtle.Turtle(shape = 'square')
            self.segments.append(bob)
            bob.color('white')
            bob.penup()
            bob.goto(i)
    def move(self):
        time.sleep(0.07)
        for i in range(len(self.segments)-1,0,-1):
            x = self.segments[i-1].xcor()
            y = self.segments[i-1].ycor()
            self.segments[i].goto(x,y)

        self.segments[0].forward(20)
    

