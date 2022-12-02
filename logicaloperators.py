#logical operators(and,or,not) = used to check if two or more conditional statements are true

temp = int(input("what is the temp"))

if not(temp>=0 and temp<=30):
    print("temp is good")
elif not(temp<=0 and temp>=30):
    print("temp is not good")
#not operator will reverse the output value meaning line 5 was true but it became false if we add not operator
       

