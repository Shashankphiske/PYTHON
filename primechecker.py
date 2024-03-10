a = int(input("Enter the number :"))
def checker():
    b = True
    for i in range(2,a):
        if a%i == 0:
            b = False       
    if b == True:
        print("The number is prime")
    elif b == False:
        print("The number is not prime")
        
checker()