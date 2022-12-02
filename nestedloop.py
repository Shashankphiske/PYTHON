#nested loop = its a general consept of having one loop inside another 
#              the inner loop will finish all of its loops before the outer loop finishes its 1st loop
# we will create a pattern using this concept

rows = int(input("how many rows"))
columns = int(input("how many columns"))
symbol = input("which symbol")

for i in range(rows):
    for j in range(columns):
        print(symbol+" " ,end="")
    print()    