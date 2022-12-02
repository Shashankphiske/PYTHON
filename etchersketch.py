import turtle

bob = turtle.Turtle()
screen = turtle.Screen()

def forward():
    bob.forward(20)
def back():
    bob.backward(20)
def left():
    bob.left(10)        
def right():
    bob.right(10)
def clear():
    bob.clear()
def reset():
    bob.reset()
def circle():
    bob.circle(-80,extent=10)

screen.listen()
screen.onkey(key='w',fun = forward)
screen.onkey(key = 's',fun = back)
screen.onkey(key = 'a',fun = left)
screen.onkey(key = 'd',fun = right)
screen.onkey(key = 'c',fun = clear and reset)           
screen.onkey(key = 'q',fun = circle)       
screen.exitonclick()
# there are instances in object and class building
# timmy and tommy are two objects from the same class but they are different 
# they are instances of a class
# here if i give tommy green color and timmy red then state of timmy and tommy are different 