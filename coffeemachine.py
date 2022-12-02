from coffeedata import MENU
from coffeedata import resources
change = 0
choice3 = 0
choice = input("Would you like a coffee? :")
if choice == "yes":
    choice == True
else:
    choice == False
water1 = resources["water"]
milk1 = resources["milk"]
coffee1 = resources["coffee"]
while choice:
    if choice3 == 0:
        water = water1
        milk = milk1
        coffee = coffee1
    else:
        choice == True    
    
            
    print('''
    ⠀⠀⠀⠀⠀⠀⢀⣀⣤⣤⣴⣶⠶⠶⠶⠶⠶⢶⠶⠶⠲⠶⠶⠶⠶⠶⡶⢶⣤⣤⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣤⣾⠟⠋⠉⣀⣀⣤⣴⣶⣶⣶⣿⣿⣿⣿⢿⠿⠿⠿⠷⠶⣭⣭⣍⣛⠫⠝⠻⢷⣦⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⡷⣷⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⠆⠀⠀⠘⠻⢿⣉⣻⣶⣾⢿⠃⠀⣀⡀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⡇⠀⠉⠙⠛⠻⠿⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣶⣶⣶⣶⠿⢿⣛⡛   ⢸⠛⠛⢿⠛⢿⣦⡀
⠀⠀⠀⠀⠀⠀⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠀⢀⡀⠀⢁⣀⣘⣻⣍⡭⣥⣤⠀⠀⡀⣼⠖⠒⠉⠙⡞⡜⣷
⠀⠀⠀⠀⠀⠀⢿⠰⢠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠑⠢⣄⠀⠠⠽⡤⢾⠾⢰⢡⢤⡿⠀⠀⠀⢠⣧⡇⡟
⠀⠀⠀⠀⠀⠀⢸⡖⠈⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢣⠀⠠⢷⠼⠀⡆⡜⣾⡇⠀⠀⢀⡜⢻⣷⠇
⠀⠀⠀⠀⠀⠀⠀⢧⣧⢱⠈⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠈⠀⡜⢰⢡⣿⠁⠀⣠⠞⣠⣿⠋⠀
⠀⠀⠀⠀⠀⠀⢀⣸⣟⡄⢇⢰⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⠀⠀⢀⡼⢡⣷⢻⡧⠔⢋⣥⣾⠟⠁⠀⠀
⠀⠀⣠⣴⠞⣋⣩⠤⠿⣝⡌⣆⢣⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣧⡤⣴⠏⣠⣿⣻⡏⣀⣺⣿⠿⢥⡀⠀⠀⠀
⢠⡞⠁⡴⠛⠉⠀⠀⠀⠙⢮⠈⢢⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⡞⠁⣴⣿⡿⠋⢩⠁⡈⠉⡳⡄⢹⣦⠀⠀
⠸⣦⡆⢷⣀⠀⢠⣄⣀⠀⠀⠓⢄⣁⠀⠀⠀⠀⠀⠀⠀⠀⠠⠴⠿⠿⠟⠓⠀⣴⡿⠟⠁⠠⣞⣡⢃⣤⣷⢏⣼⡿⠀⠀
⠀⠈⠓⠮⣿⣿⣶⣿⣿⣿⣿⣶⣤⣈⣙⠒⠲⠦⠤⠤⠴⠿⠿⠿⠿⠯⠥⠖⢒⣉⣤⣤⣶⠿⠿⠟⢻⣿⠿⠟⠉⠀⠀⠀
⠀⠀⠀⠀⠀⠙⠯⣝⣛⠻⠿⠤⢬⣉⣉⣉⣉⣿⣟⣛⣛⣾⣿⣿⣿⣿⣯⣍⣉⣩⣤⣤⣴⣶⣿⡿⠟⠁⠀⠀⠀⠀⠀⠀''')
    

    print(f"Available resources are :milk :{milk},water :{water},coffee :{coffee}")
    
    print(f"Available change :{change}")
    for i in MENU:
        print(f'''
{i}''')
        cost = MENU[i]["cost"]
        print(f"Cost :{cost}")
        

    choice1 = input("Which one would you like (1/2/3) :")
    
    if choice1 == "1":
        choice1 = "espresso"
    elif choice1 == "2":
        choice1 = "latte"
    elif choice1 == "3":
        choice1 = "cappuccino"   
    else:
        print("Invlid choice")
        break         
    choice3 = int(input("Insert the money :"))
    if choice3 > MENU[choice1]["cost"]:
        cash = choice3 - MENU[choice1]["cost"]
        if cash > change:
            choice4 = input("insuficient change ,but would you like to continue (yes/no ):")
            if choice4 == "yes":
                choice5 = True
                change += choice3
            else:
                choice5 = False 
                choice = False 
        else:
            choice5 = True
            change -= cash
            print(f"The change is :{cash}")
    elif choice3 == MENU[choice1]["cost"]:
        choice5 = True
        change += choice3
    else:
        print(("insufficient funds"))
        choice5 = False
        choice = False
    if choice5:
        if water - MENU[choice1]["ingredients"]["water"] < 0 or coffee - MENU[choice1]["ingredients"]["coffee"] < 0 or milk - MENU[choice1]["ingredients"]["milk"] < 0:
            print("Sorry,Not enough resources")
            print("Money refunded")
            choice = False
            
        else:
            water -= MENU[choice1]["ingredients"]["water"]
            coffee -= MENU[choice1]["ingredients"]["coffee"] 
            milk -= MENU[choice1]["ingredients"]["milk"]
            choice = input('''
Your coffee is ready ,
do you want another one :''')
            if choice == "yes":
                choice = True
            else:
                choice = False
                        
  
    