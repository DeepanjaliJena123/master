#is an unordered collection data type that is iterable, mutable and has no duplicate elements.
# A set is a collection which is unordered, unchangeable*, and unindexed.
# # TypeError: 'set' object does not support item assignment
#  we cannot assign or change a value once the set is created.
# # We can only add or delete items in the set.
#exa:
# var={"geek","for","python"}
# print(var)

#Type Casting with Python Set method
# myset=set(["a","b","c"])
# print(myset)
#
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
#
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
#
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

