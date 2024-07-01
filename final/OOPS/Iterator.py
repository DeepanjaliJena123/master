########  W3schools
##iterator is an object that allows you to iterate over collections of data, such as lists, tuples, dictionaries, and sets.

#Iterator vs Iterable
# Lists, tuples, dictionaries, and sets are all iterable objects.
# They are iterable containers which you can get an iterator from,
# All these objects have a iter() method which is used to get an iterator:

#exa
# x=[1,2,3,4]
# iterlist=iter(x)
# print(next(iterlist))
# print(next(iterlist))

# #EXA
# mytuple=("apple","banana","mango")
# myit=iter(mytuple)
# print(next(myit))   #apple
# print(next(myit))   #banana
# print(next(myit))   #mango
#exa2
# Even strings are iterable objects, and can return an iterator:
# mystring="BANANA"
# myit=iter(mystring)
# print(next(myit))   #B
# print(next(myit))   #A
# print(next(myit))   #N
# print(next(myit))   #A
# print(next(myit))   #N
# print(next(myit))   #A

#EXA3
# As you have learned in the Python Classes/Objects chapter, all classes have a function called __init__(),
# which allows you to do some initializing when the object is being created.
# The __iter__() method acts similar, you can do operations (initializing etc.), but must always return the iterator object itself.
# The __next__() method also allows you to do operations, and must return the next item in the sequence.
#

# class MyNumbers:
#   def __iter__(self):
#     self.a = 1
#     return self
#
#   def __next__(self):
#     x = self.a
#     self.a += 1
#     return x
#
# myclass = MyNumbers()
# myiter = iter(myclass)
#
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))


#exa4 #StopIteration

# class Myclass:
#     def __iter__(self):
#         self.a=1
#         return self
#
#     def __next__(self):
#         x=self.a
#         if self.a<=20:
#             self.a+=1
#             return x
#         else:
#             raise StopIteration
# obj=Myclass()
# myiter=iter(obj)
#
# for i in myiter:
#     print(i)

################# Geeks and geek #############################
# __iter__(): The iter() method is called for the initialization of an iterator. This returns an iterator object
#__next__(): The next method returns the next value for the iterable.
# When we use a for loop to traverse any iterable object, internally it uses the iter() method to get an iterator object,
# which further uses the next() method to iterate over. This method raises a StopIteration to signal the end of the iteration.

#exa1
# string="ABC"
# ch_iterator=iter(string)
# print(next(ch_iterator))
# print(next(ch_iterator))
# print(next(ch_iterator))
#
#

######  Creating and looping over an iterator using iter() and next()

# The __next__() method will raise a StopIteration exception if there are no further elements available.
# The for loop will terminate as soon as it catches a StopIteration exception.
# Let’s call the __next__() method using the next() built-in function.

 #Function ‘iterable’ will return True if the object ‘obj’ is an iterable and False otherwise.

# cities = ["Berlin", "Vienna", "Zurich"]
#
# # initialize the object
# iterator_obj = iter(cities)
#
# print(next(iterator_obj))
# print(next(iterator_obj))
# print(next(iterator_obj))
#
# Note: If ‘next(iterator_obj)’ is called one more time, it would return ‘StopIteration’.
#
#exaCheck object is iterable or not.
# def it(ob):
#     try:
#         iter(ob)
#         return True
#     except TypeError:
#         return False
# for i in [34,[2,8],(8,9,6),20,14,7]:
#     print(i," is iterable",it(i))            #doubt


#


######################## --getitem ##########3
# __getitem__() is a magic method in Python, which when used in a class,
# allows its instances to use the [] (indexer) operators.
# Say x is an instance of this class, then x[i] is roughly equivalent to type(x).__getitem__(x, i).

# If we want to add a and b, we write the following syntax:
# c = a + b
# Internally it is called as:
# c = a.__add__(b)

# The method __getitem__(self, key) defines behavior for when an item is accessed, using the notation self[key].
# This is also part of both the mutable and immutable container protocols.

#exa
# class Test():
#     def __getitem__(self, item):
#         print(type(item),item)
#
# obj=Test()
# obj[5]
# obj[10.5]
# obj[5:10]
# obj["geek"]

#########  Iterable vs Iterator  ##########
# tup=('a','b','c')
# for item in tup:
#     print(item)

# # Iterating on an iterator
# tup=('a','b','c','d','e')
# tup_iter=iter(tup)
#
# print("Inside loop :")
# for index,item in enumerate(tup_iter):
#     print(item)
#     if index==2:
#         break
# print("Outside of loop")
# print(next(tup_iter))
# print(next(tup_iter))

# x="a,b,c,d,e,f"
# myit=iter(x)
#
# for index, item in enumerate(myit):
#     print(item)
#     if index==2:
#         break
# print("out of loop")                                doubt

#exa
# Getting StopIteration Error while using iterator
#
# Iterable in Python can be iterated over multiple times, but iterators raise StopIteration Error when all items are already iterated.
# Here, we are trying to get the next element from the iterator after the completion of the for-loop.
# Since the iterator is already exhausted, it raises a StopIteration Exception.
# Whereas, using an iterable, we can iterate on multiple times using for loop or can get items using indexing.
#

# iterable = (1, 2, 3, 4)
# iterator_obj = iter(iterable)
#
# print("Iterable loop 1:")
# # iterating on iterable
# for item in iterable:
#     print(item, end=",")
#
# print("\nIterable Loop 2:")
# for item in iterable:
#     print(item, end=",")
#
# print("\nIterating on an iterator:")
# # iterating on an iterator object multiple times
# for item in iterator_obj:
#     print(item, end=",")
#
# print("\nIterator: Outside loop")
# # this line will raise StopIteration Exception
# # since all items are iterated in the previous for-loop
# print(next(iterator_obj))



