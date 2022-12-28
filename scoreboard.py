from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color('white')
        self.goto(0,270)
        self.hideturtle()
        self.write(f"The Score is : {self.score}",align='center',font = ("Ariel",20,"normal"))
    def reset_score(self):
        self.clear()
        self.score += 1
        self.write(f"The Score is : {self.score}",align='center',font = ("Ariel",20,"normal"))
    def over(self):
        self.clear()
        self.goto(0,0)
        self.write("Game Over",align='center',font = ("Ariel",20,"normal")) 