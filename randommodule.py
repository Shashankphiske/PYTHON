import random 

x = random.randint(1,6)# we can pick a random number between 1 and 6 with this
y = random.random()# this will give a random floating number between 0 and 1
list = ['rock','paper','scissor']
z = random.choice(list)
print(z)
print(y)
print(x)

cards = [1,2,3,4,5,6,7,8,9]
random.shuffle(cards)
print(cards) # this will shuffle those values