## MRO(Method Resolution Order)::
#when multiple inheritance is done,so the class followed by left to right is considered
#class A,class B is inheritted in class c like,class C(A,B)
# class A:
#     def say_hi(self):
#         print("hi a")
#
# class B:
#     def say_hi(self):
#         print("hi b")
# class C(B,A):
#     pass
#
# obj=C()
# obj.say_hi()


# #class n object
# class Dog:
#     attr1="mammal"
#     attr2="dog"
#     def fun(self):
#         print("i am a",self.attr1)
#         print("i am a ",self.attr2)
# obj=Dog()
# # obj.fun()
# print(obj.attr1)
#self parameter
# class GFG:
#     def __init__(self,name,company):
#         self.company=company
#         self.name=name
#
#     def show(self):
#         print("hello my name is "+ self.name + " and i am working in "+ self.company)
#
# obj=GFG("DEEPA","APPSTIX")
# obj.show()
# print(obj.company)

################   Polymorphism  #################

#Polymorphism:
### polymorphisms refer to the occurrence of something in multiple forms.
#As part of polymorphism, a Python child class has methods with the same name as a parent class method.

#polymorphism means having many forms.
# In programming, polymorphism means the same function name (but different signatures) being used for different types.
# The key difference is the data types and number of arguments used in function.

#exa1                                           #normal polymorphism
# class India():
#     def capital(self):
#         print("New Delhi is capital of india")
#     def language(self):
#         print("hindi is spoken language of india")
#     def typ(self):
#         print("india is developing country")
#
# class USA():
#     def capital(self):
#         print("WASHINGTON is capital of india")
#
#     def language(self):
#         print("ENGLISH is spoken language of india")
#
#     def typ(self):
#         print("USA is developed country")
# obj_ind=India()
# obj_usa=USA()
#
# for country in (obj_ind,obj_usa):
#     country.capital()
#     country.language()
#     country.typ()

#exa2: Different classes with the same method:                    #polymorphism with init

#
# class Car:
#   def __init__(self, brand, model):
#     self.brand = brand
#     self.model = model
#
#   def move(self):
#     print("Drive!")
#
# class Boat:
#   def __init__(self, brand, model):
#     self.brand = brand
#     self.model = model
#
#   def move(self):
#     print("Sail!")
#
# class Plane:
#   def __init__(self, brand, model):
#     self.brand = brand
#     self.model = model
#
#   def move(self):
#     print("Fly!")
#
# car1 = Car("Ford", "Mustang")       #Create a Car class
# boat1 = Boat("Ibiza", "Touring 20") #Create a Boat class
# plane1 = Plane("Boeing", "747")     #Create a Plane class
#
# for x in (car1, boat1, plane1):
#   x.move()

#Inheritance Class Polymorphism
# class Vehicle:
#   def __init__(self, brand, model):
#     self.brand = brand
#     self.model = model
#
#   def move(self):
#     print("Move!")
#
# class Car(Vehicle):
#   pass
#
# class Boat(Vehicle):
#   def move(self):
#     print("Sail!")
#
# class Plane(Vehicle):
#   def move(self):
#     print("Fly!")
#
#
# car1 = Car("Ford", "Mustang") #Create a Car object
# boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
# plane1 = Plane("Boeing", "747") #Create a Plane object
#
# for x in (car1, boat1, plane1):
#   print(x.brand)
#   print(x.model)
#   x.move()


#exa:: using inheritance and method overriding:                               doubt
# class Animal:
#     def speak(self):
#         raise NotImplementedError("Subclass must implement this method")
#
#
# class Dog(Animal):
#     def speak(self):
#         return "Woof!"
#
#
# class Cat(Animal):
#     def speak(self):
#         return "Meow!"
#
#
# # Create a list of Animal objects
# animals = [Dog(), Cat()]
#
# # Call the speak method on each object
# for animal in animals:
#     print(animal.speak())
#
# class Animals:
#     def speak(self):
#         raise NotImplementedError("subclass must implement of this")
#
# class Dog(Animals):
#     def speak(self):
#         print("woof")
# class Cat(Animals):
#     def speak(self):
#         print("meow")
# animals=[Dog(),Cat()]
#
# for i in animals:
#     i.speak()


######### init ########
#constructer: all classes have a function called --init--(),
#which is always executed when the object is being initiated.

#__init__ method in Python is used to initialize objects of a class. It is also called a constructor.



# What is the use of self and init in Python?
# Python __init__:
# The python __init__ method is declared within a class and is used to initialize the attributes of an object as soon as the object is formed.
# While giving the definition for an __init__(self) method, a default parameter, named 'self' is always passed in its argument.
# This self represents the object of the class itself.

#exa:
# class Person:
#     def __init__(self,name):
#         self.name=name
#
#     def say_hi(self):
#         print("my name is ",self.name)
#
# obj=Person("Nikhil")
# obj.say_hi()
# print(obj.name)

# __init__ Method with Inheritance

# class A:
#     def __init__(self,something1):
#         self.something=something1
#         print("A init called:",something1)
# class B(A):
#     def get(self,something1):
#         A.__init__(self,something1)
#         self.something = something1
#         print("B init called:",self.something)
#
# obj=B("something")
# obj.get("hi")
# # obj.something

# class A:
#     def __init__(self,name):
#         self.n=name
#         print("A init called :",name)
# class B(A):
#     def get(self,name):
#         A.__init__(self,name)
#         self.k=name
#         print("B init called:",self.k)
# obj=B("Python")
# obj.get("java")                                            doubt


########## SUPER ##################
###  The super() Function
# The super() function is used to give access to methods and properties of a parent or sibling class.
# The super() function returns an object that represents the parent class.
#

#EXA
# class EMP():
#     def __init__(self,id,name,add):
#         self.id=id
#         self.name=name
#         self.add=add
#
# class Freelance(EMP):
#     def __init__(self,id,name,add,emails):
#         self.emails=emails
#         super().__init__(id,name,add)
#
# obj=Freelance(103,"John","Noida","kkk@gmail.com")
# print(obj.emails)
# print(obj.id)

# class EMP():
#     def __init__(self,id,name,add):
#         self.idddd=id
#         self.nameeee=name
#         self.addddd=add
# class Freelance(EMP):
#     def __init__(self,id,name,add,emails):
#         self.emailsssssss=emails
#         super().__init__(id,name,add)
#
# obj=Freelance(123,"JOHN","NOIDA","john123@gmail.com")
# print(obj.idddd)
# print(obj.emailsssssss)

############# Inheritance ##################

#Different types of Python Inheritance
# There are 5 different types of inheritance in Python. They are as follows:
#
# Single inheritance: When a child class inherits from only one parent class, it is called single inheritance.
# Multiple inheritances: When a child class inherits from multiple parent classes, it is called multiple inheritances.

#exa:# Single inheritance:
#parent
# class Parent():
#     def __init__(self,name,id):
#         self.name=name
#         self.id=id
#
#     def display(self):
#         print(self.name,self.id)
#
# #child
# class Child(Parent):
#     def Print(self):
#         print("child class called")
#
# obj=Child("Rohan",103)
# obj.display()
# obj.Print()

#or
# class Parent:
#     def func1(self):
#         print("this function is in parent class")
#
# class Child(Parent):
#     def func2(self):
#         print("this function is in Child class")
#
# obj=Child()
# obj.func1()
# obj.func2()

#exa:Subclassing (Calling constructor of parent class) Single inheritance: with init
# class Person():
#     def __init__(self,name,id):
#         self.name=name
#         self.id=id
#     def dispaly(self):
#         print(self.name)
#         print(self.id)
# class Employee(Person):
#     def __init__(self,name,id,salary,post):
#         self.salary=salary
#         self.post=post
#
#         Person.__init__(self,name,id)
#
# obj=Employee("John",103,30000,"Eng")
# obj.dispaly()
#

#multiple inheritances.

# class Base1:
#     def __init__(self):
#         self.str1="geek1"
#         print(self.str1)
# class Base2:
#     def __init__(self):
#         self.str2="geek"
#         print(self.str2)
# class Derived(Base1,Base2):
#     def __init__(self):
#         Base1.__init__(self)
#         Base2.__init__(self)
#         print("derived class")
#     def print(self):
#         print(self.str1,self.str2)
#
# Multilevel inheritance:
#
# class Base(object):
#
#     # Constructor
#     def __init__(self, name):
#         self.name = name
#
#     # To get name
#     def getName(self):
#         return self.name
#
#
# # Inherited or Sub class (Note Person in bracket)
# class Child(Base):
#
#     # Constructor
#     def __init__(self, name, age):
#         Base.__init__(self, name)
#         self.age = age
#
#     # To get name
#     def getAge(self):
#         return self.age
#
#
# # Inherited or Sub class (Note Person in bracket)
#
#
# class GrandChild(Child):
#
#     # Constructor
#     def __init__(self, name, age, address):
#         Child.__init__(self, name, age)
#         self.address = address
#
#     # To get address
#     def getAddress(self):
#         return self.address
#
#
# # Driver code
# g = GrandChild("Geek1", 23, "Noida")
# print(g.getName(), g.getAge(), g.getAddress())
#

########   single inheritance:
# Single inheritance enables a derived class to inherit properties from a single parent class, thus enabling code reusability
# and the addition of new features to existing code

# class Parent:
#     def func1(self):
#         print("this function is in parent class")
# class Child(Parent):
#     def func2(self):
#         print("this function is in child class")
#
# obj=Child()
# obj.func2()
# obj.func1()

# #######  Multilevel Inheritance:
#
# class Base:
#     def __init__(self,name):
#         self.name=name
#     def getname(self):
#         return self.name
#
# class Child(Base):
#     def __init__(self,name,age):
#         self.age=age
#         Base.__init__(self,name)
#     def getage(self):
#         return self.age
#
# class Grandchild(Child):
#     def __init__(self,name,age,adress):
#         self.adress=adress
#         Child.__init__(self,name,age)
#     def getadress(self):
#         return self.adress
#
# obj=Grandchild("john",28,"Banglore")
# print(obj.name,obj.age,obj.adress)

# Multiple Inheritance:
# When a class can be derived from more than one base class this type of inheritance is called multiple inheritances.
# #exa
# class Base1:
#     def __init__(self):
#         self.str1="geek1"
#         print(self.str1)
# class Base2:
#     def __init__(self):
#         self.str2="geek"
#         print(self.str2)
# class Derived(Base1,Base2):
#     def __init__(self):
#         Base1.__init__(self)
#         Base2.__init__(self)
#         print("derived class")
#     def print(self):
#         print(self.str1,self.str2)

#exa
# class Mother:
#     mothername=""
#     def mother(self):
#         print(self.mothername)
# class Father:
#     fathername=""
#     def father(self):
#         print(self.fathername)
# class Son(Mother,Father):
#     def parents(self):
#         print("Father : ",self.mothername)
#         print("Mother : ",self.fathername)
# obj=Son()
# obj.fathername="Ram"
# obj.mothername="sita"
# obj.parents()


# #####  Hierarchical Inheritance:
# # When more than one derived class are created from a single base this type of inheritance is called hierarchical inheritance.
#
# class Parent:
#     def func1(self):
#         print("This function is in parent class")
# class Child1(Parent):
#     def func2(self):
#         print("This function is in child class")
# class Child2(Parent):
#     def func3(self):
#         print("This function is in child2")
# obj1=Child1()
# obj2=Child2()
# obj1.func1()
# obj2.func3()


# Hybrid Inheritance:
# Inheritance consisting of multiple types of inheritance is called hybrid inheritance.

# class School:
#     def func1(self):
#         print("this function is in school")
# class Student1(School):
#     def fun2(self):
#         print("this function is in student1")
# class student2(School):
#     def func3(self):
#         print("this function is in student2")
#
# class Student3(Student1,School):
#     def fun4(self):
#         print("this function is in student3")
#
# obj=Student3()
# obj.fun4()
# obj.func1()
# obj.fun2()


#############  Encapsulation  ############
# Private members of the parent class
# We don’t always want the instance variables of the parent class to be inherited by the child class i.e.
# we can make some of the instance variables of the parent class private, which won’t be available to the child class.

#Conceptual implimentations in python
#Private attributes and methods are meant to be used only within the class and are not accessible from outside the class.


# class Base:
#     def __init__(self):
#         self._a=2
#
# class Derived(Base):
#     def __init__(self):
#         Base.__init__(self)
#         print("calling protected member of base class: ",self._a)
#
#         self._a=4
#         print("callling modified protected member : ",self._a)
#
# obj=Derived()


# ####  Private members
#private should neither be accessed outside the class nor by any base class.

# class Base:
#     def __init__(self):
#         self.a="geek"
#         self.__a="geekforgeeks"
# class Derived(Base):
#     def __init__(self):
#         Base.__init__(self)
#         print("calling private member of base class")
#         # print(self.__a)
# obj=Derived()
# print(obj.a)

# class A:
#     def __init__(self):
#         self._a="geek"
#         self.__a="python"
#     def display(self):                    #Access private member in outside of class using method
#         print("print __a :",self.__a)
#
# class B(A):
#     def __init__(self):
#         A.__init__(self)
#         print("calling protected member :",self._a)
#         # print("calling private member :",self.__a)
#
# obj=B()
# obj.display()



##### Access private member in outside of class
#exa
# class Account:
#     def __init__(self,acc_no,acc_pass):
#         self.acc_no=acc_no
#         self.__acc_pass=acc_pass
#
#     def reset_pass(self):
#         print(self.__acc_pass)
#
# obj=Account("12345","abcd")
# print(obj.acc_no)
# obj.reset_pass()

#
# class Person:
#     __name="abc"
#
# obj=Person()
# print(obj.__name)       #####error ,cant call private member

#or
# class Person:
#     __name = "abc"
#     def __hello():
#         print("hello person")

# obj=Person()
# # print(obj.__name)
# obj.__hello             #error.cant access private method or atrribute

#or can call using methods
# class Person:
#     __name = "abc"
#
#     def __hello(self):
#         print("hello person")
#     def welcome(self):
#         self.__hello()
#
# obj=Person()
# # print(obj.__name)
# print(obj.welcome())

#########  Polymorphism   ######
# The word polymorphism means having many forms. In programming,
# polymorphism means the same function name (but different signatures) being used for different types.
# The key difference is the data types and number of arguments used in function.

#or
#when the same operator is allowed to have different meaning according to the context.

# class Complex:
#     def __init__(self,real,img):
#         self.real=real
#         self.img=img
#     def shownumber(self):
#         print(self.real,"i+",self.img,"j")
#
#     def __add__(self, num2):
#         newreal=self.real+num2.real
#         newimg=self.img+num2.img
#         return Complex(newreal,newimg)
#
#
# num1=Complex(2,4)
# num1.shownumber()
#
# num2=Complex(1,3)
# num2.shownumber()
#
# num3=num1+num2
# num3.shownumber()


#exa
#define a circle to creat with radius r using the constuctor
#and area of the class which calculates the area of the circle
#define parametere 2paye r,which allows to calculate the perimeter of the circle

# class Circle:
#     def __init__(self,radius):
#         self.radius=radius
#     def area(self):
#         return 22/7*self.radius**2
#     def perimeter(self):
#         return 2*(22/7)*self.radius
#
# obj=Circle(21)
# print(obj.area())
# print(obj.perimeter())

#exa
# class Employee():
#     def __init__(self,role,dept,salary):
#         self.role=role
#         self.dept=dept
#         self.salary=salary
#     def showdetails(self):
#         print("role=",self.role)
#         print("dept=",self.dept)
#         print("salary=",self.salary)
# class Engineer(Employee):
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#         super().__init__("Engineer","IT","80000")
#
# obj=Engineer("Mayank",30)
# obj.showdetails()

#exa dunder function

# class Order:
#     def __init__(self,item,price):
#         self.item=item
#         self.price=price
#     def __gt__(self, odr2):
#         return self.price>odr2.price
#
# odr1=Order("chips",20)
# odr2=Order("tea",15)
# print(odr1>odr2)  #True


#exa of geeksandgeeks
#exa1
# print(len("geeks"))
# print(len([10,20,30]))
#
#

#Exa2:
# def add(x,y,z=0):
#     return x+y+z
# print(add(2,3,4))
# print(add(1,2,3))
#

#exa3:

# class India():
#     def capital(self):
#         print("New Delhi is the capital of India.")
#
#     def language(self):
#         print("Hindi is the most widely spoken language of India.")
#
#     def type(self):
#         print("India is a developing country.")
#
#
# class USA():
#     def capital(self):
#         print("Washington, D.C. is the capital of USA.")
#
#     def language(self):
#         print("English is the primary language of USA.")
#
#     def type(self):
#         print("USA is a developed country.")
#
#
# obj_ind = India()
# obj_usa = USA()
# for country in (obj_ind, obj_usa):
#     country.capital()
#     country.language()
#     country.type()

#exa4:
# class India():
#     def capital(self):
#         print("New Delhi is the capital of India.")
#
#     def language(self):
#         print("Hindi is the most widely spoken language of India.")
#
#     def type(self):
#         print("India is a developing country.")
#
#
# class USA():
#     def capital(self):
#         print("Washington, D.C. is the capital of USA.")
#
#     def language(self):
#         print("English is the primary language of USA.")
#
#     def type(self):
#         print("USA is a developed country.")
#
#
# def func(obj):
#     obj.capital()
#     obj.language()
#     obj.type()
#
#
# obj_ind = India()
# obj_usa = USA()
#
# func(obj_ind)
# func(obj_usa)

#exa5:polymorphism in Python using inheritance and method overriding:

# class Animal:
#     def speak(self):
#         raise NotImplementedError("Subclass must implement this method")
#
#
# class Dog(Animal):
#     def speak(self):
#         return "Woof!"
#
#
# class Cat(Animal):
#     def speak(self):
#         return "Meow!"
#
#
# # Create a list of Animal objects
# animals = [Dog(), Cat()]
#
# # Call the speak method on each object
# for animal in animals:
#     print(animal.speak())


###############33
#### Data Abstraction:
## Hiding the implementation details of a class and
#and only showing the essential features of the user.
# class Car:
#     def __init__(self):
#         self.ac=False
#         self.brk=False
#         self.clutch=False
#     def Start(self):
#         self.clutch=True
#         self.ac=True
#         print("Car started")
# obj=Car()
# obj.Start()

#EXA
# class Myclass:
#     __hiddenvariable=0
#
#     def add(self,increment):
#         self.__hiddenvariable+=increment
#         print(self.__hiddenvariable)
# obj=Myclass()
# obj.add(2)
# obj.add(5)                                #doubt





#polymorphism
# class India:
#     def capital(self):
#         print("india is tha capital of india")
#     def language(self):
#         print("hindi is india language")
# class USA:
#     def capital(self):
#         print("washington is capital of india")
#     def language(self):
#         print("english is spoken language")
#
# obj_ind=India()
# obj_usa=USA()
#
# for country in (obj_ind,obj_usa):
#     country.capital()
#     country.language()

##Encapsulation
# class Employee:
#     def __init__(self, name, id, salary):
#         self.name = name
#         self.id = id
#         self.__salary = salary
#
# class emp1(Employee):
#     def __init__(self, name, id, salary):
#         super().__init__(name, id, salary)
#         # print(f"Salary is Rs.{self.__salary}")
#         print(f"Salary is Rs.{self._Employee__salary}")
#
# #
# obj = emp1("JOHN", 123, 50000)

# ##orr
# class Car:
#     def __init__(self, brand, mileage):
#         self.__brand = brand  # Private attribute
#         self.__mileage = mileage  # Private attribute
#
#     def get_brand(self):
#         return self.__brand
#
#     def set_mileage(self, mileage):
#         if mileage >= 0:
#             self.__mileage = mileage
#
#     def get_mileage(self):
#         return self.__mileage
#
# my_car = Car("Toyota", 50000)
# print(my_car.get_brand())  # Accessing private attribute using getter method
# my_car.set_mileage(60000)  # Modifying private attribute using setter method
# print(my_car.get_mileage())  # Accessing private attribute using getter method
#

#
# class A:
#     def Rev_str(self,name):
#         new_str = ""
#         for i in name:
#             new_str = i + new_str
#         return new_str,name
#

# name='python'
# obj=A()
# print(obj.Rev_str(name))
# print(type(obj.Rev_str(name)))

# x=[1,2,3,4,5]
# it=iter(x)
# for i in range(len(x)):
#     print(next(it))

# def abc(n):
#     for i in range(1,n+1):
#         yield i
# a=abc(4)
# print(next(a))
# print(next(a))
# print(next(a))
# #
# from abc import ABC, abstractmethod
# # #Abstract Class
#
# class Bank(ABC):
#    def bank_info(self):
#        print("Welcome to bank")
#    @abstractmethod
#    def interest(self):
#        "Abstarct Method"
#        pass
# #Sub class/ child class of abstract class
# class SBI(Bank):
#    def interest(self):
#        "Implementation of abstract method"
#        print("In sbi bank 5 rupees interest")
# s= SBI()
# s.bank_info ()
# s.interest()                                                          #doubt


# from abc import ABC, abstractmethod

# class Animal(ABC):
#     @abstractmethod
#     def make_sound(self):
#         print("animal")
#
# class Dog(Animal):
#     def make_sound(self):
#         return "Woof!"
#
# class Cat(Animal):
#     def make_sound(self):
#         return "Meow!"
#
# dog = Dog()
# print(dog.make_sound())  # Output: Woof!
#
# cat = Cat()
# print(cat.make_sound())  # Output: Meow!
#

# class Person:
#     __name="abc"
#     def __hello(self):
#         print("hello Person")
#     def welcome(self):
#         self.__hello()
#         print(self.__name)
#
# obj=Person()
# obj.welcome()
# hello Person
# abc

# obj._Person__hello()      #hello Person


####MRO
# class A:
#     def info(self):
#         print("a")
# class B:
#     def info(self):
#         print("b")
# class C(A,B):
#     pass
#
# obj=C()
# obj.info()


#SUPER()
# class EMP:
#     def __init__(self,name,id):
#         self.name=name
#         self.id=id
# class Freelance(EMP):
#     def __init__(self,name,id):
#         super().__init__(name,id)
#
# obj=Freelance("deepa",135)
# print(obj.name)
# print(obj.id)


#single inheritance:
# class Parent:
#     def func1(self):
#         print("this function is in parent class")
# class Child(Parent):
#     def func2(self):
#         print("this function is in Child class")
#
# obj=Child()
# obj.func2()

### multi_level inheritance:
# class Base:
#     def __init__(self,name):
#         self.name=name
#     def getName(self):
#         return self.name
# class Child(Base):
#     def __init__(self,name,age):
#         Base.__init__(self,name)
#         self.age=age
#     def getAge(self):
#         return self.age
# class Grandchild(Child):
#     def __init__(self,name,age,adress):
#         Child.__init__(self,name,age)
#         self.adress=adress
#     def getAdress(self):
#         return self.adress
#
# obj=Grandchild("geek",25,"noida")
# print(obj.getName(),obj.getAge(),obj.getAdress())

#multiple inheritance
# class Base1:
#     def __init__(self):
#         self.str1="geek"
#         print(self.str1)
# class Base2:
#     def __init__(self):
#         self.str2="python"
#         print(self.str2)
# class Derived(Base1,Base2):
#     def __init__(self):
#         Base1.__init__(self)
#         Base2.__init__(self)
#         print("derived class")
#         print(self.str1,self.str2)
# obj=Derived()

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


#
# def add(num1: int, num2: int) -> int:
#     """Add two numbers"""
#     num3 = num1 + num2
#
#     return num3
#
# # # Driver code
# # num1, num2 = 5, 15
# # print(add(num1, num2))
#
# print(add(2,5))


############################### #################### 19-May prac
#polymorphism
# class India():
#     def capital(self):
#         print("new delhi is capital of India")
#     def language(self):
#         print("hindi is spoken language")
#     def typ(self):
#         print("India is a developing country")
# class USA():
#     def capital(self):
#         print("wasignton is capital of USA")
#     def language(self):
#         print("English is a spoken language")
#     def typ(self):
#         print("USA is a developed country")
#
#
# obj_ind=India()
# obj_usa=USA()
#
# for counry in (obj_ind,obj_usa):
#     counry.capital()
#     counry.language()
#     counry.typ()


#exa2:
# class Car:
#     def __init__(self,brand,model):
#         self.brand=brand
#         self.model=model
#     def move(self):
#         print("Drive")
# class Boat:
#     def __init__(self,brand,model):
#         self.brand=brand
#         self.model=model
#     def move(self):
#         print("sail")
# class Plane:
#     def __init__(self,brand,model):
#         self.brand=brand
#         self.model=model
#     def move(self):
#         print("fly")
#
# car=Car("FORD","X")
# boat=Boat("IZA","KDH")
# plane=Plane("INDIGO","KSDJ123")
#
# for i in (car,boat,plane):
#     i.move()
#

#self:: “self” refers to the instance of the class
# class Mynumber:
#     def __init__(self,value):
#         self.value=value
#     def print_value(self):
#         print(self.value)
# obj=Mynumber(17)
# obj.print_value()
#

#exa
# class Subject:
#     def __init__(self,attr1,attr2):
#         self.attr1=attr1
#         self.attr2=attr2
#
# obj=Subject("science","math")
# print(obj.attr1)
# print(obj.attr2)

##

# class check:
#     def __init__(self):
#         print("adress of self",id(self))
#
# obj=check()
# print(id(obj))
#
#
# ##
# class Person:
#     def __init__(self,name):
#         self.name=name
#     def say_hi(self):
#         print("my name is ",self.name)
#
# p=Person("NIKHIL")
# p.say_hi()
#

#INIT
# class A():
#     def __init__(self,something):
#         print("A init called")
#         self.something=something
#
# class B(A):
#     def __init__(self,something):
#         A.__init__(self,something)
#         print("B init called")
#         self.something= something
#
# obj=B("SOMETHING")                          #doubt

#
# class Person():
#     def __init__(self,name,id):
#         self.name=name
#         self.id=id
#     def Display(self):
#         print(self.name,self.id)
#
# obj=Person("john",123)
# print(obj.Display())


# class Person():
#     def __init__(self,name):
#         self.name=name
#     def getName(self):
#         return self.name
#     def isemployee(self):
#         return False
#
# class Employee(Person):
#     def isemployee(self):
#         return True
#
# emp=Person("geek1")
# print(emp.getName(),emp.isemployee())
#

###
# class Person():
#     def __init__(self,name,idnumber):
#         self.name=name
#         self.idnumber=idnumber
#     def display(self):
#         print(self.name)
#         print(self.idnumber)
#
# class Employe(Person):
#     def __init__(self,name,idnumber,salary,post):
#         self.salary=salary
#         self.post=post
#
#         Person.__init__(self,name,idnumber)
#
#
# obj=Employe('Rahul',123,201,56)
# obj.display()
#
#
# class A:
#     def __init__(self, n='Rahul'):
#         self.name = n
#
#
# class B(A):
#     def __init__(self, roll):
#         self.roll = roll
#
#
# object = B(23)
# print(object.name)          #doubt

# class Person():
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def display(self):
#         print(self.name,self.age)
# class Student():
#     def __init__(self,name,age):
#         self.sname=name
#         self.sage=age
#
#         super().__init__("rahul",age)
#     def displayinfo(self):
#         print(self.sname,self.sage)
#
# obj=Student("mayank",23)
# obj.display()
# obj.displayinfo()
#

# class Person():
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def display(self):
#         print(self.name, self.age)
#
#
# # child class
# class Student(Person):
#     def __init__(self, name, age):
#         self.sName = name
#         self.sAge = age
#         # inheriting the properties of parent class
#         super().__init__("Rahul", age)
#
#     def displayInfo(self):
#         print(self.sName, self.sAge)
#
#
# obj = Student("Mayank", 23)
# obj.display()
# obj.displayInfo()
#

# class Person():
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def display(self):
#         print(self.name,self.age)
#
# class Student(Person):
#     def __init__(self,name,age,dob):
#         self.sname=name
#         self.sage=age
#         self.dob=dob
#         super().__init__("rahul",age)
#
#     def displayinfo(self):
#         print(self.sname,self.sage,self.dob)
#
# obj=Student("Mayank",23,"16-03-2000")
# obj.display()
# obj.displayinfo()
#

#multiple inheritance
# class Base1():
#     def __init__(self):
#         self.str1="geek1"
#         print("Base1")
#
# class Base2():
#     def __init__(self):
#         self.str2="geek2"
#         print("base2")
#
# class Derived(Base1,Base2):
#     def __init__(self):
#         Base1.__init__(self)
#         Base2.__init__(self)
#         print("derived")
#     def printstr(self):
#         print(self.str1,self.str2)
#
# obj=Derived()
# obj.printstr()
#
#
# multilevel inheritance
# class Base():
#     def __init__(self,name):
#         self.name=name
#     def getname(self):
#         return self.name
# class Child(Base):
#     def __init__(self,name,age):
#         self.age=age
#         Base.__init__(self,name)
#
#     def getage(self):
#         return self.age
#
# class Grandchild(Child):
#     def __init__(self,name,age,adress):
#         self.adress=adress
#         Child.__init__(self,name,age)
#
#     def getadress(self):
#         return self.adress
#
# obj=Grandchild("Rohan",30,"Banglore")
# print(obj.name,obj.age,obj.adress)
#
#

# class C():
#     def __init__(self):
#         self.c=21
#         self.__d=45
#
# class D(C):
#     def __init__(self):
#         self.e=84
#         C.__init__(self)
#
# obj=D()
# print(obj.c)      #21
# print(obj.e)       #84
# print(obj.__d)       #AttributeError: 'D' object has no attribute '__d'


##single inheritance
# class Parent:
#     def func1(self):
#         print("this is parent class")
# class Child(Parent):
#     def func2(self):
#         print("this child class")
#
# obj=Child()
# obj.func1()
# obj.func2()

#multiple inheritance
# class Mother:
#     mothername=""
#
#     def mothername(self):
#         print(self.mothername)
#
# class Father:
#     fathername=""
#
#     def fathername(self):
#         print(self.fathername)
#
# class Son(Mother,Father):
#     def parents(self):
#         print(self.fathername)
#         print(self.mothername)
#
# obj=Son()
# obj.fathername="Ram"
# obj.mothername="sita"
# obj.parents()

#multi_level inheritance
# class Grandfather():
#     def __init__(self,gdname):
#         self.gdname=gdname
#
# class Father(Grandfather):
#     def __init__(self,gdname,fname):
#         self.fname=fname
#         Grandfather.__init__(self,gdname)
#
# class Son(Father):
#     def __init__(self,gdname,fname,sname):
#         self.sname=sname
#         Father.__init__(self,gdname,fname)
#
#     def print_name(self):
#         print(self.gdname)
#         print(self.fname)
#         print(self.sname)
#
# obj=Son("Nityam","Soyam","Nitosh")
# print(obj.print_name())

#Hierarchical Inheritance:
# class Parent:
#     def func1(self):
#         print("this is parent class")
#
# class Child1(Parent):
#     def func2(self):
#         print("this is child1 class")
#
# class Child2(Parent):
#     def func3(self):
#         print("this is child2 class")
#
#
# obj1=Child2()
# obj1.func1()
#
# obj2=Child1()
# obj2.func2()
# obj2.func1()

#Hybrid Inheritance:
# class School():
#     def func1(self):
#         print("This function is from school")
#
# class Student1(School):
#     def func2(self):
#         print("this is from student1 class")
#
# class Student2(School):
#     def func3(self):
#         print("this is from Student2 class")
#
# class Student3(Student1,School):
#     def func4(self):
#         print("this is from student3")
#
# obj1=Student1()
# obj1.func2()
#
# obj2=Student3()
# obj2.func4()
# obj2.func1()


# ###Encapsulation:
# #PROTECTED
# class Base:
#     def __init__(self):
#         self._a=22
#
# class Derived(Base):
#     def __init__(self):
#         Base.__init__(self)
#         print("calling preteced memeber :",self._a)
#
#         self._a=30
#         print("modified proteced member :",self._a)
#
# obj=Derived()
# print(obj._a)

#private member
# class Base:
#     def __init__(self):
#         self.a="geek"
#         self.__c="python"
#
# class Derived(Base):
#     def __init__(self):
#         Base.__init__(self)
#         print("print private member ")
#         print(self.__c)
#
# obj=Derived()


# class A:
#     def __init__(self,name):
#         self.__name=name
#
#     def printname(self):
#         return self.__name
#
# class B(A):
#     def __init__(self,name,age):
#         self.age=age
#         A.__init__(self,name)
#
#     def info(self):
#         print("calling private member :",self.__name)
# obj=B("MAMA",123)
# # print(obj.printname())
# print(obj._A__name)   #CALLING PRIVATE MEMBER



# class Tree:
#    def __init__(self, height):
#        self.__height = height
#
#    def get_height(self):
#        return self.__height
#
#    def set_height(self, new_height):
#        if not isinstance(new_height, int):
#            raise TypeError("Tree height must be an integer")
#        if 0 < new_height <= 40:
#            self.__height = new_height
#        else:
#            raise ValueError("Invalid height for a pine tree")
#
#
# pine = Tree(20)
# print(pine.get_height())             #doubt
#


# Using @property decorator in Python classes
# We introduce a new technique — creating properties for attributes:


# class Tree:
#    def __init__(self, height):
#        # First, create a private or protected attribute
#        self.__height = height
#
#    @property
#    def height(self):
#        return self.__height
#
# pine = Tree(17)
# print(pine.height)           doubt
#


#protected example
# # illustrating protected members & protected access modifier
# class details:
#     _name = "Jason"
#     _age = 35
#     _job = "Developer"
#
#
# class pro_mod(details):
#     def __init__(self):
#         print(self._name)
#         print(self._age)
#         print(self._job)
#
#
# # creating object of the class
# obj = pro_mod()
#
#

#private examples
# # illustrating private members & private access modifier
# class Rectangle:
#     __length = 0  # private variable
#     __breadth = 0  # private variable
#
#     def __init__(self):
#         # constructor
#         self.__length = 5
#         self.__breadth = 3
#         # printing values of the private variable within the class
#         print(self.__length)
#         print(self.__breadth)
#
# rect = Rectangle()  # object created
# # printing values of the private variable outside the class
# # print(rect.length)  #AttributeError: 'Rectangle' object has no attribute '__length'
# # print(rect.breadth) #AttributeError: 'Rectangle' object has no attribute '__length'


# Example: Access private member
#
# class Employee:
#     # constructor
#     def __init__(self, name, salary):
#         # public data member
#         self.name = name
#         # private member
#         self.__salary = salary
#
# # creating object of a class
# emp = Employee('Jessa', 10000)
#
# print('Name:', emp.name)
# # direct access to private member using name mangling
# print('Salary:', emp._Employee__salary)