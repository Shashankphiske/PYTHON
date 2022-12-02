from calculatorart import logo
print(logo)
print("Hi ,Welcome to the Calculator!")
result = ["0"]
num = [0]
value = "yes"
while value != "no":
    if result[0] != num[0]: 
        num[0] = float(input("What is your first number? :"))
    operation = input('''+
-
*
/
Which operation do you want? :''')


    num_2 = float(input("What is your second number? :"))
    
    if operation == "+":
        num[0] += num_2
    elif operation == "-":
        num[0] -= num_2
    elif operation == "*":
        num[0] *= num_2
    else:
        num[0] /= num_2
    result[0] = num[0]    
    print(result[0]) 
    value = input("Do you want to continue with the operation or create a new operation? yes or no or new:")
    if value == "new":
        num[0] = 0
        result[0] = "0"
               


 