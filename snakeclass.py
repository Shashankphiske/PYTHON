import turtle
import time
import random

positions = [(0,0),(-20,0),(-40,0)]

class Snake:
    def __init__(self):
        self.segments =[]
        self.create_snake()
        self.snake_head = self.segments[0]
    def create_snake(self):
        for i in positions:
            bob = turtle.Turtle(shape = 'square')
            bob.color('white')
            bob.penup()
            bob.goto(i)
            self.segments.append(bob)
    def move(self):
        time.sleep(0.02)
        for i in range(len(self.segments)-1,0,-1):
            x = self.segments[i-1].xcor()
            y = self.segments[i-1].ycor()
            self.segments[i].goto(x,y)
        self.segments[0].forward(20)
    def right(self):
        self.segments[0].right(90)
    def left(self):
        self.segments[0].left(90)
    def up(self):
        h = self.segments[0].heading()
        if h == 0:
            self.segments[0].left(90)
        elif h == 180:
            self.segments[0].right(90)            
    def down(self):
        h = self.segments[0].heading()  
        if h == 0:
            self.segments[0].right(90)
        elif h == 180:
            self.segments[0].left(90)   
    def snake_refresh(self):
        bob = turtle.Turtle(shape = 'square')
        self.segments.append(bob)
        bob.color('white')
        bob.penup()
        bob.goto(self.segments[len(self.segments)-1].xcor()-20,self.segments[len(self.segments)-1])   
    def collision_wall(self,gameon): 
        if  self.snake_head.xcor() > 270 or self.snake_head.xcor() < -270 or self.snake_head.ycor() > 270 or self.snake_head.ycor() < -270:
            return self.gameon ==  False
                  

