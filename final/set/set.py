#is an unordered collection data type that is iterable, mutable and has no duplicate elements.
#values of set can not be changed
#a set can not have duplicate value


#exa:
# var={"geek","for","python"}
# print(var)

#Type Casting with Python Set method
# myset=set(["a","b","c"])
# print(myset)

# myset.add("d")
# print(myset)

#exa: a set can not have duplicate value
# myset1={"geek","for","geek"}
# print(myset1)

#values of set can not be changed
# myset1[1]="hello"
# print(myset1)              ###TypeError: 'set' object does not support item assignment
# del myset1
# print(myset1)

###  The second code generates an error because
# we cannot assign or change a value once the set is created.
# We can only add or delete items in the set.


#exa  Heterogeneous Element with Python Set
# set2={'a',2,2,10.2,True}
# print(set2)


#exa:  Python Frozen Sets
# Frozen sets in Python are immutable
# set1={"a","b","c"}
# frozen_set2=frozenset(["a","f","n"])
# print(frozen_set2)

## Adding elements to Python Sets
# people = {"Jay", "Idrish", "Archi"}
# print("people:",end="")
# print(people)
#
# people.add("daxit")
# print(people)

# for i in range(1,5):
#     people.add(i)
# print(people)


## Union operation on Python Sets
# Two sets can be merged using union() function or | operator

# people = {"Jay", "Idrish", "Archil"}
# vampires = {"Karan", "Arjun"}
# dracula = {"Deepanshu", "Raju"}
#
# population=people.union(vampires)
# print(population)
#
# population=people|dracula
# print(population)

# Intersection operation on Python Sets
# This can be done through intersection() or & operator
#
# set1=set()
# set2=set()
#
# for i in range(5):
#     set1.add(i)
# print(set1)
#
# for i in range(3,9):
#     set2.add(i)
# print(set2)
#
# set3=set1.intersection(set2)
# print(set3)
# #
# set3= set1 & set2
# print(set3)

##  Finding Differences of Sets in Python
# To find differences between sets.
# Similar to finding differences in the linked list.
# This is done through difference() or – operator

#
# set1=set()
# set2=set()
#
# for i in range(5):
#     set1.add(i)
# print(set1)
#
# for i in range(3,9):
#     set2.add(i)
# print(set2)
#
# set3=set1.difference(set2)
# print(set3)
#
# set3=set1-set2
# print(set3)


#exa
# Clearing Python Sets
# Set Clear() method empties the whole set inplace.

# set1 = {1,2,3,4,5,6}
# set1.clear()
# print(set1)
#


#######    Append Multiple Elements in Set in Python

# Using update() Method
# set1={1,2,3,5,6}
# set2={9,7}
# set1.update(set2)
# print(set1)

# Using | Operator (Pipe Operator)
# set1={1,2,3,5,6}
# set2={9,7}
#
# set1 |= set(set2)
# print(set1)


##################################33

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





