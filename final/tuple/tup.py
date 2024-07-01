######  TUPLE ##########.
#A tuple is ordered and unchnageable.
#it writtens in round brackets().
#tuple is immutable.
#can not modify,append,insert and remove.

# tp=('a','b','c')
# print(tp)

# ls=[1,2,3,4,5]
# print(tuple(ls))
#
# t=tuple("geeks")
# print(t)

#exa
# tp1=('a','b')
# tp2=(1,2,3)
# tp3=(tp1,tp2)
# print(tp3)        #(('a', 'b'), (1, 2, 3))




#exa
# tpl=("geeks",)*3
# print(tpl)           #('geeks', 'geeks', 'geeks')


#exa
# tuple=("geeks")
# n=5
# for i in range(int(n)):
#     tuple=(tuple,)
#     print(tuple)
# ('geeks',)
# (('geeks',),)
# ((('geeks',),),)
# (((('geeks',),),),)
# ((((('geeks',),),),),)

#exa accessing
# tuple=("geeks")
# print(tuple[0])

## Tuple unpacking
# tup=("geeks","for","teep")
# a,b,c=tup
# print(a)
# print(b)
# print(c)

#concatination

# tp1=("geek","feek")
# tp2=(1,2,3)
# tp3=tp1+tp2
# print(tp3)

#slicing
# tp=tuple("geeks")
# print(tp[1:])
# #reverse
# print(tp[::-1])

#index
#
# animals=["dog","cat","rat"]
# print(animals.index("dog"))

# list1 = [1, 2, 3, 4, 1, 1, 1, 4, 5]
# print(list1.index(4,4,8))
#
# list1 = [6, 8, 5, 6, 1, 2]
# print(list1.index(6,1))

# li=[1,2,3,4,5]
# for i in range(6):
#     print(li[i])


##exa  Creating a Tuple with Mixed Datatypes.
# tup1=(1,2,3)
# tup2=("geek","for","python")
# tup3=(tup1,tup2)
# print(tup3)

#with repetition
# tup1=("geek",)*3
# print(tup1)

#using loop
# tup1=("geek")
# n=5
# for i in range(int(n)):
#     tup1=(tup1,)
#     print(tup1)

# #exa
# tup1=("Geek")
# print(tup1[0])

# Tuple unpacking
# tup1=("geek","for","python")
# a,b,c=tup1
# print(a)
# print(b)
# print(c)

#exa::Concatenation of Tuples
# tup1=(1,2,3)
# tup2=("g","y","p")
# tup3=tup1+tup2
# print(tup3)

#Slicing of Tuple::
# Tuple1 = tuple('GEEKSFORGEEKS')
# print(Tuple1[1:])
# print(Tuple1[::-1])
# print(Tuple1[4:9])


#INDEX using loop
# li = [1, 5, 3, 2, 4]
# count=0
#
# for num in li:
#     count+=1
# for i in range(count):
#     print(li[i])

#count
# lst = ['Cat', 'Bat', 'Sat', 'Cat', 'Mat', 'Cat', 'Sat']
# print([[l,lst.count(l)] for l in set(lst)])
# print(dict((l,lst.count(l))for l in set(lst)))

#sum
# numbers = [1,2,3,4,5,1,4,5]
# Sum=sum(numbers)
# print(Sum)               #25
#
# Sum=sum(numbers,10)
# print(Sum)


#exa
# my_dict = {'a': 10, 'b': 20, 'c': 30}
# Total=sum(my_dict.values())
# print(Total)                   #60

#exa:: sum on a set
# my_set = {1, 2, 3, 4, 5}
# print(sum(my_set))
#

#exa::sum on tuple
# tup1=(1,2,3)
# print(sum(tup1))      #6

#exa::loop
# numbers = [10, 20, 30, 40, 50]
# total=0
#
# for num in numbers:
#     total+=num
# print(total)

#average
# numbers = [1,2,3,4,5,1,4,5]
# Sum=sum(numbers)
# average=Sum/len(numbers)
# print(average)

##    sort
# print(sorted([1,5,3,10,0,7]))

#exa
# s=[1,5,60,10,8,50]
# print(sorted(s))

#exa
# s=[1,5,60,10,8,50]
# print(sorted(s,reverse=True))

#exa
# k="geekforpython"
#
# res="".join(sorted(k,reverse=True))
# print(res)

#exa
# import functools
# k="geekforpython"
#
# res=functools.reduce(lambda x,y:x+y,sorted(k,reverse=True))
# print(res)

#exa
# L = ["cccc", "b", "dd", "aaa"]
# print("the sorted L is :",sorted(L))
# print("The len wise sorted :",sorted(L,key=len))


#EXA
# d="hello,world!"
# ds=sorted(d)
# print(ds)

#exa::
# my_tuples = [(1, "one"), (3, "three"), (2, "two"), (4, "four")]
# new=sorted(my_tuples,key=lambda x:x[1])
# print(new)

#exa
# students = [
#     {'name': 'John', 'age': 20},
#     {'name': 'Alice', 'age': 18},
#     {'name': 'Bob', 'age': 22} ]
#
# res=sorted(students,key=lambda x:x["age"])
# print(res)
#




