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
    if snake.turtles[0].xcor() > 270 or snake.turtles[0].xcor() < -270 or snake.turtles[0].ycor() > 270 or snake.turtles[0].ycor() < -270:
        gameon = False
        score.over()
    if snake.head.distance(apple) < 15:
        apple.reset_apple()
        snake.snake_reset()
        score.reset_score()
    for i in snake.turtles:
        if i is snake.head:
            pass
        else:
            if snake.head.distance(apple) < 10:
                gameon = False
                apple.over()      
    snake.movement()
screen.exitonclick()