scorelist = input("Enter the scores of the students :").split()

highscore = 0
for i in scorelist:
    if(highscore < int(i)):
        highscore = int(i)

print("The highest number is :"+str(highscore))