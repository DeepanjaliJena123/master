######  function

# def fun():
#     print("hello")
#
# fun()

#exa

# def add(num1:int,num2:int):
#     num3=num1+num2
#     return num3
#
# num1,num2=5,10
# ans=add(num1,num2)
#
# print(ans)

## exa
# def is_prime(n):
#     if n in [2,3]:
#         return True
#     if n==1 or n%2==0:
#         return False
#
#     r=3
#
#     while r*r<=n:
#         if n%r==0:
#             return False
#         r+=2
#
#     return True
# print(is_prime(78),is_prime(79))


#exa

# def even_odd(x):
#     if x%2==0:
#         print("even")
#     else:
#         print("odd")
# even_odd(12)
# even_odd(9)

# 4typs of arguments in function
#1:Default argument
#2:keyword argument
#3:positional argument
#4:arbitary argument (*args,**kwargs)


#####  1: Default argument:::
#Default arguments are values that are provided while defining functions.
#
# def myfun(x,y=10):
#     print("x:",x)
#     print("y:",y)
#
# myfun(5)

#2:: Keyword argument

# def student(firstname,lastname):
#     print(firstname,lastname)
#
# student(firstname="python",lastname="geek")

#3::positional argument

# def nameage(name,age):
#     print("my name is ",name)
#     print("my age is ",age)
#
# print("case1")
# nameage("surya",28)
#
# print("case2")
# nameage("nasha",30)


#4::atribitary argument:

# def myfun(*argv):
#     for arg in argv:
#         print(arg)
#
# myfun("hell",'welcoen',"jsahs")

#kwargs:

# def myfun(**kwargs):
#     for key,value in kwargs.items():
#         print("%s==%s" % (key,value))
#
# myfun(name="geeksngeek",language="python",year=2024)


#exa
# def factorial(n):
#     if n==0:
#         return 1
#     else:
#         return n * factorial(n-1)
#
# print(factorial(3))


####  *args
# is used to pass a variable number of arguments to a function.
# It is used to pass a non-keyworded, variable-length argument list.
#What *args allows you to do is take in more arguments than the number of formal arguments

#exa
# def myfun(*argv):
#     for arg in argv:
#         print(arg)
# myfun("hello","python","for geek")


#exa:: pass argument
# def myfun(arg1,*argv):
#     print("first argument",arg1)
#     for arg in argv:
#         print("second argument through :",arg)
#
# myfun("hello","geek","python","java")


####   **kwargs
# is used to pass a keyworded, variable-length argument list
#The reason is that the double star allows us to pass through keyword arguments (and any number of them).


#exa
# def myfun(**kwargs):
#     for key,value in kwargs.items():
#         print("%s==%s" % (key,value))
#
# myfun(name="python",year="2024")

#exa extra argument

# def myfun(arg1,**kwargs):
#     for key,value in kwargs.items():
#         print("%s==%s" % (key,value))
#
# myfun("h",n="hi",name="python",year="2024")


#exa:: Using both *args and **kwargs in Python to call a function
# def myfun(arg1,arg2,arg3):
#      print("arg1 :",arg1)
#      print("arg2 :",arg2)
#      print("arg3 :",arg3)
#
# args=("geek","for","python")
# myfun(*args)
#
# kwargs={"arg1":1,"arg2":2,"arg3":3}
# myfun(**kwargs)


##we are passing *args and **kwargs as an argument in the myFun function.
# def myfun(*args,**kwargs):
#     print("args:",args)
#     print("kwargs",kwargs)
#
# myfun("a","b","c",name="python",company="geeksandgeeks")
#

#exa::Using *args and **kwargs in Python to set values of object

# class car:
#     def __init__(self,*args):
#         self.speed=args[0]
#         self.color=args[1]
#
# audi = car(200, 'red')
# bmw = car(250, 'black')
# mb = car(190, 'white')
#
# print(audi.color)
# print(bmw.color)
# print(audi.speed)



##
# class car():
#     # args receives unlimited no. of arguments as an array
#     def __init__(self, **kwargs):
#         # access args index like array does
#         self.speed = kwargs['s']
#         self.color = kwargs['c']
#
#
# # creating objects of car class
# audi = car(s=200, c='red')
# bmw = car(s=250, c='black')
# mb = car(s=190, c='white')
#
# print(audi.color)
# print(audi.speed)






