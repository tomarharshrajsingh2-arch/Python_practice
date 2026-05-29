# class Simplest_class:
#     name="harsh"
#     age=20
    
#     def getname(self):
#         print(self.name)


# firstobject=Simplest_class()
# print(firstobject)

# firstobject.getname()
# print(firstobject.name)
# print(firstobject.age)

class Student:
    def __init__(self,name,age,gender,grade):
        self.name=name
        self.age=age
        self.gender=gender
        self.grade=grade

    def printdetails(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")
        print(f"Grade: {self.grade}")
harsh = Student("Harshraj Singh Tomar", 20, "Male", "12th")
print (harsh)
harsh.printdetails()


