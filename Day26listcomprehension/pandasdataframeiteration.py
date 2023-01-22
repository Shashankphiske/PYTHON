import pandas

temperature = {
        "day":["monday","tueesday"],
        "temp":[23,32]
}

temp_new = pandas.DataFrame(temperature)
print(temp_new)
for (index,row) in temp_new.iterrows():
    print(row)
    print(row.day)