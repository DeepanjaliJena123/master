


#print dublicate n greater than 2
# l=[1,2,3,4,5,5,4,4,3,2]
# new=[]
# for i in l:
#     if i not in new and i>=2:
#         new.append(i)
# print(new)


#qsn1
# x="abcabcbb"
# new=""
# count=0
# for i in x:
#     if i not in new:
#         new+=i
#         count+=1
# print(f"string count : {count}",new)
# #



#qsn2


# 69. Compare 2 strings and give the unique words
# a="hello how r u i'm good"
# x=a.split()
# print(x)
# b="hey how r u are you good"
# y=b.split()
# z=[]
# for i in x:
#     if i in y:
#         z.append(i)
# print(z)


# 81.
# s='i am ashok'               #- After reverse output will be kohsa ma i But again print the output like below
# output="kohsa ma i"        #Reverse the string  like this
# new=""
# for i in s:
#     new=i+new
# print(new)


# 98.Wap to print  3 and 8            doubt
# l=[1,3,5,8,9]
# d=11

# x=l[1:4]
# print(x)


# #Wap to check s2 is formed using s1 or not          doubt
# s1="panda"
# s2="nap"
# if s2 in s1[::-1]:
#     print("yes")
# else:
#     print("no")


# # arrey = 0 to n-1, 1 no. is missing .wap to findout which no. is missing        doubt
# n = int(input('enter number:'))
# s1 = n[0]
# for i in range(0, len(n - 1)):
#     if n[i] == n[0]:
#         print(n[0] is the
#         missing
#         number)
#         else:
#         pass

# 112. Convert list into dictionary and here key same but value will be square of key
# l=[10,20,30,20,10]
# square={x:x*x for x in l }
# print(square)

# 113.Convert single  list into dictionary using enumerate function
# l=[10,20,30,20,10]
# d1=dict(enumerate(l))
# print(d1)


# 114. Adition of 2 number using lambda function
# a=10
# b=20
# addition=lambda a,b:a+b
# print(addition(a,b))

# 115. Sum of 2 number using function(Non-void function)        #doubt

# def sum_num(x,y):
#     return x+y
# x=10
# y=10
# print(sum_num(x,y))
#

####
# 117. Write a python function which return multiple values
#120  doubt


# 231. Define a dictionary and reverse the order of the dictionary   doubt
# Ans- d = {
#   "ashok": "python",
#   "kumar": "tester",
#   "panda": 1994
# }
# print(d)
#
# 239. Give one example of exception?
# Ans- try:
#     div = 0 // 4
#     print( div )
# except:
#     print('attempting to divided by zero')
# finally:
#     print('execute every time')
#
#


# 240. Write a dynamic python program to find the sum of the numbers present in the string.
# Output-: 230
# x="Mango40Banana70Apple95Grapes25"
# a=[]
# for i in x:
#     if i.isnumeric():
#         a.append(i)
# print(a)
#
#
#







# import re
#
# a = "ajhdj123dh40dhghg60fhdgf"
# numbers = re.findall(r'\d+', a)
# print(numbers)                   #['123', '40', '60']

#
# import re
#
# s = "abc123def456"
# result = re.split(r'\d+', s)
# print(result)                 #['abc', 'def', '']


# Output -: 21
# x="Mango4Banana7Apple9Grapes1"
# a=[]
# for i in x.split():
#     if i.isnumeric():
#         a.append(i)
# print(a)                                    DOUBT



# 241. What will be the output without executing?
# str ="Python is a programming language"
# print (str.isalnum())


# 243. # Here i have to add l2 in l1 in place of [72,12,22]
# l1=[[35 ,53, 63],
#      [72 ,12, 22],
#      [43, 84, 56]]
# l2=[20,30,40]
# new=[]
# l1[1]=l2
# print(l1)

# for i in l1:
#     new.append(i)
# print(new)

#or
# l1=[[35 ,53, 63],
#      [72 ,12, 22],
#      [43, 84, 56]]
# l2=[20,30,40]
# new=[]
# for i in l1:
#     for j in i:
#         print()         doubt
#


# 256. What is Iterator in python?
# Ans-Iterator- Iterator is an object that allow us to travers through a sequence of data without storing the entire data in the memory
# # An object to be an iterator it must implement 2-methods,1.__iter__(),2.__next__()
# __iter__(): The iter() method is called for the initialization of an iterator. This returns an iterator object
# __next__(): The next method returns the next value for the iterable
# Every iterator is a iterable but all iterables are not iterator

# Example-1
# l=[10,20,30,40]
# iter_obj=iter(l)
# print(next(iter_obj))
# print(next(iter_obj))
# for i in iter_obj:
#     print(i)
# Memory used in list and iterator
# Example-Using list
# l=[x for x in range(1,100000)]
# for i in l:
#      print(i*2)
# import sys
# print(sys.getsizeof(l)/1024)  #->0/p->782.21
# example iterator
# x=range(1,100000)
# for i in x:
#     print(i*2)
# print(sys.getsizeof
#


# 28. From the given list create two new list, 1st list having only duplicate element and 2nd list having non duplicate element?







# 32. Write a python program using generator to print 1 to 100.





















