pos = [(0,0),(-20,0),(-40,0)]
from turtle import Turtle
speed = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.turtles = []
        self.create_snake()
        self.head = self.turtles[0]
    def create_snake(self):
        for i in pos:
            bob = Turtle('square')
            bob.color('white')
            bob.penup()
            bob.goto(i)
            self.turtles.append(bob)

    def movement(self):
        for i in range(len(self.turtles)-1,0,-1):
            x = self.turtles[i-1].xcor()
            y = self.turtles[i-1].ycor()
            self.turtles[i].goto(x,y)
        self.turtles[0].forward(speed)              

    def up(self):
        if self.head.heading() == DOWN:
            pass
        else:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading() == UP:
            pass
        else:
            self.head.setheading(DOWN)
    def left(self):
        if self.head.heading() == RIGHT:
            pass
        else:
            self.head.setheading(LEFT)
    def right(self):
        if self.head.heading() == LEFT:
            pass
        else:
            self.head.setheading(RIGHT)    
    def snake_reset(self):
        bob = Turtle('square')
        bob.color('white')
        bob.penup()
        bob.goto(self.turtles[len(self.turtles)-1].xcor()-20,self.turtles[len(self.turtles)-1])
        self.turtles.append(bob)        

    