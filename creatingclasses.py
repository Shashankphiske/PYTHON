class User:
    pass

menu = User()
menu.attribute2 = "hello" # here we added an attribute
print(menu.attribute2)
# an attribute is a variable which associated with an object
# they are such variables associated with the object
# when an object is being created we can set counters or variables to their starting values this is called 
# constructor

# the methods are the things  that an object can do or does
# when a function is attached to an object then its called as a method
class Hello:
    def __init__(self,user_id,user_name):
        self.id = user_id # the attribute id is now associated with the object
        self.user_name = user_name
        self.followers = 0 # in python we can provide default value to the attributes
        self.following = 0
    def follow(self,user):# a method always needs to have a self parameter
                     # which means when this method is called it knows which object called it   
        user.followers += 1
        self.following += 1