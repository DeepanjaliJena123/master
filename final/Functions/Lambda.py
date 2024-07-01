# #Lambda
# #A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression.
#lambda keyword is used to define an anonymous function in Python.
# Syntax: lambda arguments : expression

#exa:
# s#exa:
# str1="geek"
# upper=lambda string:string.upper()
# print(upper(str1))

#exa
# lambda_cube=lambda y:y*y*y
# print(lambda_cube(5))

# #or
# def cube(y):
#     return y*y*y
#
# print(cube(3))

#############list comprehension
# newlist = [expression for item in iterable if condition == True]

#exa
# lis=[1,2,3,4]
# v=[var for var in lis if var%2==0]
# print(v)

#exa
# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# new_lis=[x for x in fruits if "a" in x]
# print(new_lis)

# #exa
# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = []
#
# for x in fruits:
#   if "a" in x:
#     newlist.append(x)
#
# print(newlist)

###exa
# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
#
# newlist = [x for x in fruits if x != "apple"]
#
# print(newlist)

#exa
# #newlist = [x for x in range(10)]
# print(newlist)

#exa
# newlist = [x for x in range(10) if x < 5]
# print(newlist)

#exa
# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = [x.upper() for x in fruits]
# print(newlist)



















