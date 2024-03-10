import math
l = int(input("Enter the length :"))
b = int(input("Enter the breadth :"))

def answer():
    print("The number of cans required are :",math.ceil((l*b)/5))
    
answer()