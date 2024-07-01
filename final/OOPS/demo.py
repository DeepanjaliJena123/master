#1:polymorphism: if the the multiple class having same mathods function name
# class India():
#     def capital(self):
#         print("New delhi is capital of India")
#     def language(self):
#         print("Hindi is india language")
#     def typ(self):
#         print("India is developing country")
#
# class USA():
#     def capital(self):
#         print("Washington is capital of USA")
#     def language(self):
#         print("English is language")
#     def typ(self):
#         print("USA is a developed country")
#
# obj1=India()
# obj2=USA()
#
# for country in (obj1,obj2):
#     country.capital()
#     country.language()
#     country.typ()

#exa2: polymorphism withi init
# class Car:
#     def __init__(self,brand,model):
#         self.brand=brand
#         self.model=model
#     def move(self):
#         print("Drive")
# class Plane:
#     def __init__(self,brand,model):
#         self.brand=brand
#         self.model=model
#     def move(self):
#         print("fly")
#
# obj1=Car("i20","asta")
# obj2=Plane("Indigo","sw123")
#
# for i in (obj1,obj2):
#     i.move()


#2.Inheritance: Inheritance allows us to define a class that inherits all the methods and properties from another class
#single inheritance: when a child class inherits from only one parent class is call single inheritance

#exa:
# class Parent:
#     def func1(self):
#         print("This function is in Parent class")
#
# class Child(Parent):
#     def func2(self):
#         print("This function in in a Child class")
#
# obj=Child()
# obj.func2()
# obj.func1()

#Multiple Inheritance:
#when a child class inherits from multiple parent classes
# class Base1:
#     def __init__(self):
#         self.str1="Python"
#         print(self.str1)
# class Base2:
#     def __init__(self):
#         self.str2="Java"
#         print(self.str2)
# class Derived(Base1,Base2):
#     def __init__(self):
#         Base1.__init__(self)
#         Base2.__init__(self)
#         print("Derived class")
#     def Print(self):
#         print(self.str1,self.str2)# #######  Multilevel Inheritance:
# #


#Multi-level inheritance

# # class Base:
# #     def __init__(self,name):
# #         self.name=name
# #     def getname(self):
# #         return self.name
# #
# # class Child(Base):
# #     def __init__(self,name,age):
# #         self.age=age
# #         Base.__init__(self,name)
# #     def getage(self):
# #         return self.age
# #
# # class Grandchild(Child):
# #     def __init__(self,name,age,adress):
# #         self.adress=adress
# #         Child.__init__(self,name,age)
# #     def getadress(self):
# #         return self.adress
# #
# # obj=Grandchild("john",28,"Banglore")
# # print(obj.name,obj.age,obj.adress)
#
# obj=Derived()
# obj.Print()
















# #######  Multilevel Inheritance:
#it is a typ of inheritance in whice a class inherits from a class, which itself inherits from another class
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














