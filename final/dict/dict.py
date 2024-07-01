#a dictinary is a collection which is unordered,changeble and indexed.
#dictionary is mutable
#the dictionary are written with curly brackets, and have key and values {}.
#dictionaries are ordered and can not contain duplicate keys.

#exa
# dict={1:'geek',2:'for',3:'geek'}
# print(dict)

#exa
# dict={'name':"geeks",1:[1,2,3]}
# print(dict)

#exa:Dictionary with the use of dict()
# dict=dict({1:'geek',2:'for',3:'geek'})
# print(dict)   #{1: 'geek', 2: 'for', 3: 'geek'}

#exa: Dictionary with each item as a pair:
# Dict = dict([(1, 'Geeks'), (2, 'For')])
# print(Dict)        #{1: 'Geeks', 2: 'For'}

#nested dictionary
# dict={1:"geek",2:"for",3:{'a':'wlcome','b':'to',"c":"geeks"}}
# print(dict)
#exa
# dict={}
# dict[1]='geek'
# dict[2]='python'
# dict[3]=10
# print(dict)
# #
# #
#exa: accessing element
# dict = {1: 'Geeks', 'name': 'For', 3: 'Geeks'}
# print(dict['name'])
# print(dict[1])


#exa:Access a Value in Dictionary using get() in Python
# dict={1: 'Geeks', 'name': 'For', 3: 'Geeks'}
# # print(dict.get(3))

#exa: Accessing an Element of a Nested Dictionary
# dict = {'dict1': {1: 'Geeks'},
#         'dict2': {'Name': 'For'}}
# print(dict['dict1'])
# print(dict['dict1'][1])
# print(dict['dict2']['Name'])


#exa:: Deleting Elements using ‘dFor',el’ Keyword
# dict = {1: 'Geeks', 'name':'klj','l':'java'}
# # print(dict)
# del (dict[1])
# print(dict)

#exa clear
# dict = {1: 'Geeks', 'name': 'For', 3: 'Geeks'}
# dict.clear()
# print(dict)

#exa copy
# dict = {1: 'Geeks', 'name': 'For', 3: 'Geeks'}
# dict2=dict.copy()
# print(dict2)

#exa: Returns a list containing a tuple for each key value pair
# dict = {1: 'Geeks', 'name': 'For', 3: 'Geeks'}
# print(dict.items())                ###dict_items([(1, 'geek'), ('name', 'for'), (3, 'sdjhfjh')])

#exa:  Returns a list containing dictionary’s keys
# dict = {1: 'Geeks', 'name': 'For', 3: 'Geeks'}
# print(dict.keys())
# print(dict.values())

#exa:
dict = {1: 'Geeks', 'name': 'For', 3: 'Geeks'}
# dict.update({'4': 'python'})
# print(dict)
#
# #pop
# dict = {1: 'Geeks', 'name': 'For', 3: 'Geeks'}
# dict.pop(3)
# print(dict)

#popitems
# dict = {1: 'Geeks', 'name': 'For', 3: 'Geeks'}
# dict.popitem()
# print(dict)

#exa:get values
# dict = {1: 'Geeks', 'name': 'For', 3: 'Geeks'}
# print(dict.values())

## maerging 2 dictionary using methods
# def Merge(dict1, dict2):
#     return (dict2.update(dict1))
#
# #
# # # Driver code
# dict1 = {'a': 10, 'b': 8}
# dict2 = {'d': 6, 'c': 4}
#
# # This returns None
# print(Merge(dict1, dict2))
# #
# # changes made in dict2
# print(dict2)

#exa: change value in dictionary
# dict={'a':1,'b':2,'c':3}
# print(dict)
# dict['c']=5   #changed value
# print(dict)

#exa: want key and value
# dict={'a':1,'b':2,'c':3}
# for x,y in dict.items():
#     print(x,y)

#add item in dict
# dict={'a':1,'b':2,'c':3}
# dict['d']=10
# print(dict)
#
#Merge Dictionaries
# dict1 = {'a': 1, 'b': 2}
# dict2 = {'c': 3, 'd': 4}
# dict1.update(dict2)
# print(dict1)

#
# def student(firstname, lastname):
#     print(firstname, lastname)
#
#
# # Keyword arguments
# student(firstname='Geeks', lastname='Practice')
# student(lastname='Practice', firstname='Geeks')
















########

# def addition(*args):
#     total_add = 0
#     for i in args:
#         total_add+=i
#     print(total_add)
#
# def subtract(*args):
#     total_sub = 0
#     for i in args:
#         total_sub=i-total_sub
#     print(total_sub)
#
# addition(1,2,3,4)
#
# subtract(5,8)














