# function() : a block code, store & reuse
# from cgitb import reset


# variable length positional argument 'arg' *
# def add(*data):             # data = (34, 2, 6, 10)
#     sum = 0
#     for numb in data:
#         sum = sum * numb
#     print(sum)

#
# add(34, 2, 6, 10, 100, 450)

# variable length keywords argument "kwarg" **

# def profile(**data):                        # {'id':1002, 'name' : 'ram'}
#     for key, value in data.items():
#         print(key,":", value)
#
# profile(name="Suhana", add="Dang", grad="csit", blood_gp='A+ve')

# Return statement
# def addition(a, b):
#     sum = a + b
#     return sum
#
# result = addition(45, 45)
# print(result)

# Python Recursion

# def sum(n):
#     if n == 1:
#         return 1
#     else:
#         return n * sum(n-1)
#
# n = int(input("Enter Number : "))
# result = sum(n)
# print(result)