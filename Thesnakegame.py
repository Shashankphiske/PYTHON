# building the snake game

# a turtles body will have a size of 20px wide and 20px height while being a square

import turtle
import random
import time

apple = turtle.Turtle(shape = 'square')
apple.color('red')
apple.penup()

t = random.randint(-50,150)
z = random.randint(-50,150)

apple.goto(t,z)
screen = turtle.Screen()
screen.bgcolor('black')
screen.setup(width=600,height=600)

turtles = []
screen.tracer(0)
apple.goto(x=100,y=0)
distance = [(0,0),(-20,0),(-40,0)]
for i in distance:
    
    bob = turtle.Turtle(shape = 'square')
    turtles.append(bob)
    bob.color('white')
    bob.penup()
    bob.goto(i)


def left():
    turtles[0].left(90)        
def right():
    turtles[0].right(90)

screen.listen()

screen.onkey(key = 'a',fun = left)
screen.onkey(key = 'd',fun = right)

lent = len(turtles)
run = True
run1 = True
while run:
    screen.update()
            
    if turtles[0].xcor() > apple.xcor()-20 and turtles[0].xcor() < apple.xcor()+20 and turtles[0].ycor() > apple.ycor()-20 and turtles[0].ycor() < apple.ycor()+20:
        bob = turtle.Turtle(shape = 'square')
        turtles.append(bob)
        bob.color('white')
        bob.penup()
        bob.goto(turtles[lent-1].xcor()-20,turtles[lent-1])
        t = random.randint(-150,150)
        z = random.randint(-150,150)
        apple.goto(t,z)

    if turtles[0].xcor() > 270 or turtles[0].xcor() < -270 or turtles[0].ycor() > 270 or turtles[0].ycor() < -270:
        run = False
        break

    time.sleep(0.07)
    for i in range(len(turtles)-1,0,-1):
        x = turtles[i-1].xcor()
        y = turtles[i-1].ycor()
        turtles[i].goto(x,y)

    turtles[0].forward(20)
    
screen.exitonclick()
