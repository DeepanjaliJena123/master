######  LAMBDA

# An anonymous function in Python is a function without a name.
# It can be immediately invoked or stored in a variable.
# Anonymous functions in Python are also known as lambda functions.

#ORR
# Lambda functions are similar to user-defined functions but without a name.
# They're commonly referred to as anonymous functions. Lambda functions are efficient ' \
#  'whenever you want to create a function that will only contain simple expressions –' \
#  'that is, expressions that are usually a single line of a statement
#
##orr


#EXA

# def fun(x): return x*x*x
# print(fun(5))
#
# cube_v=lambda x:x*x*x
# print(cube_v(3))


##exa
# calc=lambda num:"even number" if num%2==0 else "odd number"
#
# print(calc(20))

#exa
#
# filters_num=lambda s:"".join([ch for ch in s if not ch.isdigit()])
# print("filters_num :",filters_num("geek123"))
#
# do_exclaim=lambda s:s+"!"
# print("do_exclaim :",do_exclaim("i am tired"))
#
# find_sum=lambda n:sum([int(x) for x in str(n)])
# print("sum: ",find_sum(101))

#exa
# str="Geeksforgeek"
# upper=lambda string:string.upper()
# print(upper(str))

#exa::def and lambda
# def cube(x):
#     return x*x*x
#
# lambda_cube=lambda x:x*x*x
# print("the def value is :",cube(5))
# print("the lambda value is :",lambda_cube(3))








