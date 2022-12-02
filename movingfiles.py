import os

source = "test.txt"
destination = "C:\\Users\\shash\\Pictures\\Saved Pictures\\test.txt "

try:
    if os.path.exists(destination):
        print("there is already a file there")
    else:
        os.replace(source,destination)
        print(source+"was replaced")
except FileNotFoundError:
    print("source was not found")
    

