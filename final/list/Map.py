# 3
# - map() function is used when we want to change the value of every element of a list.
# - map() function also takes two arguments i.e., a function and an iterable.
#  map(func, *iterables)
# -  To get the result as a list, the built-in list() function can be called on the map object.
# - We have to define a function that we have passed as a condition in an argument.
# - The defined function should return any value.
# - The lambda function can also be used in an argument as a function instead of defining the normal function for the logic.
# - map() function returns a list. The function returns a map object which is a generator object.
#

#filter
# nums=[2,8,4,10,7,9,3]
# evens=list(filter(lambda n: n%2==0,nums))
# print(evens)
#
# #map
# doubles=list(map(lambda n:n*2,nums))
# print(doubles)
#
# #reduce
# from functools import reduce
#
# sum=reduce(lambda a,b: a+b,doubles)
# print(sum)
#
#

#exa: # Return double of n
# def addition(n):
#     return n+n

# seq=[1,3,4,5]
# # res=list(map(addition,seq))
# # print(res)
#
# #or lambda
# res=list(map(lambda n:n+n,seq))
# print(res)

# exa
# number=(1,2,3,)
# res=list(map(lambda x:x+x,number))
# print(res)


#exa# Add two lists using map and lambda
# num1=[1,2,3]
# num2=[4,5,6]
# res=list(map(lambda x,y:x+y,num1,num2))
# print(res)
#
# #exa
# # map() can listify the list of strings individually
#
# l = ['sat', 'bat', 'cat', 'mat']
# test=list(map(list,l))
# print(test)
#

## Define a function that doubles even numbers and leaves odd numbers as is
# def double_even(num):
#     if num%2==0:
#         return num*2
#     else:
#         return num
#
# numbers=[1,2,3,4]
# res=list(map(double_even,numbers))
# print(res)
#











