# conditional Statement
# if else
# age = int(input("Enter Your age : "))
#
# if age >= 18:
#     print("He is eligible for driving license")
#
# else:
#     print("sorry... he/she is under age.")

# elif : if there are two or more than two condition, elif is required..

# a = int(input("Enter 1st Number : "))
# b = int(input("Enter 2nd Number : "))
# c = int(input("Enter 3rd Number : "))
#
# if a > b and a > c:
#     print(f'{a} is the greatest number.')
#
# elif b > a and b > c:
#     print(f'{b} is the greatest number')
#
# else:
#     print(f'{c} is the greatest number..')
# Nested If stated

number = int(input("Enter Your Age : "))
if number >= 20:
    print("He is eligible for driving license")
    if number > 60:
        print("sorry... he is over age..")

