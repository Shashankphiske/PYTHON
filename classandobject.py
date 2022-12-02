import turtle

class Polygon:# we created a class in which we will pass in 2 arguments namely: sides and name
        def __init__ (self,sides,name):
            self.sides = sides
            self.name = name
        def draw(self): # here we defined a method and when defining a method we dont need to specify any arguments
            turtle.color("red","black")
            turtle.begin_fill()
            turtle.speed(3)
            for i in range(self.sides):
                turtle.forward(150)
                if self.sides == 4:
                    turtle.left(90)
                else:
                    turtle.left(72)        
            turtle.end_fill()
                 

Square = Polygon(4,"Square") # to make an object of our choice from this class we need to specify our arguments
                             # here sides and name
Pentagon = Polygon(5,"Polygon")

print(Square.sides) # here as we needed to access the number of sides that we specified to our object
                    # we needed to access the parameter of that class here sides
                    
Pentagon.draw()                    

# the concept of inheritence and subclassing

class Square(Polygon):
    def __init__(self):
         super().__init__(4,"Square")
    def draw(self):
        turtle.color("white","cyan")
        turtle.begin_fill()
        for i in range(4):

            turtle.forward(100)
            turtle.left(90)
        turtle.end_fill()
       
supp = Square()
supp.draw()
turtle.done
# sub class has another feature called method overriding
