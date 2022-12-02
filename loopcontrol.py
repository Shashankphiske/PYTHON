# loop control statements = change a loops execution from its normal sequence
#break = used to terminate a loop entirely
#continue = skips to the next iteration of the loop
#pass = does nothing acts as placeholder

while True:
    name = input("type ur name")
    if name !="":
        break
     

phone_number = "99-33-99999"

for i in phone_number:
    if i == "-":
        continue
    print(i , end = " " )
print("\n")    
    
for j in range(1,21):
    if j ==  13:
        pass
    else:
         print(str( j) , end = " ")

     