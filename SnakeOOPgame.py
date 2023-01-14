from turtle import Screen
from snakeclass import Snake
from foodclass import FOOD
from scoreboard import Score
import time

screen = Screen()
screen.bgcolor('black')
screen.setup(width=600,height = 600)
screen.title("The Snake Game")
screen.tracer(0)

snake = Snake()
apple = FOOD()
score = Score()
screen.listen()
screen.onkey(snake.up,'w')
screen.onkey(snake.down,'s')
screen.onkey(snake.left,'a')
screen.onkey(snake.right,'d')

gameon = True
while gameon:
    screen.update()
    time.sleep(0.1)
    if snake.head.distance(apple) < 20:
        apple.reset_apple()
        score.reset_score()
        snake.snake_reset()
    if snake.turtles[0].xcor() > 270 or snake.turtles[0].xcor() < -270:
        x = snake.head.xcor()
        y = snake.head.ycor()
        snake.head.goto(-x,y)
    if snake.turtles[0].ycor() > 270 or snake.turtles[0].ycor() < -270:
        x = snake.head.xcor()
        y = snake.head.ycor()
        snake.head.goto(x,-y)       
        

    for i in range(1,len(snake.turtles)-1):
        if snake.head.distance(snake.turtles[i]) < 10:
            gameon = False
            score.over()
            
       
    snake.movement()
screen.exitonclick()