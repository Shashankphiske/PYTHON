import math #math module which this program or code can use it is built in
pi = 3.14
x = 3
y = 5
z = 9
print(round(pi))#this will round the value provided to the nearest integer,it is a built in function
print(round(2.33333,2))# here we specified ,2 which means round to 2 decimal places
print(8//3)# here as the division operator always converts a result to float we can use // floor division to chop of all the floating numbers and convert it directly to an integer

print(math.ceil(pi))#this function is accessed through math module , it will round the value up to the nearest integer
print(math.floor(pi))#this function will round down the value to the nearest integer 
print(abs(pi))#this function will give how far the value is from 0
print(pow(pi,2))#this function will raise the given value to the given power , here pi is base and 2 is exponent
print(math.sqrt(pi))#this will give the sqr root of the value (keep it positive)
print(max(x,y,z))#this function will give the max value from the given variables
print(min(x,y,z))#this will give the min value of the function
print(2**3)# here ** means power of (here 2 is base and 3 is power)
# the math operations follow step by step by step rule of PEMDAS
# power,exponents,multiplication,division,addition,substraction
# we can execute a block of operation of our will first by adding a ( ) around the operation
# eg : ((3+3)- 3*3) here * should have happened first but + will happen 