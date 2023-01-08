from turtle import Turtle

class score(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle() 
        self.l_score = 0
        self.r_score = 0
        
    def scoreboard(self): 
        self.clear()   
        self.goto(-50,200)
        self.write(self.l_score,align = "center" , font = ('Courier',80,'normal'))
        self.goto(50,200)
        self.write(self.r_score,align = "center" , font = ('Courier',80,'normal'))

    def l_reset(self):
        self.l_score += 1   
        self.scoreboard()

    def r_reset(self):
        self.r_score += 1
        self.scoreboard()    
       