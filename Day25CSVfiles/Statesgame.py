import turtle
import pandas

count = 0
count2 = 0

screen = turtle.Screen()
screen.title("The State Game")
screen.setup(width = 700,height = 700)

image = "C:\\Users\\shash\\Documents\\PYTHON\\Day25CSVfiles\\blank_states_img.gif"

screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("C:\\Users\\shash\\Documents\\PYTHON\\Day25CSVfiles\\50_states.csv") 
data_state = data.state.to_list()
states = []
data_dict = {}

bob = turtle.Turtle()
bob.hideturtle()
bob.penup()

gameon = True
while gameon:
    answer_state = screen.textinput(title = f"States {count}/{50}",prompt = "Whats's the State name :").title()
    if answer_state == "Break":
        break
    if answer_state in data_state:
        data_state.remove(answer_state)
        coords = data[data["state"] == answer_state]
        count += 1
        bob.goto(int(coords["x"]),int(coords["y"]))
        bob.write(answer_state,align = "center" , font = ("Ariel",10,"normal"))
    else:
        count2 += 1

    if count == 50 or count2 == 5:
        gameon = False    

states_to_learn = pandas.DataFrame(data_state)
states_to_learn.to_csv("states_to_learn.csv")

screen.exitonclick()