# tupple = a collection which is ordered and unchangeable
#          used to group together related data

student = ("me","boys","girls")
print(student.count("bro"))# counts how many times bro has appeared in the tupple
print(student.index("boys"))#finds the index of the element boys

for x in student:
    print(x)

if "me" in student:
    print("i am here")    
   

           