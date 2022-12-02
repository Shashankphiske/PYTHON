
from multiprocessing.sharedctypes import Value
from turtle import st


students_grades = {"harry":81 ,"ron":78,"Shashank":99,"Draco":74,"Neville":62}

for key,Value in students_grades.items():
    if students_grades[key] > 91 and students_grades[key] < 100:
        students_grades.update({key:"Outstanding"})
    elif students_grades[key] >= 81 and students_grades[key] < 91:
        students_grades.update({key:"Excellent"})
    elif students_grades[key] > 71 and students_grades[key] < 81:
        students_grades.update({key:"Acceptable"})
    elif students_grades[key] <= 70 :
        students_grades.update({key:"Average"})          
print(students_grades)        