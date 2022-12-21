import turtle
from snakeclass import Snake
import time
from foodclass import apple

screen = turtle.Screen()
screen.setup(600,600)
screen.bgcolor('black')
screen.tracer(0)

snake = Snake() # once this line is triggered we will be calling our create snake method directly to create 3 headed snake

apple = apple()

screen.listen()
screen.onkey(snake.up,'w')
screen.onkey(snake.down,'s')
screen.onkey(snake.left,'a')
screen.onkey(snake.right,'d')

gameon = True
while gameon:
    screen.update()
    time.sleep(0.07)
# we will check the collision with apple using the distance method inside turtle
    if snake.segments[0].distance(apple) < 14 :
        apple.refresh()
        snake.snake_refresh()

    if snake.snake_head.xcor() > 280 or snake.snake_head.xcor() < -280 or snake.snake_head.ycor() > 280 or snake.snake_head.ycor() < -280:
        gameon = False

    snake.move()
    for i in range(0,len(snake.segments)):
        if snake.snake_head.distance(snake.segments[i]) < 10:
            gameon = False
screen.exitonclick()