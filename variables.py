#a variable is a container or a value , it behaves as the value it contains
#there are various data types in python and as whole in coding languages
name = "shashank"
lastname = "phiske"
integernumber = 3
floatingnumber = 3.3
booleanvalue = False #or True
print("hello "+name)
#we can use the type function to find the type of the variable = print(type(name))
print(name +" "+ lastname)
# [ integernumber + 1 = integernumber ] this the same as integernumber += 1
#print(name +integernumber) this will not work because we are adding an integer data type to string one
# we use typecasting here to do this job, which means we will convert our integer number into string
print(name + str(integernumber) ) 

#print(123_456_789)# here if we print this the _ will be ignored 
                  # it is only used by us humans to better understand the number
# the len function only works on strings
# to avoid the pain of type casting every other data type to use we can use f strings
print(f"the use is great {name} {floatingnumber}{integernumber}{booleanvalue}")                  
