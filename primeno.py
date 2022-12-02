import math
from unittest import skip

def function(num):
    value = True
    for i in range (2,num):
        if num % i == 0:
            value = False
            break
    if value == False:
        print("not prime")
    else:
        print("prime")    
                  
n = int(input("what is ur number :"))
function(num = n)               
