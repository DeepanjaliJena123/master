# A Generator in Python is a function that returns an iterator using the Yield keyword.

#syntax:  def function_name():
    #         yield statement

#exa
# def simplegeneratorfun():
#     yield 1
#     yield 2
#     yield 3
# for value in simplegeneratorfun():
#     print(value)

# Generator Object
# Python Generator functions return a generator object that is iterable, i.e., can be used as an Iterator.
# Generator objects are used either by calling the next method of the generator object or using the generator object in a “for in” loop.
#
# Example:
# def simplegeneratorfun():
#     yield 1
#     yield 2
#     yield 3
#
# x=simplegeneratorfun()
# print(next(x))
# print(next(x))
# print(next(x))

######3 we will create two generators for Fibonacci Numbers, first a simple generator and second generator using a for loop.
# # A simple generator for Fibonacci Numbers
def fib(limit):
    # Initialize first two Fibonacci Numbers
    a, b = 0, 1

    # One by one yield next Fibonacci Number
    while a < limit:
        yield a
        a, b = b, a + b
x = fib(5)
#
# # Iterating over the generator object using next
# # In Python 3, __next__()
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))
#
# # Iterating over the generator object using for
# # in loop.
# print("\nUsing for in loop")
# for i in fib(5):
#     print(i)                                            #doubt


#exa::Python Generator Expression
# The generator expression in Python has the following Syntax:
# (expression for item in iterable)

# Example:
#
# In this example, we will create a generator object
# that will print the multiples of 5 between the range of 0 to 5 which are also divisible by 2.
# generator_exp = (i * 5 for i in range(5) if i % 2 == 0)

############   Difference Between Iterator VS Generator   ########
# a = [0, 5, 10, 15, 20]
# for i in a:
#     if i%2==0:
#         print(str(i),"is an even number")
#     else:
#         print(str(i),"is an odd number")
#
#


#ex
# iter_list = iter(['Geeks', 'For', 'Geeks'])
# print(next(iter_list))
# print(next(iter_list))
# print(next(iter_list))



#EXA GEN
# def sq_numbers(n):
#     for i in range(1, n+1):
#         yield i*i
# a = sq_numbers(3)
#
# print("The square of numbers 1,2,3 are : ")
# print(next(a))
# print(next(a))
# print(next(a))

# def sq_numbers(n):
#     for i in range(1,n+1):
#         yield i*i
# a=sq_numbers(3)
#
# print(next(a))
# print(next(a))
# print(next(a))




