
text = "hello have a good day \n my name is shashank"

with open('test.txt','w') as file:# here we wrote 'w' which as in means write and 'r' means read ,'a' means append
                                  # append means updating without erasing previous data
                                  # just change to 'a' and write ur text and run it the file will be updated
    file.write(text)
with open('test.txt','r') as file:
    print(file.read())  
