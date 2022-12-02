from turtle import Turtle , Screen
import random
import turtle

direction = [90,180,270,360]
colours = ["medium slate blue","hot pink","deep pink","red","coral","medium violet red","blue violet","green","yellow","steel blue","dark turquoise","dark blue","slate gray","sienna"]
bob = Turtle()
turtle.colormode(255)
bob.width(10)
bob.speed(9)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    random_color = (r,g,b)
    return random_color
while True:
    
    bob.pencolor(random_color())
    bob.forward(25)
    bob.setheading(random.choice(direction))

 


    