import random

names = ["shashank","utkarsh","kunal","aditya"]
new_list = {key:random.randint(1,100) for key in names}
print(new_list)

print({k:v for (k,v) in new_list.items() if v > 50})