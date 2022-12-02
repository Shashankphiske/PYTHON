#return statement = return statement in used within functions to send python values/objects back to the caller
#                   these values/objects are known as the functions's return value

def multiply(num1 , num2):
    result = num1*num2
    return result     # we can write this function in simpler manners by deleting the 5th line and modifying the 6th
                      # line as return num1*num2

print(multiply(6,8))# we used print here cause the multiply function will call and return value back to the user
                    # which will not be printed
#we can store the returned value in another variable and print it

x = multiply(6,6)
print(x)