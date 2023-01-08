from turtle import Turtle

class score(Turtle):
    def __init__(self):
        super().__init__()
        self.crosser_score = 0
        self.color('white')
        self.hideturtle()
        self.penup()
        self.goto(-260,260)
        self.writer()

    def writer(self):    
        self.write(self.crosser_score,align = "center",font = ("Ariel",24,"normal"))

    def update_score(self):
        self.crosser_score += 1
        self.clear()
        self.writer()

    def game_over(self):
        self.clear()
        self.goto(0,0)
        self.crosser_score = 'GAME OVER'
        self.writer()        