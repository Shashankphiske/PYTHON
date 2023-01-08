import turtle
import time
import random
from turtlecrosser import crosser
from crosser_score import score

colors = ['red','blue','yellow','green','pink','white','purple','brown','orange']
crosser_list1 = []
crosser_list2 = []
crosser_list3 = []
crosser_list4 = []
crosser_list5 = []
crosser_list6 = []
crosser_list7 = []
crosser_list8 = []
crosser_list9 = []
crosser_list10 = []
crosser_list11 = []
crosser_list12 = []
crosser_list13 = []
main_list = []

screen = turtle.Screen()
screen.bgcolor('black')
screen.setup(width = 600,height = 600)
screen.listen()
screen.tracer(0)

crosser_turtle = crosser()

crosser_score = score()

screen.onkey(fun = crosser_turtle.move,key = 'w')


gameon = True
while gameon:

    time.sleep(0.1)
    screen.update()
    for i in main_list:
        z = random.randint(-10,-3)
        i.forward(z)
    if crosser_turtle.ycor() >= 290:
        crosser_turtle.crosser_reset()
        crosser_score.update_score()

screen.exitonclick()