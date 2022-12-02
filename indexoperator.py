# index operator[] = gives access to sequence's element (str,lists,tuples)

name = "shashank phiske"

if(name[0].islower()): # this will check if the first letter of my name is lower case or not
                       # (here we accessed this string with sequence)
                       # we should use other than[] for other values like tupples
    name = name.capitalize()
first_name = name[0:8] # we created a sub string of the string name
                       # if we add .upper() after name[0:8] the entire str created will be uppercase
                       # if we add .lower() after name[0:8] the entire str created will be lower
                       
print(name)    
print(first_name)