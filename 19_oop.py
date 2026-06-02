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

# class Student:
#     def __init__(self,name,age,gender,grade):
#         self.name=name
#         self.age=age
#         self.gender=gender
#         self.grade=grade

#     def printdetails(self):
#         print(f"Name: {self.name}")
#         print(f"Age: {self.age}")
#         print(f"Gender: {self.gender}")
#         print(f"Grade: {self.grade}")
# harsh = Student("Harshraj Singh Tomar", 20, "Male", "12th")
# print (harsh)
# # harsh.printdetails()

# class ExampleClass:
#     def __init__(self,val=1):
#         self.first=val
#     def set_second(self,val):
#         self.second = val

# example_object_1= ExampleClass()
# example_object_2=ExampleClass(2)
# example_object_2.set_second(3)
# example_object_3=ExampleClass(4)
# example_object_3.third =5

# print(example_object_1)

# print(example_object_1.__dict__)
# print(example_object_2.__dict__)
# print(example_object_3.__dict__)

# class classy:
#     def method(self,par):
#         print("method ", par)
# obj=classy()
# obj.method(1)

# class classy:
#     varia = 2
#     def method(self):
#         print(self.varia, self.var)
# obj = classy()
# obj.var = 3
# obj.method()

class star:
    def __init__(self,name,galaxy):
        self.name=name
        self.galaxy=galaxy

    def __str__ (self):
        return self.name + ' in ' +self.galaxy    
sun=star("sun","milky way")
print(sun)