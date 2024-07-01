
# #1
# - Normal functions are defined by using the def keyword and function name.
# - A function without a function name is known as an Anonymous function.
# - Anonymous function is called a lambda function.
# - Functions are objects in Python so we can also pass a function in a function.
# - Instead of defining a function, we can directly define it whenever it is required to use.
# - We have to use the lambda keyword to directly define the function in one line.
# - We need to store the lambda function in a variable as the function is also an object.
# - Then, that variable will define the function and we can also use it in other functions.
# - We can pass any number of arguments in a lambda function but it should be only one expression.
# - Lambda functions are syntactically restricted to a single expression.


#2
# Advantages of Lambda Function:-
# - Lambda function supports single-line statements that return some value.
# - It is useful when we have to perform short operations and data manipulations.
# - It saves the time as it requires less time to read the code.

#exa
# str="geeksforgeek"
# upper=lambda string:string.upper()
# print(upper(str))
#
#


#exa
# def cube(y):
#     return y*y*y
#
# lambda_cube=lambda y:y*y*y
# print(lambda_cube(5))


#EXA  Filter all people having age more than 18, using lambda and filter() function

# ages = [13, 90, 17, 59, 21, 60, 5]
# adults = list(filter(lambda age: age > 18, ages))
#
# print(adults)

#EXA  Multiply all elements of a list by 2 using lambda and map() function


# li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]
#
# final_list = list(map(lambda x: x * 2, li))
# print(final_list)
# #

#exa:Transform all elements of a list to upper case using lambda and map() function
#
# animals = ['dog', 'cat', 'parrot', 'rabbit']
# uppered_animals = list(map(lambda animal: animal.upper(), animals))
#
# print(uppered_animals)

#exa  A sum of all elements in a list using lambda and reduce() function
# from functools import reduce
# li = [5, 8, 10, 20, 50, 100]
# sum = reduce((lambda x, y: x + y), li)
# print(sum)

#Find the maximum element in a list using lambda and reduce() function
# import functools
# lis = [1, 3, 5, 6, 2, ]
# print("The maximum element of the list is : ", end="")
# print(functools.reduce(lambda a, b: a if a > b else b, lis))
#
#









