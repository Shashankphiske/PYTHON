import os
import shutil#we imported this to delete non empty folders

path = "test.txt" # we will use this to remove files
folder = "shashank"
exampledpath = "shashank"
try:
    #os.remove(path)# it wont delete a folder or if you try you will get a permission error
    #os.rmdir(folder)# we will use this to remove an empty folder
    shutil.rmtree(exampledpath)# we will use this to delete a folder that is non empty
except FileNotFoundError:
    print("file doesnt exist")    
except PermissionError:
    print("you dont have permission to do that")  
except OSError:
    print(" you cant delete that using that function")      
else:
    print("file was deleted")   