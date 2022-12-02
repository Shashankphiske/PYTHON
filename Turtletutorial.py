import turtle

mitthu = turtle.Turtle() # created a mitthu object from class Turtle()
# here the screen created will be 300 in height and 300 in width

# mitthu.forward(100) # the object will move forward by given amount 
# mitthu.left(45) # here the object will turn to the specific direction in the provided angle
# mitthu.forward(100)
# mitthu.right(90)
# mitthu.forward(100)
mitthu.color("red","black") # if you want certain color then type in that shades hex value in " "
#here the first color is the object color and the second is filling color
#making a square
count = 3
mitthu.begin_fill()
while count>=0:
    mitthu.forward(100)
    mitthu.left(90)
    count-=1
mitthu.right(90)    
mitthu.end_fill()
mitthu.penup()# as the name suggests pen will not draw
mitthu.forward(100)
mitthu.pendown()
turtle.done() # keeps the animation window open till the given code is executed