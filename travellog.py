country = input("what is ur country :")
visits = input("travellers visited :")
cities = []
input1 = input("what is the 1st city :")
input2 = input("what is the 2nd city :")
input3 = input("what is the third city :")
cities.append(input1)
cities.append(input2)
cities.append(input3)
travel_log = []
list = input("name the list :")
list = {}
list.update({"country":country})
list.update({"visits":visits})
list.update({"cities":cities})
travel_log.append(list)
print(list)
list.clear() 


