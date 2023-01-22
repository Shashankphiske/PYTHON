# we can add a condition to the list comprehension

name = ["alex","beth","shashank"]
new_list = [i for i in name if len(i) == 4]
print(new_list)

numbers = [1,2,3,4,5,6,7,8]
print([n**2 for n in numbers])
print([n for n in numbers if n%2 == 0])