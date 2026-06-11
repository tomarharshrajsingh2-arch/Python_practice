import csv
from tokenize import Name
students=[["Name","Age",'M1','M2','M3'],["harsh",20,81,87,89],["abhi",21,87,88,86],["raj",23,71,72,72],["jay",19,64,67,91]]
found=False
with open('student.csv','w',newline='') as f:
    csv.writer(f).writerows(students)
search=input("enter name of student :")
with open('student.csv','r') as f:
    for row in csv.DictReader(f):
        if row["Name"]== search:
            print(f"name:{row['Name']},AGE:{row['Age']},M1:{row['M1']},M2:{row['M2']},M3:{row['M3']}")
            found = True
            break
if not found:        
    print(f"there is no record of {search}")

