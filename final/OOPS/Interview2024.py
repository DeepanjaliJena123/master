## OOPS EXAMPLE
#Polymorphism
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


###single inheritance
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
# obj.get("java")

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

