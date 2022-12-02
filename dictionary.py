# dictionary = a changeable , unordered collection of   unique key:value pairs
#              they are fast because they use hashing , allow us to acces a value quickly
#              a feature of dictionaries is that they are mutable (we can change them after the program is already running)

capitals = {'India':'New Delhi',
             'USA':'Washington',
             'China':'Beijing'}#here India is the key and New Delhi is the value and capitals is dictionary

print(capitals['India'])#prints the value stored in the key and we use key to access because they are unordered
print(capitals.get('Germany'))#this will check if the key germany exists in my dictionary
print(capitals.keys())# this will print only the keys of the dicitonary
print(capitals.values())# this will print only the values in the dictionary
print(capitals.items ())#this will print everything in a dictionary

capitals.update({'Germany':'Berlin'})# we mutated our dictionary
capitals.update({'USA':'Florida'})# we can also change existing values with update
capitals.pop('USA')# pop will remove a key value pair
capitals.clear()# this will clear the dictionary

for key,value in capitals.items():
    print(key , value)

