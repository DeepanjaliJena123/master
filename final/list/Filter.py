# #2
# - filter() function will take a list and do filtering and give values.
# - filter() takes a sequence and also returns a sequence.
# - filter() function takes two arguments: function and iterable.
#  filter(func, iterable)
# - We have to give the definition of a function that we have passed as a condition in an argument.
# - The defined function should return a value of either True or False based on the condition.
# - Then, filter() will take the value that is returned by the defined function and does perform filtering based on this value.
# - In the defined function, we need only two things i.e, a variable and an expression. So, we can also use the lambda function instead of using the normal function to define the condition for a filter.
# -Lambda reduces the number of lines of code and makes it more precise.
# - Filter() simply returns the iterable passed to it.
#


#exa
# def is_even(n):
#     return n%2==0
#
# nums=[2,8,4,10,7,9,3]
# evens=list(filter(is_even,nums))
# print(evens)

#or using lambda
#filter
# nums=[2,8,4,10,7,9,3]
# # evens=list(filter(lambda n: n%2==0,nums))
# # print(evens)
# even=list(filter(lambda n:n%2==0,nums))
# print(even)

# #map
# doubles=list(map(lambda n:n*2,nums))
# print(doubles)
# double=list(map(lambda n:n*2,nums))
# print(double)

# #reduce
# from functools import reduce
#
# sum=reduce(lambda a,b: a+b,doubles)
# print(sum)

#exa
# def fun(variable):
#     letters = ['a', 'e', 'i', 'o', 'u']
#     if (variable in letters):
#         return True
#     else:
#         return False
#
#
# sequence = ['g', 'e', 'e', 'j', 'k', 's', 'p', 'r']
#
# # using filter function
# filtered = filter(fun, sequence)
#
# print('The filtered letters are:')
# for s in filtered:
#     print(s)


#exa using the lambda function to filter out the odd and even numbers from a list.

# seq = [0, 1, 2, 3, 5, 8, 13]
#
# res=filter(lambda x:x%2!=0,seq)
# print(list(res))
#
# res=filter(lambda x:x%2==0,seq)
# print(list(res))
#


#exa  if a number is a multiple of 3

# def ismultiple_by_3(num):
#     return num%3==0
#
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# res=list(filter(lambda x:ismultiple_by_3(x),numbers))
# print(res)




