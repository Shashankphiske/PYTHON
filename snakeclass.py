import turtle

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
        

