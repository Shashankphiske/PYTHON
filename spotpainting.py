color_list = [(202, 164, 109), (238, 240, 245), (150, 75, 49), (223, 201, 135)
            , (52, 93, 124), (172, 154, 40), (140, 30, 19), (133, 163, 185), (198, 91, 71)
            , (46, 122, 86), (72, 43, 35), (145, 178, 148), (13, 99, 71), (233, 175, 164),
              (161, 142, 158), (105, 74, 77), (55, 46, 50), (183, 205, 171), (36, 60, 74), 
              (18, 86, 90), (81, 148, 129), (148, 17, 20), (14, 70, 64), (30, 68, 100), 
              (107, 127, 153), (174, 94, 97), (176, 192, 209)]
from turtle import Screen
import turtle
import random
turtle.colormode(255)
bob = turtle.Turtle()
bob.hideturtle()
bob.speed('fastest')
i = 0
j = 0
while j < 5:
  while i < 10:
    bob.dot(15,random.choice(color_list))
    if i <9:
      bob.penup()
      bob.forward(30)
      bob.pendown()
    i+=1
  bob.left(90)
  bob.penup()
  bob.forward(30)
  bob.pendown()
  bob.left(90)
  
  i = 0  
  while i < 10:
    bob.dot(15,random.choice(color_list))
    if i < 9:
      bob.penup()
      bob.forward(30)
      bob.pendown()
    i+=1
  bob.right(90)
  bob.penup()
  bob.forward(30)
  bob.pendown()
  bob.right(90)
  i = 0
  j+=1
  