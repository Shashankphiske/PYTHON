l1 = [" "," "," "]
l2 = [" "," "," "]
l3 = [" "," "," "]

#rows will numbers(1,2,3) and columns will alphabets(A,B,C)
mainlist = [l1,l2,l3]

pos = input("Enter the position :")

col = pos[0]
row = int(pos[1])

if col == "A":
    col = 0
elif col == "B":
    col = 1
elif col == "C":
    col = 2
else:
    print("Give correct position")
    
mainlist[row-1][col] = "X"
for i in mainlist:
    print(i)