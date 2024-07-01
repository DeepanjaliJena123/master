#OOPS:
# Python, like every other object-oriented language, allows you to define classes to create objects
# OOPs Concepts in Python
# Class
# Objects
# Polymorphism
# Encapsulation
# Inheritance
# Data Abstraction

##_init_
#It is run as soon as an object of a class is instantiated.
# The method is useful to do any initialization you want to do with your object.

#orr:
# The init method in python is a special method used in the process of initializing an object.
# When you create a new instance of a class,
# the init method is automatically called. It simply initialize the class object.

#
#Class attributes are shared by all instances of the class.
#__init__ is a special method (constructor) that initializes an instance of the class
#It takes two parameters:
#1:self (referring to the instance being created)
# The self is used to represent the instance of the class.
# With this keyword, you can access the attributes and methods of the class in python.
# It binds the attributes with the given arguments.

#2:name (representing the name of the class name)
#
##__init__ method is called for each instance to initialize their name attributes with the provided names.

#exa1
# __init__ method in Python is used to initialize objects of a class. It is also called a constructor.

#self :
# In Python, self is a convention used to represent the instance of the class in methods and attributes.
# It is the first parameter of any method in a class and refers to the instance of the class itself.
# When you call a method on an instance of a class, the instance is automatically passed to the method as the first parameter (usually named self).


# What is the use of self and init in Python?
# Python __init__:
# The python __init__ method is declared within a class and is used to initialize the attributes of an object as soon as the object is formed.
# While giving the definition for an __init__(self) method, a default parameter, named 'self' is always passed in its argument.
# This self represents the object of the class itself.

#exa1
# class mynumber:
#     def __init__(self,value):
#         self.value=value
#
#     def print_mynumber(self):
#         print(self.value)
#
# obj=mynumber(30)
# obj.print_mynumber()

# In the example above, self is used in the __init__ method to refer to the instance being created, and
# it is used again in the print_value method to refer to the instance on which the method is called (obj in this case).
#
# Using self allows you to access and modify attributes of the instance within the methods of the class.
# It helps differentiate between instance variables and local variables within the class methods.


#exa2:

# class Subject:
#     def __init__(self,attr1,attr2):
#         self.attr1=attr1
#         self.attr2=attr2
#
# obj=Subject("MATH","SCIENCE")
# print(obj.attr2)
# print(obj.attr1)

#exa2: Self: Pointer to Current Object

# class check:
#     def __init__(self):
#         print("the adress of self=",id(self))
#
# obj=check()
# print("adress of class=",id(obj))

#exa3:Example: Creating Class with Attributes and Methods

# class car:
#     def __init__(self,model,color):
#         self.model=model
#         self.color=color
#
#     def show(self):
#         print("The model is", self.model)
#         print("The color is", self.color)
#
# audi=car('audi 4',"blue")
# farrari=car("farrari","green")
#
# audi.show()
# farrari.show()
#
# print("model for audi is",audi.model)
# print("model for farrari is",farrari.model)
#

# ####### Constructors in Python
# constructors is to initialize(assign values) to the data members of the class when an object of the class is created
#the __init__() method is called the constructor and is always called when an object is created.

# Types of constructors :
# 1.default constructor: The default constructor is a simple constructor which doesn’t accept any arguments.
# Its definition has only one argument which is a reference to the instance being constructed.

# 2.parameterized constructor: constructor with parameters is known as parameterized constructor.
# The parameterized constructor takes its first argument as a reference
# to the instance being constructed known as self and the rest of the arguments are provided by the programmer.
#
#Example of default constructor :

# class geekforgeeks:
#     def __init__(self):
#         self.geek="geekforpython"
#
#     def geek_print(self):
#         print(self.geek)
#
# obj=geekforgeeks()
# obj.geek_print()

# Example of the parameterized constructor :

# class addition:
#     first=0
#     second=0
#     ans=0
#
#     def __init__(self,s,f):
#         self.first=s
#         self.second=f
#
#     def display(self):
#         print("the first number is = "+str(self.first))
#         print("the second number is = "+str(self.second))
#         print("addition of two number is = "+str(self.ans))
#
#     def calculate(self):
#         self.ans=self.first+self.second
#
# obj=addition(10,30)
# obj.display()
# obj.calculate()                                                         #doubt,call calculate
#

#exa
# class Myclass:
#     def __init__(self,name=None):
#         if name is None:
#             print("default constructer called")
#         else:
#             self.name=name
#             print("parameterized constructer called with name",self.name)
#
#     def method(self):
#         if hasattr(self,"name"):
#             print("method called with name",self.name)
#         else:
#             print("method called without a name")
#
# obj=Myclass()
# obj.method()
#
# obj2=Myclass("deepa")
# obj2.method()


##init
#ex
# class Person:
#     def __init__(self,name):
#         self.name=name
#
#     def say_hi(self):
#         print("hello, my name is ",self.name)
#
# obj=Person("nikhil")
# obj.say_hi()
#
# #creating different object
# obj2=Person("shyam")
# obj3=Person("ram")
# obj2.say_hi()
# obj3.say_hi()


#exa2:######## Inheritance
# Benefits of inheritance are:
#
# Inheritance allows you to inherit the properties of a class,
# i.e., base class to another, i.e., derived class. The benefits of Inheritance in Python are as follows:
#
# It represents real-world relationships well.
# It provides the reusability of a code. We don’t have to write the same code again and again. Also,
# it allows us to add more features to a class without modifying it.
# It is transitive in nature, which means that if class B inherits from another class A,
# then all the subclasses of B would automatically inherit from class A.
# Inheritance offers a simple, understandable model structure.
# Less development and maintenance expenses result from an inheritance.

#exa creating parent class

# class Person:
#     def __init__(self,name,id):
#         self.name=name
#         self.id=id
#
#     def display(self):
#         print(self.name,self.id)
#
# emp=Person("nitesh",102)
# emp.display()
#
# #exa creating child class
#
# class Emp(Person):
#     def Print(self):
#         print("emp class called")
#
# emp_details=Emp("MAYANK",103)
#
# emp_details.display()
#
# emp_details.Print()

# #exa
#
# class Person:
#     def __init__(self,name):
#         self.name=name
#
#     def gatAname(self):
#         return self.name
#     def isemployee(self):
#         return False
# class Employee(Person):
#     def isemployee(self):
#         return True
#
# obj=Employee("JOHN")
#
# print(obj.gatAname())
# print(obj.isemployee())
#
# obj2=Person("nikhil")
# print(obj2.gatAname())
# print(obj2.isemployee())


#exa
# class Person:
#     def __init__(self,name,idnumber):
#         self.name=name
#         self.idnumber=idnumber
#
#     def display(self):
#         print(self.name)
#         print(self.idnumber)
#
# class Employee(Person):
#     def __init__(self,name,idnumber,salary,post):
#         self.salary=salary
#         self.post=post
#
#         Person.__init__(self,name,idnumber)
#
# a=Employee("rahul",103,50000, "manager")
# print(a.display())


#exa:Python program to demonstrate error if we forget to invoke __init__() of the parent

# class A:
#     def __init__(self, n):
#         self.name=n
# class B(A):
#     def __init__(self,n,roll):
#         self.roll=roll
#
#         # A.__init__(self, n)
#
# obj=B(102,"k")
# print(obj.roll)
# print(obj.name)


###  The super() Function
# The super() function is used to give access to methods and properties of a parent or sibling class.
# The super() function returns an object that represents the parent class.
#
#exa
# class Person():
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#
#     def display(self):
#         print(self.name,self.age)
#
# class Student(Person):
#     def __init__(self,name,age):
#         self.sname=name
#         self.sage=age
#
#         super().__init__("rahul",age)
#
#     def displayinfo(self):
#         print(self.sname,self.sage)
#
#
# obj=Student("mayank",25)
#
# print(obj.display())
# print(obj.displayinfo())

#Different types of Python Inheritance
# There are 5 different types of inheritance in Python. They are as follows:
#
# Single inheritance: When a child class inherits from only one parent class, it is called single inheritance.
# Multiple inheritances: When a child class inherits from multiple parent classes, it is called multiple inheritances.


#exa
# class Base1:
#     def __init__(self):
#         self.str1="geek1"
#         print("Base1")
# class Base2:
#     def __init__(self):
#         self.str2="geek2"
#         print("Base2")
#
# class Derived(Base1,Base2):
#     def __init__(self):
#
#         Base1.__init__(self)
#         Base2.__init__(self)
#         print("Derived")
#     def printstr(self):
#         print(self.str1,self.str2)
#
# obj=Derived()
# obj.printstr()

#exa
# class Parent:
#     def fun1(self):
#         print("parent class")
# class child(Parent):
#     def fun2(self):
#         print("child class")
#
# obj=child()
# obj.fun2()
# obj.fun1()

##Multilevel inheritance: When we have a child and grandchild relationship.
# This means that a child class will inherit from its parent class, which in turn is inheriting from its parent class.

#exa:
# class Base:
#     def __init__(self,name):
#         self.name=name
#
#     def getname(self):
#         return self.name
#
# class Child(Base):
#     def __init__(self,name,age):
#         self.age=age
#         Base.__init__(self,name)
#
#     def getAge(self):
#         return self.age
#
# class grandchild(Child):
#     def __init__(self,name,age,address):
#         self.address=address
#         Child.__init__(self,name,age)
#
#     def getadress(self):
#         return self.address
#
# obj=grandchild("geek1",23,"noida")
# print(obj.getname(),obj.getAge(),obj.getadress())

#exa
# class Mother:
#     mothername=""
#
#     def mother(self):
#         print(self.mothername)
#
# class Father():
#     fathernem=""
#     def father(self):
#         print(self.fathernem)
#
# class Son(Mother,Father):
#     def parents(self):
#         print(self.fathernem)
#         print(self.mothername)
#
# s1=Son()
# s1.fathernem="ram"
# s1.mothername="sita"
# s1.parents()

# ## Multilevel Inheritance :

# Hierarchical Inheritance:
# When more than one derived class are created from a single base this type of inheritance is called hierarchical inheritance.

# we have a parent (base) class and two child (derived) classes.

# class Parent:
#     def fun1(self):
#         print("parent class")
#
# class child1(Parent):
#     def fun2(self):
#         print("child class")
#
# class child2(Parent):
#     def fun3(self):
#         print("child3")
#
# obj=child1()
# obj.fun1()
# obj.fun2()
#
# obj2=child2
# obj2.fun3


#Hybrid Inheritance:
# Inheritance consisting of multiple types of inheritance is called hybrid inheritance

#exa

# class School:
#     def fun1(self):
#         print("shc")
# class student(School):
#     def fun2(self):
#         print("student")
# class student2(School):
#     def fun3(self):
#         print("student2")
# class student3(student,School):
#     def fun4(self):
#         print("student3")
#
# obj=student3()
# obj.fun4()
# obj.fun1()
# obj.fun2()


# Private members of the parent class
# We don’t always want the instance variables of the parent class to be inherited by the child class i.e.
# we can make some of the instance variables of the parent class private, which won’t be available to the child class.

#exa
# class C():
#     def __init__(self):
#         self.c=21
#         self.__d=42
#
# class D(C):
#     def __init__(self):
#         self.e=60
#         C.__init__(self)
#
# obj=D()
# print(obj.c)
# # produces an error as d is private instance variable
# print(obj.__d)


# #########    Encapsulation in Python
#binding of methods and variables in single unit.

# class Base:
#     def __init__(self):
#         self._a=2
# class Derived(Base):
#     def __init__(self):
#         Base.__init__(self)
#         print("derived",self._a)
#
#         self._a=3
#         print("modified",self._a)
#
# obj=Derived()
# obj2=Base()
#
# print(obj._a)
# print(obj2._a)


#Polymorphism:
### polymorphisms refer to the occurrence of something in multiple forms.
#As part of polymorphism, a Python child class has methods with the same name as a parent class method.

#polymorphism means having many forms.
# In programming, polymorphism means the same function name (but different signatures) being used for different types

#exa
# print(len("geeks"))
# print(len([10,20,30]))
#

# Examples of user-defined polymorphic functions:
# def add(x,y,z=0):
#     return x+y+z
#
# print(add(2,3))
# print(add(2,3,4))
#

#exa
# class India():
#     def capital(self):
#         print("delhi is capital")
#     def language(self):
#         print("hindi")
#     def typ(self):
#         print("developed country")
#
# class USA():
#     def capital(self):
#         print("WASHINGTON is capital")
#     def language(self):
#         print("ENGLISH")
#     def typ(self):
#         print("developed country")
#
# obj1=India()
# obj2=USA()
# for country in (obj1,obj2):
#     country.capital()
#     country.language()
#     country.typ()


#Encapsulation
# class Base:
#     def __init__(self):
#         self._a=2
#
# class derived(Base):
#     def __init__(self):
#         Base.__init__(self)
#         print("calling the protected member base class",self._a)
#
#         self._a=4
#         print("modified protected memeber outside of class",self._a)
#
# obj1=derived()
# obj2=Base()
#
# print(obj1._a)
# print(obj2._a)

#####  Private members
# private should neither be accessed outside the class nor by any base class.
# Private instance variables that cannot be accessed except inside a class.












