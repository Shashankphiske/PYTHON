import random
from blackjackart import logo
import os

gambling = input("Do you want to play Blackjack :")
while  gambling != "no":
    king = 10
    queen = 10
    jack = 10
    ace = 11
    cards = [2,3,4,5,6,7,8,9,10,king,queen,jack,ace]
    player_value = []
    dealer_value = []
    value = 0
    sum = 0   
    print(logo)
    player_value.append(random.choice(cards))
    player_value.append(random.choice(cards))
    dealer_value.append(random.choice(cards))
    dealer_value.append(random.choice(cards))
    
    print(f"The dealers first card value is :{dealer_value[0]}")
    print(f"Your card values are :{player_value}")

    for j in dealer_value:
        sum += j 

    for i in player_value:
        value += i 
        if i == ace:
            if value + 11 <= 21:
                ace = 11
            elif value + 11 > 21:
                ace = 1 
    if value == 21 and  sum < 21:
        print("Player wins")
        continue
    elif value == 21 and sum == 21:
        print("Draw") 
        break
    sum = 0                
    call = input("Do you want a new card :")
      
    while value < 21 and call == "yes":
        player_value.append(random.choice(cards))
        value = 0
        for i in player_value:
            value += i
        if value > 21:
            print("Player lost")
            print(player_value)
            break    
        print(player_value)    
        call = input("Do you want a new card :")
        if call == "no":
            break
    print(f"Dealers cards are :{dealer_value}")
    for j in dealer_value:
        sum += j  

    if value <= 21 and sum <= value:
        while sum <= value :
            dealer_value.append(random.choice(cards))
            sum = 0
            for j in dealer_value:
                sum += j
            if sum > 21:
                print("Dealer lost")   
                print(dealer_value) 
            elif sum > value:
                print(dealer_value)
                print("Dealer wins")          
            elif value == 21 and sum < 21:
                print(player_value)
                print("Player wins ")
            elif sum == 21 and value < 21:
                print(dealer_value)
                print("Dealer wins")
            elif sum == 21 and value == 21:
                print("Draw")
                print(dealer_value)
                break 

    elif sum > 21:
        print("Dealer lost")
    elif sum > value:
        print(dealer_value)
        print("Dealer wins")          
    elif value == 21 and sum < 21:
        print(player_value)
        print("Player wins ")
    elif sum == 21 and value < 21:
        print(dealer_value)
        print("Dealer wins")
    elif sum == 21 and value == 21:
        print("Draw")  
    player_value.clear()
    dealer_value.clear()       
    gambling = input("Do you want to continue playing :")
    os.system("cls")

      



