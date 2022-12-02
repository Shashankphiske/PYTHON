with open('shashank.txt') as file:# here i didnt needed to give the entire path cause its already in my python folder
    print(file.read())
# this will automatically close the file but we can test this
print(file.closed)    