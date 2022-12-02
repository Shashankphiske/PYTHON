#scope = scope of a variable is a region that a variable is recognized 
#        a variable is only available inside the region it is created 
#        a global and localy scoped versions of a variable can be created 

def firstname():
    name = "shashank"# here in this function the variable name is localy scoped variable and cannot be accessed globaly
    print(name)     

lastname = "phiske" # here this is a global variable and can be used by any function
                    # i can also name this variable name same as defined in above function but they will be different
firstname()
print(lastname)  

# if we use a variable inside of a function it will first look for the local version of it
# or it will use the global version if available
# there is rule for this in python it is =  LEGB (local , Enclosing , Global , Built in)