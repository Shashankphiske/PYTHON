import turtle
import time
import random
from turtlecrosser import crosser
from crosser_score import score
from crossing_cars import car_manager   


screen = turtle.Screen()
screen.bgcolor('black')
screen.setup(width = 600,height = 600)
screen.listen()
screen.tracer(0)

crosser_turtle = crosser()

crosser_score = score()

crosser_car = car_manager()
screen.onkey(fun = crosser_turtle.move,key = 'w')

gameon = True
while gameon:

    time.sleep(0.1)
    screen.update()

    if crosser_turtle.ycor() >= 290:
        crosser_turtle.crosser_reset()
        crosser_score.update_score()
        crosser_car.level_up()

    crosser_car.create_cars()
    crosser_car.move_car()

    for i in crosser_car.cars:
        if crosser_turtle.distance(i) < 20:
            gameon = False
            crosser_score.game_over()
    for i in crosser_car.cars:
        if i.xcor() > 310:
            crosser_car.cars.remove(i)        
screen.exitonclick()