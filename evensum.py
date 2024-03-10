a = int(input("Enter the number :"))
sum = 0
for i in range(1,a+1):
    if i%2 == 0:
        sum += i
    
print("The sum is :",sum)