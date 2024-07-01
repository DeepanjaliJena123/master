# x='Hello Welcome to python'
# # swap all upper to lower and lower to upper
#
## separate all value and numbers

# y="hello wel1come t2o pyth4on"
# new=""
# for i in y:
#     # print(i)
#     if i.isalpha() or i.isspace()==True:
#         new+=i
# print(new)

#or
# # separate all value and numbers
# str1="hello wel1come t2o pyth4on"
# x=""
# y=""

# for i in str1:
#     if i.isalpha() or i.isspace():
#         x+=i
#     else:
#         y+=i
# print(x)            #hello welcome to python
# print(y)            #124
#


#Fibonacci series
# x=0
# y=1
# for i in range(10):
#     z=x+y
#     x=y
#     y=z
#     print(z)
#
# # #find the vowels count
# #
# z="hello welcome to python"
# vowel="a,e,i,o,u"
# count=0
#
# for i in z:
#     if i in vowel:
#         count+=1
# print(count)
#
# a='hel$lo wel*come to@ pyt#&on'
# #remove all speacial characters
# new_str=""
# for i in a:
#     if i.isalnum() or i.isspace():
#         new_str+=i
# print(new_str)

#
# #remove all speacial characters
# a='hel$lo wel*come to@ pyt#&on'
# chrs=""
# spcl_chr=""
#
# for i in a:
#     if i.isalpha() or i.isspace():
#         chrs+=i
#     else:
#         spcl_chr+=i
# print(spcl_chr)
# print(chrs)


# c=" hello welcome to python "
# #remove first and last spaces
# c.strip()
# print(c)
#
# x=" hello welcome to python "
# new=""
# for i in range(1,len(x)-1):
#     new+=x[i]
# print(new)

# for i in range(1,len(x)-1):
#     new+=x[i]
# print(new)                  #hello welcome to python


# #

# # # reversed list
# x=[5,9,6,8,3,2,4]
# z=[]
# y=1

# for i in range(len(x)):
#     z.append(x[-y])
#     y+=1
# print(z)


# # #or
# x=[5,9,6,8,3,2,4]
# z=[]
# count=1
# for i in range(-1,len(x)): #7            #0,1,2,3,4,5,6
#     z.append(x[i])
#     count=count+1
# print(z)


#exa: Reverse a list using loop

# s=[10,20,30,40]
# z=[]
# y=1
# for i in range(len(s)):
#     z.append(s[-y])
#     y+=1
# print(z)





###################################################################################
# Example 1: Print the first 10 natural numbers using for loop.
# n=11
# for i in range(1,n):
#     print(i)

# Example 2: Python program to print all the even numbers within the given range.
# given_range=11
# for i in range(given_range):
#     if i%2==0:
#         print(i)

# Example 3: Python program to calculate the sum of all numbers from 1 to a given number.
# n=11
# count=0
# for i in range(1,n):
#     count+=i
# print(count)

# or
# for i in range(1,n+1):
#     count+=i
# print(count)

# Example 4: Python program to calculate the sum of all the odd numbers within the given range.
# num=10
# sum=0
# for i in range(num):
#     if i%2!=0:
#         sum+=i
# print(sum)

#or
# n=10
# count=0
# z=[]
# for i in range(1,n+1):
#     if i%2==0:
#         z.append(i)
#         count+=i
# print(z)
# print(count)

#Example 5: Python program to print a multiplication table of a given number
# n=5
# for i in range(1,11):
#     print(n,'X',i,'=',n*i)

# Example 6: Python program to display numbers from a list using a for loop.
# list = [1,2,4,6,88,125]
# for i in list:
#     print(list)
#

# Example 7: Python program to count the total number of digits in a number.
# given_number = 129475
# gv=str(given_number)
# total=0
# count=0
# for i in range(len(gv)):
#     count+=1
#     total+=int(gv[i])
# print(count)
# print(total)

# Example 8: Python program to check if the given string is a palindrome.
# given_string="madam"
# reverse_string=""
# for i in given_string:
#     reverse_string=i+reverse_string
# if given_string==reverse_string:
#     print("it is palindrome")
# else:
#     print("not palindrome")

# Example 9: Python program that accepts a word from the user and reverses it.

# given_string=input()       #deepa
# r=""
# for i in given_string:
#     r=i+r
# print(r)

# Example 10: Python program to check if a given number is an Armstrong number
# number that equals the sum of its individual digits, each raised to the power of the number of digits



# Example 11: Python program to count the number of even and odd numbers from a series of numbers.
# num_list = [1, 3, 5, 6, 99, 134, 55]
# for i in num_list:
#     if i % 2 == 0:
#         print(i, "is an even number.")
#     else:
#         print(i, "is an odd number."

#or
# num=[1, 3, 5, 6, 99, 134, 55]
# count_even=0
# count_odd=0
# for i in num:
#     if i%2==0:
#         count_even+=1
#     else:
#         count_odd+=1
# print(count_even)
# print(count_odd)


#exa:find the 2nd largest number:
# x=[2,4,1,3,6,5]
# x.sort()
# number=25
# second_largest=[]
# for i in x:
#     if number%i==0:
#         number=number+i
# print(second_largest)

#check prime number
# n=10
# for i in range(2,n):
#     if n%i==0:
#         print("not prime number")
#         break
# else:
#         print("prime number")
#

#sort character of string? 1st alphabet,sy,bol followed by digit?
# name="geekforpython"
# print("".join(sorted(name)))
#
# ch=input("enter character :")
# if ch.isdigit():
#     print("is digit")
# else:
#     print("not digit")
#
# print("".join(sorted(ch)))

#Count number of vowels in a String in Python
# s="geek for python"
# vowel=['a','e','i','o','u']
# count=0
# for i in s:
#     if i in vowel:
#         count+=1
# print(count)
#or
# for i in range(len(s)):
#     if s[i] in vowel:
#         count+=1
# print(count)
#


#exa::
#ABAABBCA
#ans. 4A3B1C
# s="ABAABBCA"
# count_chr=""
# for i in range(len(s)):
#     count_chr.count(s[i])
# print(count_chr)
#
# for i in range(len(s)):
#     for j in range(1,len(s)):
#         count_chr+=j
# print(count_chr)               doubt
#####
###ABAABBCA
# #ans. 4A3B1C
# s="ABAABBCA"
# new=""

# for k in s:
#     if k not in new:
#         new+=k
# print(new)
#
# for i in new:
#     count=0
#     for j in range(len(s)):
#         if i==s[j]:
#             count+=1
#     print(str(count)+str(i),end="")

##Ascending order  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# a=[1,3,5,7,9]
# b=[2,4,6,8,10]
# a=[1,3,5,7,9,2,4,6,8,10]
# print(a)
# for i in range(len(a)):
#     for j in range(len(a)):
#         if a[i]<a[j]:
#             a[i],a[j]=a[j],a[i]
# print(a)
####
# #output={hello:5,welcome:7,to:2,python:6}
# x="hello welcome to python"
# v=x.split()
# dic={}
#
# for i in v:
#     dic[i]=len(i)
# print(dic)
# for i in v:
#     count=0
#     for j in range(len(i)):
#         count+=1
#     dic[i]=count
# print(dic)

###output:"he"
# s="hello"
# unq=""
# for i in s:
#     if i not in unq:
#         unq+=i
# print(unq[0:2])
#
# for i in s:
#     unq=unq+i[0:2]
# print(unq)

#######3
# n=10
# for i in range(1,n+1):
#     if n%i==0:
#         print(i)
#
#Multiplw
# class Base1:
#     def __init__(self):
#         self.str1="geek"
# class Base2:
#     def __init__(self):
#         self.str2="python"
# class Derived(Base1,Base2):
#     def __init__(self):
#         Base1.__init__(self)
#         Base2.__init__(self)
#         print("derived class")
#     def Print(self):
#         print(self.str1,self.str2)
# obj=Derived()
# obj.Print()
#





# X="aaBBccDDeeFgHii"
# ch=""
#
# for i in range(len(X)):     #1,15
#     if X[i]==i:
#         continue
#         ch+=i

#exa: Reverse a list using loop
# s=[10,20,30,40]
# z=[]
# y=1
# for i in range(len(s)):
#     z.append(s[-y])
#     y+=1
# print(z)

#exa or
# lst = [10, 11, 12, 13, 14, 15]
#
# l = []
# for i in lst:
#     l.insert(0, i)
# print(l)

#exa or
# original_list = [1, 2, 3, 4, 5]
# reversed_list = []
# for value in original_list:
#   reversed_list = [value] + reversed_list
# print(reversed_list)

#exa or
# s= [1, 2, 3, 4, 5]
# k= []
# for value in range(len(s)):
#   k.append(s.pop())
# print(k)

#Using recursion,without the use of any built-in functions.
# def list_reverse(original_list ):
# if(len(original_list) == 0):
#   return original_list
# else:
#   return list_reverse(original_list [1: ])+original_list[0]
#
# original_list = [1, 2, 3, 4, 5]
# print("List before reverse : ",original_list)
# print("List after reverse : ", list_reverse(original_list))


#get 4 snd 5 uding slicing
# s=[1,2,3,4,5,7,8,9,10]
# sliced_list=s[3:5]
# print(sliced_list)

#################################  Duplicate   ###################
#remove duplicate from list
# s=[2,2,3,4,5,6,5,1]
# chr_uniqe=[]

# for i in s:
#     if i not in chr_uniqe:
#         chr_uniqe.append(i)
# print(chr_uniqe)

#exa
# mylist = ["a", "b", "a", "c", "c"]
# lis1=list(dict.fromkeys(mylist))
# print(lis1)

#exa
# mylist = ["a", "b", "a", "c", "c"]
# s=list(set(mylist))
# print(s)

#



################################
# Make all the first letter as capital.
#xa
# x="my name is deepa"
# k=x.split()
# print(k)
#
# for i in k:
#     z=i[0].upper()+i[1:]
#     print(z,end=" ")

#Or
# z=''
# for i in k:
#     d=i[0].upper()+i[1:]
#     z=z+d+" "
# print(z)


#exas1 = "abcdefg"
# s1 = "abcdefg"
# s2 = "xyz"
# s3 = '12345'
#
# result = ''
# for i in range(max(len(s1), len(s2), len(s3))):
#     if i < len(s1):
#         result += s1[i]
#     if i < len(s2):
#         result += s2[i]
#     if i < len(s3):
#         result += s3[i]
# #
# print(result)                                               doubt

##exa: x=baNaNa
# x='banana'
# y=[]
# for i in x:
#     if i=='n':
#         y.append(i.upper())
#     else:
#         y.append(i)
# print("".join(y))



#exa ['my', 'NAME', 'is', 'NAME', 'deepanjali', 'NAME', 'jena']
# s="m@y name is na@me deepanjali name j@ena"
# k=s.split()
# y=[]
# for i in k:
#     if i=="name":
#         y.append(i.upper())
#     else:
#         y.append(i)
# print(y)


#exa
# s="m@y name is na@me deepanjali name j@ena"
# y=[]
#
# for i in s:
#     if i!="@":
#         y+=i
# print("".join(y))

#or
# for i in "m@y name is na@me deepanjali name j@ena":
#     if i=="@":
#         continue
#     print("".join(i),end="")       #my name is name deepanjali name jena
#
#

#or
# s="m@y name is na@me deepanjali name j@ena"
# y=[]
#
# for i in s:
#     if i=="@":
#         continue
# print(y)                                  #another way


#exa:
# clothes = ["shirt", "sock", "pants", "sock", "towel"]
# paired_socks = []
#
# for item in clothes:
#     if item == "sock":
#         continue
#     else:
#         print(f"Washing {item}")
# paired_socks.append("sock")
# print(f"washing{paired_socks}")
#

#exa:
# s=['john','jimmy','Aman','jisu','jini']
# empty=[]
# for i in s:
#     if i.islower():
#         empty.append(i[0].upper()+i[1:])
# print(empty)


#exa: odd word middle ltr will be uper
# x='hello welcome to python'
# k=x.split()
# modified=[]
#
# # for i in k:
# #     if len(i)%2!=0:
# #         ltr=len(i)//2
# #         modified.append(i[0:ltr]+i[ltr].upper()+i[ltr:])
# #     else:
# #         modified.append(i)
# # print(modified)
#
# for i in k:
#     if len(i)%2!=0:
#         ltr=len(i)//2
#         modified.append(i[0:ltr]+i[ltr].upper()+i[ltr+1:])
#     else:
#         modified.append(i)
# print(modified)


#exa: increment 2
# s=[10,20,30,40,50]
# new=[]
# for i in s:
#     new.append(i+2)
# print(new)
#or
#comprehesion:
# s=[10,20,30,40,50]
# new=[i+2 for i in s]
# print(new)

#exa:find out even number
# cube=[]
# for i in range(11):
#     if i%2==0:
#         cube.append(i**3)
# print(cube)
#

# #comprehension
# new=[x**3 for x in range(11) if x%2==0]
# print(new)


##swap 1st and last number from list /interchange first and last elements in a list

# def swap_list(lst):
#     if len(lst)<2:
#         return lst
#     else:
#         lst[0],lst[-1]=lst[-1],lst[0]
#         return lst
# lis=[12, 35, 9, 56, 24]
# print("original list:",lis)
# lis=swap_list(lis)
# print("swap list:",lis)

### Using * operand. swap list
#exa:
# list=[1,2,3,4]
# a,*b,c=list
# print(a)
# print(b)
# print(c)

#exa
# def swaplist(list):
#     start,*middle,end=list
#     list=start,*middle,end
#     return list
#
# newList = [12, 35, 9, 56, 24]
#
# print(swaplist(newList))

###Convert a List into a Tuple
# def convert(list):
#     return tuple(list)
#
# list=[1,2,3,4,5]
# print(convert(list))
#

#Convert Python List to String using for loop
# def listTOstring(list):
#     str1=""
#
#     for i in list:
#         str1+=i
#     return str1
#
# list=['geek','for','geek']
# print(listTOstring(" ".join(list)))



#Remove Duplicates from the list using the set() Method
# list1= [1, 5, 3, 6, 3, 5, 6, 1]
# list2=list(set(list1))
# print(list2)

#or
# list1= [1, 5, 3, 6, 3, 5, 6, 1]
# new_list=[]
# for i in list1:
#     if i not in new_list:
#         new_list.append(i)
# print(new_list)


###### Remove Elements From Lists in Python using pop()
# test_list = [1, 4, 3, 6, 7]
# test_list.pop(0)
# print(test_list)

#or sclicing
# test_list = [1, 4, 3, 6, 7]
# res=test_list[1:]
# print(res)

#or using List comprehension
# list = [1, 4, 3, 6, 7]
#
# new=[x for x in list[1:]]
# print(new)
#
#

########## Merge Two Lists in Python
# list1 = [1, 4, 5, 6, 5]
# list2 = [3, 5, 7, 2, 5]
# for i in list2:
#     list1.append(i)
# print(list1)
#
#or Merge Two Lists in Python using list comprehension
# list1 = [1, 4, 5, 6, 5]
# list2 = [3, 5, 7, 2, 5]
#
# res=[y for x in (list1,list2) for y in x]
# print(res)

# Merge two lists using extend()
# list1 = [1, 4, 5, 6, 5]
# list2 = [3, 5, 7, 2, 5]
# list1.extend(list2)
# print(list1)

### find sum of elements in list
# list=[1,2,3,4,5]
# count=0
# for i in list:
#     count+=i
# print(count)

#or
# list=[1,2,3,4,5]
# count=0
# for i in range(len(list)):
#     count=count+list[i]
# print(count)

#or sum method using
# list=[1,2,3,4,5]
# total=sum(list)
# print(total)


# Using enumerate function
# list=[1,2,3,4,5]
# s=0
# for i, a in enumerate(list):
#     s+=a
# print(s)


#Using list comprehension
# list=[1,2,3,4,5]
# res=[i for i in list]
# print(sum(res))

#####  Find Largest Number in a List
# list1 = [10, 20, 4, 45, 99]
# list1.sort()
# print("Largest number:",list1[-1])
#
#

# #exa:qstn
# x=[0.1,2,0.9,3,5,0.5,8,6]
#
# for i in range(len(x)):
#     for j in range(i+1,len(x)):
#         if x[i]>x[j]:
#             x[i],x[j]=x[j],x[i]
# print(x)


# def myMax(list1):
#
#     max = list1[0]
#
#     for x in list1:
#         if x > max:
#             max = x
#
#     return max
#
# list1 = [10, 20, 4, 45, 99]
# print("Largest element is:", myMax(list1))




################
# #polymorphism
# class India:
#     def languange(self):
#         print("hindi ")
#     def Capital(self):
#         print("delhi")
# class USA:
#     def languange(self):
#         print("english")
#     def Capital(self):
#         print("washington")
#
# ind_obj=India()
# usa_obj=USA()
#
# for i in (ind_obj,usa_obj):
#     i.Capital()
#     i.languange()



#inheritance
#single inheritance
#when a class inherits only one parent class
# class A:
#     def fun1(self):
#         print("hi A")
# class B(A):
#     def fun2(self):
#         print("hi B")
#
# obj=B()
# obj.fun2()
# obj.fun1()

#multiple
#when child class inherit propertis of multiple parent class

# class Base1:
#     def __init__(self):
#         self.attr1="python1"
#         print("Base1")
# class Base2():
#     def __init__(self):
#         self.attr2="python2"
#         print("Base2")
# class Derived(Base1,Base2):
#     def __init__(self):
#         Base1.__init__(self)
#         Base2.__init__(self)
#         print("Derived")
#
#     def Print(self):
#         print(self.attr1,self.attr2)
#
# obj=Derived()
# obj.Print()


#Multi level
#when a class inherit from a class, which itself inherit from another class
# class Base:
#     def __init__(self,name):
#         self.name=name
#     def getName(self):
#         return self.name
# class Child(Base):
#     def __init__(self,name,age):
#         self.age=age
#         Base.__init__(self,name)
#     def getAge(self):
#         return self.age
# class Grandchild(Child):
#     def __init__(self,name,age,adress):
#         self.adress=adress
#         Child.__init__(self,name,age)
#     def getAdress(self):
#         return self.adress
#
# obj=Grandchild("deepa",30,"odihsa")
# print(obj.name,obj.age,obj.adress)
#

#hierarchie
#when more than one derived class  are created from a single base

# class Parent:
#     def func1(self):
#         print("this is func1 from parent class")
# class child1(Parent):
#     def func2(self):
#         print("this is func2 from child1 class")
# class child2(Parent):
#     def func3(self):
#         print("this is func3 form child3 class")
#
# obj=child1()
# obj2=child2()
# obj2.func3()
# obj.func1()

#hybrid
# Inheritance consisting of multiple types of inheritance is called hybrid inheritance.

# class School:
#     def func1(self):
#         print("This function is in school.")
#
#
# class Student1(School):
#     def func2(self):
#         print("This function is in student 1. ")
#
#
# class Student2(School):
#     def func3(self):
#         print("This function is in student 2.")
#
#
# class Student3(Student1, School):
#     def func4(self):
#         print("This function is in student 3.")
#
#
# # Driver's code
# object = Student3()
# object.func1()
# object.func2()


########
#### IRIS
#
# x="i am linga100raj routray345 py789thon"
#
# # add 100,345,789
# z=x.split()
# y=[]
#
# for i in z:
#     val=''
#     for j in range(len(i)):
#         if i[j].isnumeric():
#             val+=i[j]
#     y.append(val)
# print(y)

#


# for i in z:
#     if i.isdigit():
#         y.append(i)
# print(y)


####qstn
# # Output : {'Gfg': 1, 'is': 1, 'best': 1}
# x='Gfg is best'
# y=x.split()
# z={}
# for i in y:
#     z[i]=1
# print(z)


######
#hello , count chr
# x="hello"
# u=[]
# for s in x:
#     if s not in u:
#         u.append(s)
# print(u)
# for i in u:
#     count=0
#     for j in range(len(x)):
#         if i==x[j]:
#             count+=1
#     print(i,count)


#output=h:1,e:1,l:2,o:1
# x="helllo"
# uniq=[]
# for k in x:
#     if k not in uniq:
#         uniq.append(k)
# print(uniq)

# for i in x:
#     count=0
#     for j in range(len(x)):
#         if i==x[j]:
#             count+=1
#     print(i,count)                                     doubt

#
# my_list = [[10,20,30],[40,50,60],[70,80,90]]
# new=[]
# for i in my_list:
#     for j in i:
#         new.append(j)
# print(new)


##ashok
##Write a program Find the second largest prime number
# x =[2,5,3,7,9,3,6]
#
# for i in range(len(x)):
#     for j in range(i+1,len(x)):
#         if x[i]>x[j]:
#             x[i],x[j]=x[j],x[i]
# print(x[-2])
#

###
##occurance in

# x=[1,2,5,6,7,9,2,6,4,2,4,8,4,2]
# new=[]
# for i in x:
#     if i not in new:
#         new.append(i)
# print(new)
# for j in new:
#     count = 0
#     for k in range(len(x)):
#         if j==x[k]:
#             count+=1
#     print(j,count)


#######33
# output=Hello world
# x=''' @@@@@@@
# $$$$$$$$$$$
# Hello world!!!
# $$$$$$$$$$$
# @@@@@@@'''
# new=""
# for i in x:
#     if i.isalpha():
#         new=new+i
# print(new)


# make all 2 &4 to 0
# x=[1,2,5,6,7,9,2,6,4,2,4,8,4,2]
# #
# for i in range(len(x)):
#     v = 0
#     if x[i]==2 or x[i]==4:
#         x[i]=v
# print(x)                            #[1, 0, 5, 6, 7, 9, 0, 6, 0, 0, 0, 8, 0, 0]









