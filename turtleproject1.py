from turtle import Turtle,Screen
import random
colours = ["medium slate blue","hot pink","deep pink","red","coral","medium violet red","blue violet","green","yellow","steel blue","dark turquoise","dark blue","slate gray","sienna"]

sides = 3
angle = 360
bob = Turtle()
while sides < 11:
    bob.color(random.choice(colours))
    for i in range(0,sides):
        bob.forward(100)
        bob.left(angle/sides) 
    sides += 1