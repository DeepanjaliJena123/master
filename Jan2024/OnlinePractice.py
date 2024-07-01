# Q1. Convert a given string to int using a single line of code.
# a="5"
# print(int(a))
#Q2. Write a code snippet to convert a string to a list.
# s="geek for python"
# print(s.split())         #['geek', 'for', 'python']

# Q3. Write a code snippet to reverse a string.
# name="deepanjali"
# new=""
# for i in name:
#     new=i+new
# print(new)

# Q4. Write a code snippet to sort a list in Python.
# lis=[3,5,2,1]
# lis.sort()
# print(lis)          #[1, 2, 3, 5]

# Q6. How can you delete a file in Python?
# Ans. We can delete the file in Python using the os module.
# The remove() function of the os module is used to delete a file in Python by passing the filename as a parameter.
#import os
# os.remove("txt1.txt")

# Q8. Discuss different ways of deleting an element from a list.
# 1. By using the remove() function
# The remove () function deletes the mentioned element from the list.

# list1 = [1, 2, 3, 4]
# list1.remove(2)
# print(list1)         #[1, 3, 4]

# 2. By using the pop() function,using index
# list2= [1, 2, 6, 4]
# list2.pop(1)
# print(list2)        #[1, 6, 4]

# Q9. Write a code snippet to delete an entire list.
# liss=[10,20,50]
# liss.clear()
# print(liss)

# Q10. Write a code snippet to reverse an array.
# Ans. The two ways of reversing an array are as follows:
#
#1. Using the flip() function
# import numpy as np
# arry1=np.array([1,2,3])
# arry2=np.flip(arry1)
# print(arry2)
#
# 2. Without using any function

# import numpy as np
# arr1 = np.array([1, 2, 3, 4])
# arr2 = arr1[::-1]
# print(arr2)

# Q12. Write a code snippet to concatenate lists.

#
# [‘We’, ‘a ‘, ‘writing’, ‘blog’]

# lst1 = ['W', 'a', 'w', 'b']
# lst2 = ['e', ' ', 'riting', 'log']
# lst3 = [x + y for x, y in zip(lst1, lst2)]
# print(lst3)

# Q13. Write a code snippet to generate the square of every element of a list.
# lis=[1,2,3]
# lis2=[]
# for i in lis:
#     lis2.append(i*i)
# print(lis2)             #[1, 4, 9]

# Q16. What is init in Python?

##_init_
#It is run as soon as an object of a class is instantiated.
# The method is useful to do any initialization you want to do with your object.

# or
# Ans. __init__ method is used in Python to initialize the attributes of the object when the object is created.
 # It is declared within the class as a reserved method.


# Q18. Which is faster, Python list or Numpy arrays, and why?

#Ans. NumPy arrays are faster than Python lists for numerical operations.

# NumPy is an open-source library for working with arrays in Python, and
# it provides a number of functions for performing operations on arrays efficiently.

# They are faster than Python lists because they are implemented in C,
# while Python lists are implemented in Python.
# This means that operations on NumPy arrays are implemented in a compiled language,
# which makes them faster than operations on Python lists, which are implemented in an interpreted language.
#
# Python also has an inbuilt array library for basic operations. W can use it as ‘import array as arr’


# Q19. What is the difference between a Python list and a tuple?
#List
#list is a collection which is orderd and chnagable
# means that you can change the value of a list element or add or remove elements from a list
#list are mutable.[].
# Lists are created using square brackets[] and a comma-separated list of values.

#Tuple
# A tuple is also an ordered collection of objects,
# but it is immutable, which means that you cannot change the value of a tuple element or add or remove elements from a tuple.
#Lists are defined using square brackets ([ ‘’ ]), while tuples are defined using parentheses ((‘’, )).




#qstn:: Write a Python program to find the factorial of a number.

# def factorial(n):
#     if n==1:
#         return 1
#     else:
#         return n*factorial(n-1)
#
# number=5
# result=factorial(number)
# print(f"The factorial of {number} is {result}")
#


##################
# Print numbers from 1 to 10 using a for loop:
# for i in range(1,11):
#     print(i,end="")

# Calculate the sum of numbers from 1 to 10 using a for loop:
# sum=0
# for i in range(1,11):
#     sum+=i
# print(sum)

# Calculate the product of elements in a list using a for loop:
# lis=[1,2,3,4]
# product=1
# for i in lis:
#     product*=i
# print(product)

# Print even numbers from 1 to 10 using a for loop:
# for i in range(2,11,2):
#     print(i)

# Print numbers in reverse from 10 to 1 using a for loop:
# for i in range(10,0,-1):
#     print(i)
#

# Print characters of a string using a for loop:
# s="hello"
# for i in s:
#     print(i)

# Find the largest number in a list using a for loop:
#
# lis=[1,3,4,2,6]
# largest=lis[0]
# for num in lis:
#     if num>largest:
#         largest=num
# print(largest)

# Find the average of numbers in a list using a for loop:
# liss=[3,2,6,4,5]
# total=0
# for i in liss:
#     total+=i
# average=total/len(liss)
# print(average)

# Print all uppercase letters in a string using a for loop:

# # str="welcome HOME"
# # for i in str:
# #     if i.isupper():
# #         print(i)
#
#
# my_string = "Hello World"
# for char in my_string:
#     if char.isupper():
#         print(char)


# Count the number of vowels in a string using a for loop:

# s = "Hello World"
# vowels = "AEIOUaeiou"
# count=0
# for i in s:
#     if i in vowels:
#         count+=1
# print(count)
#

# Print a pattern of stars using nested for loops:
# for i in range(5):
#     for j in range(i + 1):
#         print("*", end="")
#     print()


# Calculate factorial of a number using a while loop:

num = 5
factorial = 1
while num > 0:
    factorial *= num
    num -= 1
print(factorial)









