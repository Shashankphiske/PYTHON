import turtle
import random
colors = ['red','blue','yellow','green','purple','orange','pink','brown']

class car_manager():
    def __init__(self):
        self.cars = []
        self.speed = -5

    def create_cars(self):
        self.random_num = random.randint(1,6)
        if self.random_num == 1:
            car = turtle.Turtle('square')    
            car.shapesize(stretch_len = 2,stretch_wid = 1)
            car.penup()
            car.color(random.choice(colors))
            y = random.randint(-250,250)
            car.goto(300,y)
            self.cars.append(car)

    def move_car(self):
        for i in self.cars:
            i.forward(self.speed) 

    def level_up(self):
        self.speed -= 5       

            