import random
from turtle import clear, clearscreen
from hangman_art import stages
from hangman_art import logo

words = ["hello","andrew","morning","night","python","afternoon","family"]
print(logo)
chosen_word = random.choice(words)
print("hint :" + chosen_word)
length = len(chosen_word)
list = []
symbol = '_'
six = 6
for i in range(length):
    list.append(symbol)
print(list)

while six > 0 and symbol in list:
    given_word = input("what's your guess :").lower()
    if given_word in list:
        print("already exists")    
    
    for position in range(len(chosen_word)):
        word = chosen_word[position]    
        if word == given_word:
            list[position] = given_word 
          
    if given_word not in list:
        six -= 1
        print(stages[six])
    if symbol in list:
        print(list)
    else:
        print("")                
           
if six <= 0:
    print("you lost")
else:            
    print(list) 
    print("you won!") 
                

            
        
                    
     
