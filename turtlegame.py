import turtle
import random

colors = ["red","green","blue","yellow"]
turtles = []
screen = turtle.Screen()

screen.setup(width = 500,height = 400)
bet = screen.textinput(title = "Make your bet",prompt="Which turtle do you think will win (red/green/blue/yellow) :")
y = -150
x = -240

for i in range(0,4):
    bob = turtle.Turtle(shape = 'turtle')
    bob.penup()
    bob.color(colors[i])
    bob.goto(x = x,y = y)
    y += 100
    turtles.append(bob)
if bet:
    bets = True
while bets:

    for bob in turtles:
        distance = random.randint(0,6)
        bob.forward(distance)
        if bob.xcor() > 230:
            bets = "winner"
            colour = bob.pencolor()
            if colour == bet:
                print("You won")
                print("The winning color is",colour)
                
            else:
                print("You lost")
                print("The winning color is",colour) 
    if bets == "winner":
        bets = False       


screen.exitonclick()