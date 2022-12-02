import random
import os
from game1 import logo


choice = input("Do you wanna play the game? :")
if choice == "yes":
    choice = True
else:
    choice = False


while choice:
    global number
    number = random.randint(0,1000)
    print(logo)
    hardness = input("Do you want the game to be easy or hard :")
    if hardness == "easy":
        
        loop = 10
    else:
        loop = 5
        
    def game(chance):
        global loop
        if number > choice_1:
            print("Higher")
           
            loop -= 1
        elif number < choice_1:
            print("Lower")
            
            loop -= 1
        else:
            print("Congratulations")           

    while loop != 0:
        choice_1 = int(input("What is your guess :"))
        game(chance = choice_1)
        if choice_1 == number:
            break

    if choice_1 != number:
        print("You lost!")    
    choice = input("Do you want to play the game again! :")
    if choice == "yes":
        choice = True
        os.system('cls')
    else:
        choice = False          
        break