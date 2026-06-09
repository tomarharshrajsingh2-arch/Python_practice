# def reciprocal(n):
#     try:
#         n=1/n
#     except ZeroDivisionError:
#         print("division failed")
#         n= None
#     else:
#         print("division successful")
#         return n
#     finally:
#         print("final block executed")
#     return n
# print("----------")
# print("reciprocal(2):", reciprocal(2))
# print("----------")
# print("reciprocal(0):", reciprocal(0))
# print("----------")




try:
    i = int("hello")
except Exception as e:
    print(e)
    print(e.__str__())


class MyZeroDivisionError(ZeroDivisionError):
    pass
def do_the_division(mine):
    if mine :
        raise MyZeroDivisionError("some worse news")
    else:
        raise ZeroDivisionError("some bad news")
do_the_division(False)

