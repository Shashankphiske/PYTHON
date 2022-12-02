import turtle
import random

turtle.colormode(255)
bob = turtle.Turtle()
count = 0
bob.speed('fastest')
def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    color = (r,g,b)
    return color
while True:
    bob.color(random_color())
    bob.circle(100)
    bob.left(5)
