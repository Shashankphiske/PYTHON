'''string slicing = create a substring by extracting elements from another string
                    indexing[] or slicing()
                    [start:stop:step]'''

full_name = "shashank phiske"
first_name = full_name[0:8]#full_name[:8] this will also work the same
last_name = full_name[8:15]#full_name[8:] this will also work the same
funky_name = full_name[0:15:2]
reversed_name = full_name[::-1]
print(first_name)
print(last_name)
print(funky_name)
print(reversed_name)
#now for using slice() operator
string = "www.google.com"
slice = slice(4,-4)
print(string[slice])
