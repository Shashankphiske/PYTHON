# Event listeners are functions/methods in turtle which when used wait for the user to click or type etc
# Basically wait for his command

from turtle import Turtle,Screen

bob = Turtle()
screen = Screen()

def move():
    bob.forward(10)

screen.listen()
screen.onkey(key = 'space',fun = move)# when space bar is pressed trigger the function move forward
                                      # when we pass in function as an argument then we dont need to add the parenthesis
                                      # when we add parenthesis to function it will trigger the function to happen there 
                                      # and there
                                      
# The function can be used as an input for various other functions and tasks
# The concept being used here is higher order function
# For eg: onkey() function/method takes in move() function to operate ,here onkey() is called a higher order function
# use keyword arguments instead of positional arguments in these methods or functions to pass in another function
# especially if you havent created them
screen.exitonclick()
