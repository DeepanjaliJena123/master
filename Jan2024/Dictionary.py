#a dictinary is a collection which is unordered,changeble and indexed.
#dictionary is mutable
#the dictionary are written with curly brackets, and have key and values {}.
# Duplicates Not Allowed
# Dictionaries cannot have two items with the same key:

#exa
# var={"geek","for","python"}
# print(var)

#Type Casting with Python Set method
# myset=set(["a","b","c"])
# print(myset)
#
# myset.add("d")
# print(myset)


### a set cannot have duplicate values
# set1={"geek","for","geek"}
# print(set1)


##Heterogeneous Element with Python Set
# myset = {"Geeks", "for", 10, 52.7, True}
# print(myset)

#Python Frozen Sets
# d=set(['e','g','f'])
# print(d)
# s=frozenset(['a','k','b'])
# print(s)


#exa::  add

# people = {"Jay", "Idrish", "Archi"}
# print("people:",end="")
# print(people)
#
# people.add("daxit")
#
# for i in range(1,6):
#     people.add(i)
# print(people)

## union
# people = {"Jay", "Idrish", "Archil"}
# vampires = {"Karan", "Arjun"}
# dracula = {"Deepanshu", "Raju"}
#
# population=people.union(vampires)
# print(population)
#
# population=people|dracula
# print(population)


## Intersection operation on Python Sets
# set1=set()
# set2=set()
#
# for i in range(5):
#     set1.add(i)
#
# for i in range(3,9):
#     set2.add(i)
#
# set3=set1.intersection(set2)
# print(set3)
#
# #or & operator
# set3=set1 & set2
# print(set3)

##Finding Differences of Sets in Python
# set1 = set()
# set2 = set()
#
# for i in range(5):
#     set1.add(i)
#
# for i in range(3, 9):
#     set2.add(i)
#
# # set3=set1.difference(set2)
# # print(set3)
#
# set3=set1-set2
# print(set3)


# #####  Clearing Python Sets
# set1 = {1,2,3,4,5,6}
# set1.clear()
# print(set1)


##   update

# set1={1,2,3}
# set2={"a","b","c"}
# set1.update(set2)
# print(set1)
#
# # Using | Operator (Pipe Operator)
# set1 |=set(set2)
# print(set1)





















