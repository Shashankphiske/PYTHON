import turtle
import time
from paddleCLASS import Paddle
from ballCLASS import Ball
import time
from pongscore import score

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

score = score()
score.scoreboard()

screen.onkey(key = "w",fun = l_paddle.UP)
screen.onkey(key = "s",fun = l_paddle.DOWN)
screen.onkey(key = 'o',fun=r_paddle.UP)
screen.onkey(key='l',fun=r_paddle.DOWN)

gameon = True

while gameon:
    time.sleep(0.05)
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.collison()
    if ball.distance(r_paddle) < 50 and ball.xcor() > 330 or ball.distance(l_paddle) < 50 and ball.xcor() < -330: 
        ball.collisionx() 
        ball.speed()
    if ball.xcor() > 380:
        ball.reset() 
        score.r_reset()
    if ball.xcor() < -380:
        ball.reset() 
        score.l_reset()      
    screen.update()
    ball.move()
screen.exitonclick()