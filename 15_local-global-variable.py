# def scope_test():
#     x=123
# scope_test()
# print(x) 

# def my_function():
#     print(f"do i know the var?{var}")
# var=123
# my_function()
# print(var)

# shadowing
# def mult(x):
#     var=7
#     return x*var
# var=3
# print(mult(7))

# def my_function():
#     global var
#     var=2
#     print(f"do i know the var?{var}")
# var=1
# my_function()
# print(var)

# var = 2
# print(var)
# def return_var():
#     global var
#     var=3
#     return var
# print(return_var())
# print(var)

# def my_function(n):
#     print(f"i got {n}")
#     n+=1
#     print(f"i changed n to {n}")
# var=1
# my_function(var)
# print(var)

# def my_function(my_list_1):
#     print("my list 1 :",my_list_1)
#     print("my list 2 :",my_list_2)
#     my_list_1=[1,2]
#     print("my list 1 :",my_list_1)
#     print("my list 2 :",my_list_2)
# my_list_2=[2,3]
# my_function(my_list_2)
# print("my list 2 :",my_list_2)


def my_function(my_list_1):
    print("my list 1 :",my_list_1)
    print("my list 2 :",my_list_2) 
    del(my_list_1[0])
    print("my list 1 :",my_list_1)
    print("my list 2 :",my_list_2)
my_list_2=[2,3]
my_function(my_list_2)
print("my list 2 :",my_list_2)