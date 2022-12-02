#nested function calls = these are function calls inside other function calls
#                        innermost function calls are resolved first 
#                        returned value is used as an argument for the next outer function

num = input("enter a positive integer :")
num = float(num)
num = abs(num)
num = round(num)
print(num)
#the code that we have written above gives us the positive integer even if the user is a child and doesnt understand it
#we can write the same as nested function calls and make it smaller

print(round(abs(float(input("enter a positive integer :"))))) # SIMPLE 
                                                              # its like onion but ur peeling it from inside
                                                              