# str.format() = optional method which gives users more control when displaying output

animal = "cow"
item = "moon"

print("the "+animal +" jumped over the " + item) # we can write the same as 
print("the {} jumped over the {}".format("cow" , "moon")) # i can also place the variable animal and item in place 
                                                          # of these values
                                                          # the curly brackets are called format fields they function
                                                          # as a place holder for a value or variable
print("the {0} jumped over the {1}".format("cow" , "moon"))# we can also use index numbers to place them called 
                                                           # positional arguments
print("the {animal} jumped over the {item}".format(animal="cow" , item="moon"))# we can also use keyword arguments
                                                                               # we can use these arguments in multiple places also
text = " the {} jumped over the {}"
print(text.format("cow","moon"))

# now we will see how we can add padding to a string when displaying using format method
name = "bro"
print("hello {:10} nice to meet you".format(name))# i added a space of length 10units after the value
print("hello {:<10} nice to meet you".format(name))# we left aligned this value bro                                                                            
print("hello {:>10} nice to meet you".format(name))# we right aligned this value
print("hello {:^10} nice to meet you".format(name))# we centre aligned it
# if u want to add positional or keyword argument we can type it like {name:10} or {0:10}
# we can format number by

number = 3.14352
print(" the pi value is {:.2f}".format(number))# i displayed only the first 2 digits after the decimal for a float
 
num = 1000
print(" the number is {:,}".format(num))# :, will automatically add a comma after every thousands places
print(" the number is {:b}".format(num))# :b will convert our number into binary
#:o will give octal number ,:x or :X will give a hexadecimal number , :e or :E for scientific                                   
                                         