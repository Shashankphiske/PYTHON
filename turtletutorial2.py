# we can use setheading() with  certain angle and it will turn in that direction globaly
import turtle
import math
count = 35

bob = turtle.Turtle()
bob.color("white","cyan")
bob.getscreen().bgcolor("black")
bob.speed(9)
bob.begin_fill()
while count>=0:
    
    bob.forward(200)
    bob.left(170)
    count-=1
    
bob.end_fill()    
turtle.done()