import os

path = "C:\\Users\\shash\\Documents\\PYTHON\\shashank.txt"
if os.path.exists(path):
    print("true")
    if os.path.isfile(path):
        print("it is a file")
    elif os.path.isdir(path):
        print("its a directory")    
else:
    print("false")    