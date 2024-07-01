#Functions:
# Block of statement that perform a specific task

# def func_name(param1,param2:)
#     #some work
#     return val
#
# func_name(arg1,arg2) #function call

#recursion
# def show(n):
#     if(n==0):
#         return
#     print(n)
#     show(n-1)
# show(5)

###### geeks and geeks functions examples
#exa
# def fun():
#     print("welcome")
# fun()

#exa
# def sum(a,b):
#     print(a+b)
# sum(1,2)
#
#

#exa
# def add(num1:int,num2:int):
#     num3=num1+num2
#     return num3
# num1,num2=5,15
# ans=add(num1,num2)
# print(f"The addition of {num1} and {num2} results {ans}.")
#

######## Arbitrary Keyword  Arguments #########
# *args in Python (Non-Keyword Arguments)
# **kwargs in Python (Keyword Arguments)

# def myfun(*args):
#     for arg in args:
#         print(arg)
# myfun("hello","welcome",'to',"geek")

#exa:
# def myfun(**kwargs):
#     for key, value in kwargs.items():
#         print("%s==%s" % (key,value))
#
# myfun(first='geek',mid='for',last='geek')
#

# Types of Python Function Arguments

# Python supports various types of arguments that can be passed at the time of the function call. In Python,
# we have the following 4 types of function arguments.
#
# Default argument
# Keyword arguments (named arguments)
# Positional arguments
# Arbitrary arguments (variable-length arguments *args and **kwargs)
#

####### Default Arguments :
# Default arguments are values that are provided while defining functions.
# The assignment operator = is used to assign a default value to the argument.
# Default arguments become optional during the function calls

# def myfun(x,y=10):
#     print("x:",x)
#     print("y:",y)
# myfun(20)

############ Keyword Arguments:
# :allow the caller to specify the argument name with values ,
# so that the caller does not need to remember the order of parameters.

# def Student(firstname,lastname):
#     print(firstname,lastname)
#
# Student(firstname="Deepanjali",lastname="Jena")
#

######  Positional Arguments:
# :whenever we pass the arguments in function,the 1st argument is always listed 1st,whn the function is called.
#2nd argument is needs to be called 2nd.

#exa
# def Nameage(name,age):
#     print("Name:",name)
#     print("Age:",age)
#
# Nameage("diya",29)

###### Arbitrary Keyword  Arguments:
# Arbitrary Keyword Arguments, *args, and **kwargs can pass a variable number of arguments to a function using special symbols.
# There are two special symbols:
#1:: *args in Python (Non-Keyword Arguments)
#2:: **kwargs in Python (Keyword Arguments)


#*args
#exa
# def add(x,y):
#     print("Sum:",x+y)
#
# add(2,-4)

#exa: # Program to add and display the sum of n number of integer
#
# def add(*num):
#     sum=0
#     for n in num:
#         sum+=n
#     print(sum)
#
# add(1,2,3,5)


#exa
# def func(a,*args):
#     print("value of a is :",a)
#     for i in args:
#         print("args is :",i)
# func("hey",'i','am','jen')

#exa
# def Person(*args):
#     print(args)
#
# Person('Sean', 'Male', 38, 'London', 9375821987)

## **kwargs examples

# Print values of function Person along with its associated keywords
# def Person(**kwargs):
#     for key, value in kwargs.items():
#         print("{} -> {}".format(key, value))    # OR print(f'{key} -> {value}')
#
# Person(Name = 'Sean', Sex = 'Male', Age = 38, City = 'London', Mobile = 9375821987)
#



#keyword n nonokeyword
# def person(a,b):
#     print(a+b)
# person(1,2)

#
# def add(a,b):
#     print(a+b)
# add(a=2,b=5)

# def person(*args):
#     print(args)
# person("a",1,2,3,"name")

# def person(**kwargs):
#     for key,value in kwargs.items():
#         print("{},{}".format(key,value))
# person(name="sita",sex="female",age=25)
# def person(**kwargs):
#     for key,value in kwargs.items():
#         print("{}:{}".format(key,value))
#
# person(name="ram",age=22,a="djf")

