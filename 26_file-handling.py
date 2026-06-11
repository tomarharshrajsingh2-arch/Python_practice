# # with open("data.txt","r") as file:
# #     data=file.read()
# # print(data)

# with open ('students.txt','w') as file:
#     file.write("Rahul,22,Bhopal,Engineer\n")
#     file.write("Priya,21,Indore,Doctor\n")
#     file.write("Amit,23,Bhopal,Teacher\n")

# with open('students.txt','r') as file:
#     content=file.read()
#     print(content)

# with open('students.txt','r') as f:
#     for line in f:
#         name , marks , city , profession = line.strip().split(',')
#         print(f"Name: {name}| Marks: {marks}| City: {city}| Profession: {profession}")
#         print("_____________________")


#CSV comma separated values
import csv

records=[
    ['Name','Marks','City','Grade'],
    ['Rahul',85,'Bhopal','B'],
    ['Priya',92,'Indore','A'],
    ['Amit',73,'jabalpur','B']
]

with open('students.csv','w',newline='') as f:
    csv.writer(f).writerows(records)


with open('students.csv','r') as f:
    for row in csv.DictReader(f):
        print(f"{row['Name']}: {row['Marks']} marks ({row['City']})")