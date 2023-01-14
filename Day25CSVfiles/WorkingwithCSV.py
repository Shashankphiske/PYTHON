# CSV is a very common way to represent tabular data like a spread sheet
# CSV stands for comma separated values
import csv

with open("C:\\Users\\shash\\Documents\\PYTHON\\Day25CSVfiles\\weatherdata.csv") as data:
    data = csv.reader(data) # this has created csv reader object
    temperature = []
    for row in data:
        if row[1] != "temp":
            temperature.append(int(row[1]))
    print(temperature)    

# What is Pandas library : Pandas library is a python data analysis library 
import pandas

data = pandas.read_csv("C:\\Users\\shash\\Documents\\PYTHON\\Day25CSVfiles\\weatherdata.csv")
print(data) # it formated our data much better than the previous method above
print(data.temp) # this will print all the data under the column name temp
                 # pandas take the first row as the heading for each column