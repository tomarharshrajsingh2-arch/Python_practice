# class ExampleClass:
#     counter = 0
#     def __init__(self,val=1):
#         self.__first=val
#         ExampleClass.counter +=1

# example_object_1= ExampleClass()
# example_object_2=ExampleClass(2)
# example_object_3=ExampleClass(4)

# print(example_object_1.__dict__,example_object_1.counter)
# print(example_object_2.__dict__,example_object_2.counter)
# print(example_object_3.__dict__,example_object_3.counter)

# print(ExampleClass.counter)

# class ExampleClass:
#     a=1
#     counter = 0
#     def __init__(self,val=1):
#         ExampleClass.counter +=1
#         if val%2!=0:
#             self.a=1
#         else:
#             self.b=1
# example_object= ExampleClass(1)
# # way 1 with try catch
# try:
#     print("a =",example_object.a)
# except AttributeError:
#     print("a is not defined")
# try:
#     print("b =",example_object.b)
# except AttributeError:
#     print("b is not defined")

# way 2 with try catch nested try catch
# try:
#     print("a =",example_object.a)
# except AttributeError:
#     print("a is not defined")
#     try:
#         print("b =",example_object.b)
#     except AttributeError:
#         print("b is not defined")

# way 3 with hasattr
# if hasattr(example_object,'a'):
#     print("a =",example_object.a)
# if hasattr(example_object,'b'):
#     print("b =",example_object.b)

# print (hasattr(ExampleClass,'a'))
# print (hasattr(ExampleClass,'b'))


# class Python:
#     population=1
#     victims=0
#     def __init__ (self):
#         self . length_ft=3
#         self.__venemous =False
# myObj =Python()
# print("myObj.population: ",myObj.population)
# print("myObj.victims :",myObj.victims)
# print("myObj.length_ft :",myObj.length_ft)
# print("myObj.__venemous :",myObj._Python__venemous)


#name mangling
class Classy:
    def visible(self):
        print("visible")
    def __hidden(self):
        print("hidden")
        
obj= Classy()
obj.visible()
try:
    obj.__hidden()
except:
    print("failed")
obj._Classy__hidden()


obj =Classy()
print(type(obj))
print(type(obj).__name__)