'''
the process of copying processes or methods from an existing class into another class is called inheritence
we can inherit apppearance (attributes) as well as behaviour
'''
# For eg :
class animal:
    def __init__(self):
        self.eyes = 2
    def breathe(self):
        print("inhale,exhale")
class fish(animal):
    def __init__(self):
        super().__init__() # we took the super class which here is animal 
    def breathe(self):
        super().breathe()
        print("just underwater")                

fish = fish()
fish.breathe()