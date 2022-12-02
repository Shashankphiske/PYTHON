# **kwargs = is a parameter that will pack all the arguments into a dictionary 
#            useful so that a function can accept a varying amount of keyword arguments

def hello(**hallo):
    print("hello "+hallo['first']+hallo['last']) # we can also write this as
    for key,value in hallo.items(): # this will print all the values in the kwars hallo
        print( value , end=" ")

hello(first="shashank" , last="phiske")    