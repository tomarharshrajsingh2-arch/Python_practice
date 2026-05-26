# count=0
# def fun(num):
#     global count
#     count+=1
#     if num<0:
#         print("count is :",count)
#         return
#     print(num)
#     fun(num-1)
# fun(5)


# def countdown(num):
#     global count
#     count+=1
#     print(num)
#     if num==0:
#         print("count is :",count)
#         return
#     else:
#         print("going in recursion with :",num)
#         countdown(num-1)
#         print("completed recursion with :",num)
# print("starting")
# countdown(5)
# print("done")

def fact(num):
    global x
    x=x*num
    if num==1:
        return
    fact(num-1)
x=1
fact(5)
print(x)

def factorial(number):
    if number<=1:
        return 1
    else:
        return number*factorial(number-1)
print(factorial(5))
