with open("C:\\Users\\shash\\Documents\\PYTHON\\Day26listcomprehension\\file1.txt") as file1:
    data1 = file1.readlines()
with open("C:\\Users\\shash\\Documents\\PYTHON\\Day26listcomprehension\\file2.txt") as file2:
    data2 = file2.readlines()   

data3 = [int(n) for n in data1 if n in data2]
print(data3)