numbers = [1,2,3]
new_item = [n+1 for n in numbers] # this is list comprehension
                                  # we created a list by adding 1 to each element but in one line
                                  # we can use any data we want   
print(new_item)

rangeitem = [n*2 for n in range(1,5)]
print(rangeitem)