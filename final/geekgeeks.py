# Convert numeric words to numbers
# help_dict = {
#     'one': '1',
#     'two': '2',
#     'three': '3',
#     'four': '4',
#     'five': '5',
#     'six': '6',
#     'seven': '7',
#     'eight': '8',
#     'nine': '9',
#     'zero': '0'
# }
#
# test_str = "zero four zero one"
# print("The original string is : " + test_str)
# res = ''.join(help_dict[ele] for ele in test_str.split())
# print("The string after performing replace : " + res)


########## Set
# x="geeks"
# y=set(x)
# print(y)     #{'s', 'k', 'g', 'e'}

# z=['g','geek','p','geek']
# s=set(z)
# print(s)                   #{'p', 'g', 'geek'}

#
# t = ("Geeks", "for", "Geeks")
# print(set(t))                   #{'Geeks', 'for'}
#
# d = {"Geeks": 1, "for": 2, "Geeks": 3}
# print(set(d))                            #{'for', 'Geeks'}
#

#set create
# x={1,2,3}
# print(x)        #{1, 2, 3}

# Adding Elements to a Set in Python
# add() Method
# update() Method

#add
# x=set()
# x.add(8)
# x.add(9)
# x.add((6,7))
# print(x)          #{8, 9, (6, 7)}

#
# for i in range(1,6):
#     x.add(i)
# print(x)


#update
# For the addition of two or more elements, Update() method is used

# set1=set([4,5,(6,7)])
# set1.update([10,11,12,14])
# print(set1)                  #{4, 5, (6, 7), 10, 11, 12, 14}

#accessing set
# a=set(["geek","For","geek"])
# print("\nInitial set")
# # print(a)
#
# #Initial set
# # {'For', 'geek'}
#
# for i in a:
#     print(i,end="")

#Removing Elements from the Set in Python
#pop()
#clear()
#discard()
#remove()
#
# set1=set([1,2,3,4,5,6,7,8,9,10])
# set1.remove(5)
# print(set1)
# set1.discard(8)
# print(set1)
# set1.pop()
# print(set1)
# # set1.clear()
# # print(set1)
#
# for i in range(2,5):
#     set1.remove(i)
# print(set1)
#

#frozen set
# tup1=('G', 'e', 'e', 'k', 's', 'F', 'o', 'r')
#
# ftup1=frozenset(tup1)
# print(ftup1)                  #frozenset({'s', 'o', 'e', 'k', 'F', 'G', 'r'})
# print(frozenset)


#union
# s1={1,2,3}
# s2={"a","b","c"}
# s=s1.union(s2)
# print(s)                 #{1, 2, 3, 'b', 'c', 'a'}


#interaction
# set1 = {1, 2, 3, 4, 5}
# set2 = {4, 5, 6, 7, 8}
# my_set = set1.intersection(set2)
# print(my_set)                          #{4, 5}
#
# set1 = {1, 2, 3, 4, 5}
# set2 = {4, 5, 6, 7, 8}
# my_set = set1.difference(set2)
# print(my_set)                      #{1, 2, 3}


# set1 = {1, 2, 3, 4, 5}
# set2 = {4, 5, 6, 7, 8}
# my_set = set1.symmetric_difference(set2)
# print(my_set)                              #{1, 2, 3, 6, 7, 8}



# set1 = {1, 2, 3, 4, 5}
# set2 = {2, 3, 4}
# subset = set2.issubset(set1)
# print(subset)                   #True

#
# set1 = {1, 2, 3, 4, 5}
# set2 = {2, 3, 4}
# superset = set1.issuperset(set2)
# print(superset)                      #True



############################################## DICTIONARY
# dict={1:'geek',2:'for',3:'geek'}
# print(dict)
#

#exa
# dict={'name':'geek',1:[1,2,3,4]}
# print(dict)

#exa
# d=dict({1:'abc',2:'xyz',3:'@#$'})
# print(d)

# d1=dict([(1,'geek'),(2,'for')])
# print(d1)

#exa
# d1={1:'geek',2:'for',3:{'a':'welcome','b':'To','c':"phy"}}
# print(d1)
#
#

#exa
# d1={}
# d1[0]='geek'
# d1[1]="for"
# d1[2]=123
# # print(d1)      #{0: 'geek', 1: 'for', 2: 123}
#
# d1['val_set']=2,3,5
# d1[3]={'nested':{1:'life',2:'python'}}
# print(d1)
#

#exa
# dict = {1: 'Geeks', 'name': 'For', 3: 'Geeks'}
# print(dict['name'])
# print(dict.get(3))

#exa
# d={'dict1':{1:'geek'},
#    'dict2':{3:'for'}}
# print(d['dict1'])
# print(d['dict2'][3])
#


#exa
# d={2:'geek',3:'for',4:'phy'}
# print(d.items())              #dict_items([(2, 'geek'), (3, 'for'), (4, 'phy')])
# print(d.keys())               #dict_keys([2, 3, 4])
# d.clear()
# print(d)                     #{}
# k=d.copy()
# print(k)
# d.pop(3)
# print(d)                     #{2: 'geek', 4: 'phy'}
# d.popitem()
# print(d)                       #{2: 'geek', 3: 'for'}

# d.update({5:'klm'})
# print(d)                          #{2: 'geek', 3: 'for', 4: 'phy', 5: 'klm'}

# print(d.values())                 #dict_values(['geek', 'for', 'phy'])


##merge or add two dict
# x={1:'a',2:'b'}
# y={'name':'deepa','age':30}
# x.update(y)
# print(x)                        #{1: 'a', 2: 'b', 'name': 'deepa', 'age': 30}



## use def func and merge two dict
# def Merge(x,y):
#     x.update(y)
#     return x
#
# x={1:'a',2:'b'}
# y={'name':'deepa','age':30}
#
# print(Merge(x,y))
# print(x)

#exa::Python unpacking operator
#Using ** [double star] is a shortcut that allows you to pass multiple arguments to a function directly using a dictionary

# def Merge(dict1, dict2):
#     res = {**dict1,**dict2}
#     return res
#
#
# # Driver code
# dict1 = {'a': 10, 'b': 8}
# dict2 = {'d': 6, 'c': 4}
# dict3 = (dict1, dict2)
# print(Merge(dict1,dict2))


#Python Merge Dictionaries Using | in Python 3.9

# def Merge(dict1,dict2):
#     res=dict1 | dict2
#     return res
#
# dict1 = {'x': 10, 'y': 8}
# dict2 = {'a': 6, 'b': 4}
# print(Merge(dict1,dict2))



#####sort dict by key n value
# dict1 = {'x': 10, 'y': 8}
# dict2 = {'a': 6, 'b': 4}
#
# print(dict1.values())
# print(dict1.keys())


########## looping
# d={1:'geek',2:'for',3:'Python'}
#
# for i,j in d.items():
#     print(i,j)



#exa:: accessing keys and value
#keys
# d={1:'geek',2:'for',3:'Python'}
#
# for i in d:
#     print(i)
# #for values
# for i in d:
#     print(d[i])

#or
# for i in d.values():
#     print(i)
# for i in d.keys():
#     print(i)
#
#access key and value at atime
# for x,y in d.items():
#     print(x,y)




#exa
# d={}
# x=int(input("how many pair u want to add : "))
#
# for i in range(1,x+1):
#     k=input("enter"+str(i)+"key :")
#     z=input("enter its value :")
#     d[k]=z
#     print(d)                                         doubt


#exa:access key
# test={"g":7,"f":8,"k":9}
# print(test.keys())             #dict_keys(['g', 'f', 'k'])
# print(test['k'])

#exa::update
# a={1:'nashik',2:'puna',3:'delhi'}
# a.update({4:'gujurat'})
# print(a)                              #{1: 'nashik', 2: 'puna', 3: 'delhi', 4: 'gujurat'}


## access key n value
# person = {"name": "John", "age": 30, "city": "New York"}
# for key,value in person.items():
#     print(key,':',value)


# access key using MAP
# x = {
#     'Gujarat': 'Gandhinagar',
#     'Maharashtra': 'Mumbai',
#     'Rajasthan': 'Jaipur',
#     'Bihar': 'Patna'
# }
#
# map_keys=map(x.get, x)
# for i in map_keys:
#     print(i)

#using zip
# data = {
#     'Gujarat': 'Gandhinagar',
#     'Maharashtra': 'Mumbai',
#     'Rajasthan': 'Jaipur',
#     'Bihar': 'Patna'
# }
# for x,y in zip(data.keys(),data.values()):
#     print(f'The capital of {x} is {y}')
#
### Iterate over nested dictionary ?
# data = {
#     'Student 1': {'Name': 'Bobby', 'Id': 1, "Age": 20},
#     'Student 2': {'Name': 'ojaswi', 'Id': 2, "Age": 22},
#     'Student 3': {'Name': 'rohith', 'Id': 3, "Age": 20},
# }
# for i in data:
#     print(i)
#
# for i in data:
#     print(data[i])
#
# for i in data:
#     print(data[i].keys())
#     print(data[i].values())


#######3  delete keys

# d = {1: 'Geeks', 2: 'For', 3: 'Geeks'}
#
# for key in d.keys():
#     if key==2:
#         del d[key]
# print(d)                                           doubt


# comprehension

# d = {1: 'Geeks', 2: 'For', 3: 'Geeks'}
# delete = [key for key in d if key == 3]
#
# # delete the key/s
# for key in delete:
#     del d[key]
#
# # Modified Dictionary
# print(d)


#exa

# d = {1: 'Geeks', 2: 'For', 3: 'Geeks'}
#
# delete=[]
# for key in d:
#     if key==3:
#         delete.append(key)
# print(delete)
#
# for i in delete:
#     del d[i]
# print(d)                       #doubt



#exa
# d = {1: 'Geeks', 2: 'For', 3: 'Geeks'}
#
# for key in list(d):
#     if key==2:
#         del d[key]
# print(d)


#exa
# d = {1: 'Geeks', 2: 'For', 3: 'Geeks'}
# d.pop(2)
# print(d)



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



# write a example of generator and iterator
#git stash
#y dict key is immutable
#what is pdm
#makemytrip automation
#even odd in list comprehension

#sorting
# x=[1,2,5,6,7,9,2,6,4,2,4,8,4,2]
#
# new=[]
# for k in x:
#     if k not in new:
#         new.append(k)
# print(new)          #[1, 2, 5, 6, 7, 9, 4, 8]
#
# for i in range(len(new)):
#     for j in
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

#hello
# x="hello"
# for i in x:
#     count=0
#     for j in range(len(x)):
#         if i==x[j]:
#             count+=1
#     print(i,count)


#output=h:1,e:1,l:2,o:1
# x="hello"
# uniq=[]
#
# for k in x:
#     if k not in uniq:
#         uniq.append(k)
# print(uniq)
#
# for i in x:
#     count=0
#     for j in range(len(x)):
#         if i==x[j]:
#             count+=1
#     print(i,count)

#####
# # # swap all upper to lower and lower to upper
# x='Hello Welcome to python'
# y=""

# for i in x:
#         y+=i.swapcase()
# print(y)

#or
# # swap all upper to lower and lower to upper
# x='Hello Welcome to python'
# y=[]
# for i in x:
#    if i.isupper():
#        y.append(i.lower())
#    elif i.islower():
#        y.append(i.upper())
#    else:
#        y.append(i)
# print("".join(y))

###
# # separate all value and numbers
# str1="hello wel1come t2o pyth4on"
# x=""
# y=""
#
# for i in str1:
#     if i.isalpha() or i.isspace():
#         x+=i
#     else:
#         y+=i
# print(x)            #hello welcome to python
# print(y)            #124

# #Fibonacci series
# x=0
# y=1
# for i in range(10):
#     z=x+y
#     x=y
#     y=z
#     print(z)

#amstrong
# n=153
# count=0
# z=str(n)
#
# for i in z:
#     k=int(i)**3
#     count+=k
# print(count)
#
# if n==count:
#     print("n is amstrong")
# else:
#     print("not amstrong")


###find the vowels count
# z="hello welcome to python"
# vowel="a,e,i,o,u"
# count=0
# for i in z:
#     if i in vowel:
#         count+=1
# print(count)

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

#####
# #remove first and last spaces
# x=" hello welcome to python "
# new=""
#
# for i in range(1,len(x)-1):
#     new+=x[i]
# print(new)



# #
# x=[5,9,6,8,3,2,4]
# y=[]
# z=1
# for i in range(len(x)):
#     y.append(x[-z])
#     z+=1
# print(y)

##
# Example 1: Print the first 10 natural numbers using for loop.
# n=10
# for i in range(1,n+1):
#     print(i)

## Python program to print all the even numbers within the given range.
# n=11
# for i in range(n):
#     if i%2==0:
#         print(i)

##
# Python program to calculate the sum of all numbers from 1 to a given number
# n=10
# count=0
# for i in range(1,n):
#     count+=i
# print(count)

## Python program to calculate the sum of all the odd numbers within the given range.
# n=10
# count=0
# z=[]
# for i in range(1,n+1):
#     if i%2==0:
#         z.append(i)
#         count+=i
# print(z)
# print(count)

##Python program to print a multiplication table of a given number
# n=5
# for i in range(1,11):
#     print(n,"*",i,"=",n*i)


#Python program to count the total number of digits in a number.
# n=12345
# count=0
# for i in range(len(str(n))):
#     count+=1
# print(count)

##Python program to check if the given string is a palindrome.
# name="MADAM"
# rev=""
# for i in name:
#     rev=i+rev
# print(rev)
# if name==rev:
#     print("palindrom")
# else:
#     print("not palindrom")


# Python program that accepts a word from the user and reverses it.
# user=input("enter name :")
# rev_user=""
# for i in user:
#     rev_user=i+rev_user
# print(rev_user)

# Example 11: Python program to count the number of even and odd numbers from a series of numbers.
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
#
# for i in range(len(x)):    #0,1,2,3,4,5=6
#     for j in range(i+1,len(x)):  #1 to 6
#         if x[i]>x[j]:
#             x[i],x[j]=x[j],x[i]
# print(x)


##check prime number
# n=10
# for i in range(2,n+1):
#     if n%i==0:
#         print(i,"not prime")
#     else:
#         print(i,"prime")          #doubt


##Count number of vowels in a String in Python
# name="geek for python"
# vowel="a,e,i,o,u"
# count = 0
# vol_count=""
# for i in name:
#     if i in vowel:
#         vol_count+=i
#         count+=1
# print(count)


###ABAABBCA
#ans. 4A3B1C
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
















