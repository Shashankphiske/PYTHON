def add(*the_list):
    a = 0
    for n in the_list:
        a += n
    print(a)
add(2,34,6,7,8,9)        

def calculate(n , **the_dict):
    add = n + the_dict['a']
    multiply = n* the_dict['b']
    print(add)
    print(multiply)
calculate(2,a=3,b=4)    

# creating class with optional keyword arguments

class car:
    def __init__(self,**kw):
        self.make = kw.get('make')
        self.model = kw.get('model')

mycar = car(make = "nissan")
print(mycar.make)
print(mycar.model) # this will give none as there is no passed in value for model and we created a optional argument
