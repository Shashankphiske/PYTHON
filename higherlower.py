from game_data import data
from higherlowerart import logo
from higherlowerart import vs
import random
import os

print(logo)

print('''

Hi welcome to the Higher Lower game''')
print("Your task is to guess who has the highest followers")
print("Try creating a high score!")

choice = input("Do you want to play the game :")
if choice == "yes":
    choice = True
else:
    choice = False

first = 0
second = 1
score = 0
while choice:

    if first != second:
        score = 0
        first = random.choice(data)
    
    print(f'''
Name: {first['name']} ,Description : {first['description']} ,Origin : {first['country']}''')    
    data.remove(first)

    second = random.choice(data)
    data.append(first)

    print(vs)
    print(f'''
Name : {second['name']} ,Description : {second['description']} ,Origin : {second['country']}
''')
    choice1 = input(f'''Is {first['name']} higher or lower than {second['name']} (IF you want to leave type leave) :''' )    
    
    first_count = first['follower_count']
    second_count = second['follower_count']

    if choice1 == "higher":
        if first_count > second_count:
            score +=1
            first = second
            os.system('cls')
        else:
            print("You lost")
            choice = False
    elif choice1 == "lower":
        if first_count < second_count:
            score += 1
            first = second
            os.system('cls')
            
        else:
            print("You lost") 
            choice = False
    elif choice1 == "leave":
        choice = False                           

print(f"Your score is :{score}")


