import pandas

data = pandas.read_csv("C:\\Users\\shash\\Documents\\PYTHON\\Day26listcomprehension\\nato_phonetic_alphabet.csv")

dict_data = {row.letter:row.code for (index,row) in data.iterrows()}
a = input("name :").upper()
new_data = [dict_data[letter] for letter in a]
print(new_data)