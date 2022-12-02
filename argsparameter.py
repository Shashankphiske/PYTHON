# *args = args is parameter that will pack all the arguments into a tuple
#         useful so that a function can accept a varying amounts of arguments

def add(*stuff): # this stuff is unchangeable as it is a tuple , one way we can do that is type casting it
    sum = 0
    stuff = list(stuff)
    stuff[2] = 0 # this means at index 2 value is 0
    for i in stuff:
        sum += i
    return sum

print(add(1,3,4,2,4,)) # here i can add as many arguments i want and i wont face an issue