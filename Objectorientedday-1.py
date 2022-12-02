# Class acts like a blueprint where we  draw or construct the ideas of a object and then the class is used to
# create an object which has attributes which meaning certain boundries/features/resources to work with etc
# data that it would keep track of

#we will use the turtle module which is a class built in python
#read an gethold of turtle graphics documentation from python.org

from turtle import Turtle ,Screen
timmy = Turtle()#here we created an object from the class Turtle
print(timmy)
timmy.shape("turtle")
timmy.color("red")

myscreen = Screen()
print(myscreen.canvheight)#here myscreen is an object an canvheight(meaning canvas height ) is an attribute
#we can see 300 in terminal which means height and width of 300

myscreen.exitonclick()