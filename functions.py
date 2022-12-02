# functions = a block of code which is executed only when it is called

def hello():
    print("hello") # we created a function

hello() # we used this function to print hello
def names(name):
    print("hello "+name) # in this function the name is called a parameter 
                         # this is where the argument is placed (here bro)

names("bro")  #bro is an argument , we can use different variables to specify agruments like myname = bro and then 
              #pass in myname in place of argument
              # we can also send multiple arguments by placing a comma but there should be those many parameters
              # in the function 
              # the arguments used here are positional arguments     
# using title function
print("how are u?".title())              