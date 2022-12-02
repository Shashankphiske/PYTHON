from prettytable import PrettyTable

table = PrettyTable()
table.add_column("pokemon",["lizard","charmander"])
table.align = "l" #use "r,"c" for different aligns
print(table)