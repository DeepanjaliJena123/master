#DATA ABSTRACTION
#Hiding the implementation details of a class and showing only the essential feature to the user.


#abstract class is a class that contains one or more abstract method is call abstarct class.
#and objcet of abstract clas con not be created .
#python provide abc module to work with abstraction.
#we use @abstractmethod decorator define abstarct method

#or:
#It enables programmers to hide complex implementation details while just showing users the most crucial data and functions.
# This abstraction makes it easier to design modular and well-organized code, makes it simpler to understand
# and maintain, promotes code reuse, and improves developer collaboration.

# Data hiding
#
# In Python, we use double underscore (Or __) before the attributes name
# and those attributes will not be directly visible outside.
#
# class Myclass:
#     __hiddenvariable=0
#
#     def add(self,increment):
#         self.__hiddenvariable+=increment
#         print(self.__hiddenvariable)
#
# obj=Myclass()
# obj.add(2)
# obj.add(5)

# print(obj.__hiddenvariable)   #we tried to call outside of class,it threw an exception
# AttributeError: MyClass instance has
# no attribute '__hiddenVariable'

#but we can call it by using tricky syntax

# class Myclass:
#     __hiddenvariable=10
#
#
# obj=Myclass()
# print(obj._Myclass__hiddenvariable)
#


############   Printing Objects :
# # In python, this can be achieved by using __repr__ or __str__ methods.
# class Test:
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#     def __repr__(self):
#         return "Test a:%s b:%s" % (self.a, self.b)
#     def __str__(self):
#         return "From str method of Test:a is %s,"\
#             "b is %s" % (self.a, self.b)
#
# t=Test(123,568)
# print(t)   # This calls __str__()
# # #From str method of Test:a is 123,b is 568
# print([t]) ## This calls __repr__()
# # [Test a:123 b:568]
#

#### If no __repr__ method is defined then the default is used
# class Test:
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#
# t=Test(123,5689)
# print(t)
#<__main__.Test object at 0x01647570>



######### abstract examples from youtube
# from abc import ABC,abstractmethod
# class Car(ABC):
#     def show(self):
#         print("Every car has 4 wheels")
#
#     @abstractmethod
#     def speed(self):
#         pass         #if we not provide pass, it will throw Indention error
# class Maruti(Car):
#     def speed(self):
#         print("speed is 100km/h")
# class Suzuki(Car):
#     def speed(self):
#         print("speed is 70km/h")

# obj=Maruti()
# obj.show()
# obj.speed()

#create object of Sujuki
# obj2=Suzuki()
# obj2.show()
# obj2.speed()















