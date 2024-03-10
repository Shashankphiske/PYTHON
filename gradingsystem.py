dict = {"Shashank":100,
        "Ishaan":90,
        "Utkarsh":35,
        "Amle":100}
dict2 = {
    "Shashank":"A",
    "Ishaan":"B",
    "Utkarsh":"C",
    "Amle":"D"
    }
sample = dict.keys()
def grade():
    for key in sample:
        if dict.get(key) > 90:
            dict2.update({key:"A"})
        elif dict.get(key) > 80:
            dict2.update({key:"B"})
        elif dict.get(key) > 70:
            dict2.update({key:"C"})
        elif dict.get(key) > 60:
            dict2.update({key:"D"})
        else:
            dict2.update({key:"E"})
grade()
print(dict2)