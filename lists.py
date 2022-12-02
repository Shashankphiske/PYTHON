# list = used to store multiple items in a single variable

from subprocess import STARTF_USESHOWWINDOW


food = ["pizza "," burger","chicken"]#each item in this list is referred to an element
print( food )

#we can access the single items by using index of these elements
print(food[1])
#we can change elements at index
food[2] = "sushi"
print(food[2]) 

for x in food:
    print(x)
# few usefull functions of lists
food.append("icecream") #adds an element at the end of the list
food.remove("icecream") # removes an element from a list
food.pop() # it removes the last element
food.insert(2, "momo") # inserts an element at the given index
food.sort() # this will sort the list alphabetically
food.clear()# this removes all the elements from a list





