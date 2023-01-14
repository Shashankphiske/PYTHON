from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("score.txt") as file:
            self.high_score = int(file.read())
        self.penup()
        self.color('white')
        self.goto(0,270)
        self.hideturtle()
        self.write(f"The Score is : {self.score} HighScore is {self.high_score}",align='center',font = ("Ariel",20,"normal"))
    def reset_score(self):
        self.clear()
        self.score += 1
        self.write(f"The Score is : {self.score} HighScore is {self.high_score}",align='center',font = ("Ariel",20,"normal"))
    def over(self):
        self.clear()
        self.goto(0,0)
        self.write("Game Over",align='center',font = ("Ariel",20,"normal"))
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("score.txt" , mode = 'w') as file:
                file.write(f"{self.high_score}")
        self.score = 0
        self.clear()
        self.write(f"The Score is : {self.score} HighScore is : {self.high_score}",align='center',font = ("Ariel",20,"normal"))   
