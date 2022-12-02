import os
from auctionart import logo
dict = {}
real_value = True

while real_value == True:
    
    print(logo)
    name = input("What is ur name? :")
    bid = int(input("What is ur bid :"))
    dict[name] = bid 
    
    value = input("are there any more bidders :yes or no :").lower
    if value == "yes":
        real_value = True
    else:
        real_value = False 
    os.system("cls")       
print(dict)
high = []
i = 0    
for key in dict:
    if dict[key] >= i:
        i = dict[key]
        high.append(key)
    else:
        continue
for k in high:

    print(f"The Winner is {k} and the bid was {i}$")        


