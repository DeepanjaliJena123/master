#4
# - reduce() function is used to reduce the number of values from a list.
# - reduce() function belongs to a module known as functools.
# - We have to import the module functools from the library to use the reduce function.
# - reduce() also take two arguments i.e., a function and a sequence.
#  reduce(func, iterable[, initial])
# - We have to give the definition of a function that we have passed as a condition in an argument.
# - The lambda function can also be used in an argument as a function instead of defining the normal function for the logic.
# import functools

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




#exa
# import functools
#
# lis=[1,3,4,2,6]
# print("The sum of the list element is :",end="")
# print(functools.reduce(lambda a,b:a+b,lis))

# lis=[1,3,4,2,6]
# #get max elemnt from list
# print(functools.reduce(lambda a,b:a if a>b else b,lis))
#
#
#
#exa:Using Operator Functions
# import functools
# import operator
# lis=[2,3,5,6,7]
# print("The sum of the list element is :",end="")
# print(functools.reduce(operator.add,lis))
# print("The multiply of the list element is :",end="")
# print(functools.reduce(operator.mul,lis))
#
# #exa: # using reduce to concatenate string
# print(functools.reduce(operator.add,["geek","for","python"]))



#####  Reduce() vs Accumulate()

# Both reduce() and accumulate() can be used to calculate the summation of a sequence elements.
# But there are differences in the implementation aspects in both of these.
#reduce() is defined in “functools” module, accumulate() in “itertools” module.
# reduce() stores the intermediate result and only returns the final summation value.
# Whereas, accumulate() returns a iterator containing the intermediate results.
# The last number of the iterator returned is summation value of the list.
# reduce(fun, seq) takes function as 1st and sequence as 2nd argument.
# In contrast accumulate(seq, fun) takes sequence as 1st argument and function as 2nd argument.
#
# import itertools
#
# lis=[1,2,4,5]
# print(list(itertools.accumulate(lis,lambda x,y:x+y)))
#
#


