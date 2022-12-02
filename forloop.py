# for loop = a for loop is a statement that will excecute its block of code a limited number of times
# while loop = unlimited
# for loop = limited
import time # we will use this far later
for i in range(10):
    print(i+1)

for i in range(10,20):#remember the last number is always exclusive means open
    print(i)

for i in range(0,21,2):#we created a table of 2
    print(i) 
# we can use for loop to iterate anything that is iterable

for i in "shashank phiske" :
    print(i)   
#lets build a timer which will countdown till 0 from 10 and say happy new year

for seconds in range(10,0,-1):
    print(seconds)
    time.sleep(1)#this will create a pause of 1 sec in each loop
print("happy new year")    



