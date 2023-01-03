import turtle
import time
from paddleCLASS import Paddle
from ballCLASS import Ball
screen = turtle.Screen()
screen.bgcolor('black')
screen.setup(width = 800,height = 600) 

screen.listen()

screen.tracer(0)

r_paddle = Paddle()
r_paddle.goto(350,0)
l_paddle = Paddle()
l_paddle.goto(-350,0)   

ball = Ball()

screen.onkey(key = "w",fun = l_paddle.UP)
screen.onkey(key = "s",fun = l_paddle.DOWN)
screen.onkey(key = 'o',fun=r_paddle.UP)
screen.onkey(key='l',fun=r_paddle.DOWN)

gameon = True

while gameon:
    screen.update()
screen.exitonclick()