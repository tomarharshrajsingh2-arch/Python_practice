# class Vehicle:

#     pass
# class LandVehicle(Vehicle):
#     pass
# class TrackedVehicle(LandVehicle):
#     pass 

# for cls1 in [Vehicle,LandVehicle,TrackedVehicle]:
#     for cls2 in[Vehicle,LandVehicle,TrackedVehicle]:
#         print(issubclass(cls1,cls2), end="\t")
#     print()

# class super:
#     supVar =1
# class sub(super):
#     subVar=2
# obj=sub
# print(obj.subVar)
# print(obj.supVar)

# class Super:
#     def __init__ (self):
#         self.supvar=11
# class Sub(Super):
#     def __init__ (self):
#         super().__init__()
#         self.subvar = 12
# obj=Sub()
# print(obj.subvar)
# print(obj.supvar)


# class Level1:
#     variable_1 = 100
#     def __init__(self):
#         self.var_1 = 101
#     def fun_1(self):
#         return 102

# class Level2(Level1):
#     variable_2=200
#     def __init__(self):
#         super().__init__()
#         self.var_2=201
#     def fun_2(self):
#         return 202

# class Level3(Level2):
#     variable_3=300
#     def __init__(self):
#         super().__init__()
#         self.var_3=301
#     def fun_3(self):
#         return 302
    
# obj=Level3()
# print(obj.variable_1,obj.var_1,obj.fun_1())
# print(obj.variable_2,obj.var_2,obj.fun_2())
# print(obj.variable_3,obj.var_3,obj.fun_3())

# print(isinstance(obj,Level1))

# class Vehicle:
#     pass
# class LandVehicle(Vehicle):
#     pass
# class TrackedVehicle(LandVehicle):
#     pass
# my_vehicle =Vehicle()
# My_land_vehicle=LandVehicle()
# My_tracked_vehicle=TrackedVehicle()
# for obj in[my_vehicle,My_land_vehicle,My_tracked_vehicle]:
#     for cls in[Vehicle,LandVehicle,TrackedVehicle]:
#         print(isinstance(obj,cls),end="\t")
#     print()

class SampleClass:
    def __init__(self,val):
        self.val = val

object_1= SampleClass(0)
object_2=SampleClass(2)
object_3= object_1
object_3.val +=1

print(object_1 is object_2)
print(object_2 is object_3)
print(object_3 is object_1)

print(object_1.val,object_2.val,object_3.val)

string_1="Mary had a little "
string_2="Mary had a little lamb"
string_1+="lamb"
print(string_1==string_2,string_1 is string_2)

