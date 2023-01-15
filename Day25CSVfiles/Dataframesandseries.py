# the two primary data structures of pandas , Series(1-dimensional ) and Data Frames(2-dimensional),handle vast
# majority of typical use case in finance , statistics , social science and many ares of engineering
# series is basically like a list and a dataframe is like a whole table 
import pandas

data = pandas.read_csv("C:\\Users\\shash\\Documents\\PYTHON\\Day25CSVfiles\\weatherdata.csv")

data_list = data['temp'].to_list() # converts the data under the heading temp in a list
print(data_list)
print(data["temp"].mean())
print(data["temp"].max())

print(data[data.day == 'Monday']) # prints the entire row
print(data[data.temp == 24])

monday = data[data.day == "Monday"]
print(monday.condition)

# creating a data frame from a dictionary

data_dict = {
    "students":["amy","james","angela"],
    "scores":[23,65,16]
}

new_data = pandas.DataFrame(data_dict)
print(new_data)
new_data.to_csv("new_data.csv")