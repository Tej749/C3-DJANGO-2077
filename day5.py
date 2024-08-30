# control statement
# store and reuse, multiple
# reusability
# a block of code
# represent by def keyword

# def addition(a, b, c):
#     x = a + b + c
#     print(x)
#
# addition(23, 56, 450)
# addition(50, 290, 432)
# addition(500, 250, 120)

# Variable lenghth positional argument 'arg'

# def sums(*data):
#     sum = 0
#     for value in data:
#         sum = sum + value
#     print(sum)
#
# sums(2, 4, 6, 8, 567, 23, 12, 67, 45, 12, 12, 34, 89)

# Variable length keyword argument ('**kwargs")
'''
name = "shreeya", age=19, add="npj"
'''

def details(**data):
    for key, i in data.items():
        print(key,"--->", i)

details(name="Shreeya", add="Nepalgunj", mob=9877666, dob="16/07/2058", sports="volleyball")


