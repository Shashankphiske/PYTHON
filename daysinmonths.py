month = int(input("Enter the month :"))
year = int(input("Enter the year :"))

Leap = False

if year%4 == 0:
    if year%100 == 0:
        if year%400 == 0:
            leap = True
        else:
            leap = False
    else:
        leap = True
else:
    leap = False

def days(month, year):
    day = [31,28,31,30,31,30,31,31,30,31,30,31]
    
    if leap:
        if month == 2:
            print(day[month-1]+1)
        else:
            print(day[month-1])
            
    else:
        print(day[month-1])
    
days(month,year)