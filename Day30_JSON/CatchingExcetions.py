# The process of detecting and responding to the anomalies that might occur in the code

# try : Something that might cause an exception. The program to be executed will go here

# except : Do this if there was an exception

# else : Do this if there was no exception

# finally : Do this no matter what happens

#FileNotFound
try:
    file = open("a_file.txt")
    a = {"a":20}    
    print(a["c"])
except FileNotFoundError:
    print("There was an error")
    # if you want to create the file instead you can open file in write mode
except KeyError as error_message:
    print("The does not exist")
    print(error_message)
else:
    print(a["a"])
finally:
    print("This will happen no matter what")
    
# raising your own exceptions using : raise

    raise KeyError # this will crash our program even if there is no keyerror in the program because we raised this or made it
    raise FileExistsError("This error is made by me") # message can be also given by error