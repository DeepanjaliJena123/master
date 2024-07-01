import setuptools.command.upload

#Taking Input of a Python List
# string=input("enter the element :")
#
# lst=string.split()
# print("The list is",lst)
#

#exa
# ## input size of the list
# n = int(input("Enter the size of list : "))
# # store integers in a list using map,
# # split and strip functions
# lst = list(map(int, input("Enter the integer\
# elements:").strip().split()))[:n]
#
# # printing the list
# print('The list is:', lst)


#exa:: append
#only one item can be added at a time
#append() method only works for the addition of elements at the end of the List,

# s=[]
# s.append(1)
# s.append(2)
# s.append(3)
#
# print(s)

#or loop

# for i in range(1,5):
#     s.append(i)
# print(s)
#
# s.append((5,10)) #we can add tuple in list
# print(s)
#
# lis=["geek","python"]
# s.append(lis)
# print(s)


##### insert
#insert() method requires two arguments(position, value).

# lis=[4,5,6,7,8]
#
# lis.insert(0,"geek")
# lis.insert(3,10)
#
# print(lis)

#extend
# lis=[1,2,3]
# lis.extend([10,20,"geek","for","python"])
# print(lis)


#reverse:
# lis1=["geek","for",2,3]
# lis1.reverse()
# print(lis1)


### interview qstn
# x="hello python geek"
# z=''
# y=x.split()
# val=''
#
# for i in y:
#     a=''
#     a+=i[0].upper()+i[1:len(i)-1]+i[-1].upper()
#     val+=a+''
# print(val)



# reversed list
# list1=[2,4,6,8,10]
# k=list(reversed(list1))
# print(k)


##remove list
# k = [1, 2, 3, 4, 5, 6,
#         7, 8, 9, 10, 11, 12]
#
# k.remove(5)
# k.remove(6)
# print("remove list :",k)


#or loop
# k = [1, 2, 3, 4, 5, 6,
#       7, 8, 9, 10, 11, 12]
#
# for i in range(1,5):
#     k.remove(i)
# print(k)

#pop

# lis=[1,2,3,4,5]
# lis.pop()
# print(lis)
#
# lis.pop(1)
# print(lis)

## list comprehension
#print all odd number range(10) n sqaure it.

# odd_square=[x**2 for x in range (1,11) if x%2==1]
# print(odd_square)

#or
# odd_square=[]
# for i in range(1,11):
#     if i%2==1:
#         odd_square.append(i**2)
# print(odd_square)

# #or
# power_of_2 = [2 ** x for x in range(1, 9)]
# print (power_of_2)

# lis=[1,2,3,4,5]
# del lis[1:3]
# print(lis)

# lis = [2, 1, 3, 5, 3, 8]
# lis.sort()
# print(lis)

#count
# # To get the number of occurrences
# # of each item in a list

# lst = ['Cat', 'Bat', 'Sat', 'Cat', 'Mat', 'Cat', 'Sat']
#

# print([[l, lst.count(l)] for l in set(lst)])
# print(dict([l, lst.count(l)] for l in set(lst)))
#
#
## count using loop
#qstn
# lst = [8, 6, 8, 10, 8, 20, 10, 8, 8]
# x = 8
# count=0
# new_lis=[]
#
# for i in lst:
#     if i==x:
#         new_lis.append(i)
#         count+=1
# print(count)
# print(new_lis)

#or
# def countX(lst,x):
#     count=0
#     for i in lst:
#         if i==x:
#             count+=1
#         return count
# lst = [8, 6, 8, 10, 8, 20, 10, 8, 8]
# x=8
# print("{} has occured {} times".format(x,countX(lst,x)))


#qstn
# l = [1, 1, 2, 2, 2, 3, 3, 4, 4, 5, 5]
# ele=1
# x=[i for i in l if ele==i]
# print("the element",ele,"occurs",len(x),"times")
#
# or
# print([[i,l.count(i)] for i in set(l)])

#Get Number of Unique Elements in a List(count)
#
# lis=[1,2,3,4,5,6,7,7,8,2,1,3]
# unique_lis=set(lis)
# count_unique=len(unique_lis)
#
# print("The lis is :",count_unique)


##sort
# s=[1,5,6,7,3,10,21,0,2]
# s.sort()
# print(s)


#reverse sort
# k=[1,5,0,3,8,2]
# k.sort(reverse=True)
# print(k)

# list1 = [(1,2),(3,3),(1,1)]
# list1.sort(reverse=True)
# print(list1)

#key-lenth sort
# words = ["apple", "banana", "kiwi", "orange", "grape"]
# words.sort(key=len)
# print(words)

#sort by age use lambda
# people = [("Alice", 25), ("Bob", 30), ("Charlie", 22), ("David", 28)]
# people.sort(key=lambda x:x[1])
# print(people)

# Sorting List of Dictionaries by a Specific Key
# students = [
#     {"name": "Alice", "age": 25},
#     {"name": "Bob", "age": 30},
#     {"name": "Charlie", "age": 22},
#     {"name": "David", "age": 28},
# ]
#
# students.sort(key=lambda x:x["age"])
# print(students)

###copy
# fruits = ["mango","apple","strawberry"]
# shakes=fruits.copy()
# print(shakes)


#exa
# import copy
#
# # Initializing list
# list1 = [1, [2, 3], 4]
# print("list 1 before modification:\n", list1)
#
# # all changes are reflected
# list2 = list1
#
# # shallow copy - changes to
# # nested list is reflected,
# # same as copy.copy(), slicing
#
# list3 = list1.copy()
#
# # deep copy - no change is reflected
# list4 = copy.deepcopy(list1)
# print(list4)


#Copy List Using Slicing
# ls=[1,2,3]
# ls1=ls[:]
# ls1.append(4)
# print(ls1)

#pop
# fruits = ["apple", "mango", "cherry"]
# fruits.pop()
# print(fruits)

#exa
# my_list = [1, 2, 3, 4, 5, 6]
# print(my_list.pop(),my_list)


##reduce  reduce() stores the intermediate result and only returns the final summation value
# import functools
# lis = [1, 3, 5, 6, 2]
# print("the sum of list is :",end="")
# print(functools.reduce(lambda a,b:a+b,lis))

#exa
# import functools
# import operator
# #
# lis = [1, 3, 5, 6, 2]
# print(functools.reduce(operator.add,lis))
# print(functools.reduce(operator.mul,lis))

# print(functools.reduce(operator.add,['geek','for','geeks']))



#
# reduce() vs accumulate()
#
# Both reduce() and accumulate() can be used to calculate the summation of a sequence elements.
# But there are differences in the implementation aspects in both of these.

#exa
# import functools
# import itertools
# lis = [1, 3, 5, 6, 2]
#
# print(list(itertools.accumulate(lis,lambda x,y:x+y)))
# print(functools.reduce(lambda x,y:x+y,lis))


####### filter
# def fun(variable):
#     letters = ['a', 'e', 'i', 'o', 'u']
#     if variable in letters:
#         return True
#     else:
#         return False
#
# sequence = ['g', 'e', 'e', 'j', 'k', 's', 'p', 'r']
#
# filtered=filter(fun,sequence)
# for s in filtered:
#     print(s)



#findout even odd using filter
# seq = [0, 1, 2, 3, 5, 8, 13]
#
# res=filter(lambda x:x%2 !=0,seq)
# print(list(res))
#
# res1=filter(lambda x:x%2==0,seq)
# print(list(res1))

#exa
# def is_multipleof_3(num):
#     return num%3==0
#
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# res=list(filter(lambda x:is_multipleof_3(x),numbers))
# print(res)



######   map
# Map in Python is a function that works as an iterator to return a result
# after applying a function to every item of an iterable (tuple, lists, etc.).
# It is used when you want to apply a single transformation function to all the iterable elements.
# The iterable and function are passed as arguments to the map in Python.18 May 2023
#
#Syntax: map(fun, iter)

#exa::# We double all numbers using map()

# def addition(n):
#     return n+n
#
# numbers = (1, 2, 3, 4)
#
# res=map(addition,numbers)
# print(list(res))


#exa
# numbers = (1, 2, 3, 4)
# res=map(lambda x:x+x,numbers)
# print(list(res))
#

#exa
# numbers1 = [1, 2, 3]
# numbers2 = [4, 5, 6]
#
# res=map(lambda x,y:x+y,numbers1,numbers2)
# print(list(res))

#exa::# map() can listify the list of strings individually

# l = ['sat', 'bat', 'cat', 'mat']
# res=list(map(list,l))
# print(res)

### Define a function that doubles even numbers and leaves odd numbers as is
# def double_even(number):
#     if number%2==0:
#         return number*2
#     else:
#         return number
#
# numbers = [1, 2, 3, 4, 5]
#
# res=list(map(double_even,numbers))
# print(res)

##




