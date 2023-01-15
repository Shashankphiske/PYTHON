import pandas

data = pandas.read_csv("C:\\Users\\shash\\Documents\\PYTHON\\Day25CSVfiles\\Squirrel.csv")

gray_squirrel_count = len(data[data["Primary Fur Color"] == "Gray"]) # number of gray squirrels
red_squirrel_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrel_count = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
    "Colors" : ["Gray","Black","Cinnamon"],
    "Count" : [gray_squirrel_count,black_squirrel_count,red_squirrel_count]
}

new_census_data = pandas.DataFrame(data_dict)
new_census_data.to_csv("New_Census.csv")
