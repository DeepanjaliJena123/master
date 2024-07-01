#list is a collection which is orderd and chnagable
#list are mutable.[]
#The list is a sequence data type which is used to store the collection of data.
# lists are defined by having values between square brackets [ ] .
#creat
# list=[10,20,30]
# print(list)
# #accessing
# print(list[0])
# print(list[2])
import functools
# Accessing elements from a multi-dimensional list
# ls=[["geeks","for"],["python","java"]]
# print(ls)
# print(ls[0])    #['geeks', 'for']
# print(ls[1])    #['python', 'java']
# print(ls[0][0])   #geeks
# print(ls[1][0])   #python
# print(len(ls))

# ##List = [['Geeks', 'For'], ['PYTHON']]
# k=[]
# # print(List[0][1])
# # print(List[1][0])
#
# for i in List:
#     for j in i:
#         k.append(j)
# print(k)


#Taking Input of a Python List
# lss=input("Enter the element: ")
# l=lss.split()
# print("The list is :",l)

#Enter the element: geek for geeksss
#The list is : ['geek', 'for', 'geeksss']

####    Append()          #####
#Add an element to the end of the list

###   Extend vs Append Python List Methods
#In Python, there are two ways to add elements to a list: extend() and append()
#However, these two methods serve quite different functions
## In append():: we add a single element to the end of a list
##In extend()::we add multiple elements to a list
#exa:1
# x=["geeks","for"]
# x.append("python")
# print(x)            #['geeks', 'for', 'python']

#exa:2
# ls=["geeks","for","seek"]
# ls1=[1,2,3,4]
# ls.append(ls1)
# print(ls)               #['geeks', 'for', 'seek', [1, 2, 3, 4]]

#exa:3
# ls=["geeks","for"]
# ls1=[1,2,3,4,5]
# ls.extend(ls1)
# print(ls)           #['geeks', 'for', 1, 2, 3, 4, 5]

#exa:4
# ls=["geeks","for"]
# ls.extend("python")
# print(ls)              #['geeks', 'for', 'p', 'y', 't', 'h', 'o', 'n']

#####  insert()  ######
#Insert an item at the defined index
#del
# lis=[1,6,4,3,5,9,2,7]
# del lis [2:5]
# print(lis)             #[1, 6, 9, 2, 7]

#insert
# k=[1,2,3,4]
# k.insert(2,8)
# print(k)              #[1, 2, 8, 3, 4]

#remove
# k=[1,2,3,4,]
# k.remove(1)
# print(k)          #[2, 3, 4]

#sort
# g=[1,8,6,3,5,2]
# g.sort()
# print(g)           #[1, 2, 3, 5, 6, 8]

#reverse
# r=[1,8,6,3,5,2]
# r.reverse()
# print(r)
#
#clear
# j=[2,8,9,7]
# j.clear()
# print(j)

#index
# animals=["dog","snake","tiger","cat"]
# print(animals.index("cat"))           #3


#count
#exa1
# ls=['b','c','d','b','k']
# print(ls.count('b'))        #2

#exa2
# list1 = [ ('Cat', 'Bat'), ('Sat', 'Cat'), ('Cat', 'Bat'),
#           ('Cat', 'Bat', 'Sat'), [1, 2], [1, 2, 3], [1, 2] ]
# print(list1.count(('Cat', 'Bat')))   #2
# print(list1.count([1, 2]))          #2

#exa3
# lst = ['Cat', 'Bat', 'Sat', 'Cat', 'Mat', 'Cat', 'Sat']
#
# print([[l,lst.count(l)] for l in set(lst)])
# print(dict((l,lst.count(l)) for l in set(lst)))

#sort
#The sort function can be used to sort the list in both ascending and descending order
#
# s=[1,2,8,6,9,7,20,21,12]
# s.sort()
# print(s)                    #[1, 2, 6, 7, 8, 9, 12, 20, 21]

#sort n reversed
# k=[2,5,4,6,9,10]
# k.sort(reverse=True)         #[10, 9, 6, 5, 4, 2]
# print(k)

# def sortSecond(val):
#     return val[1]
#
#
# # list1 to demonstrate the use of sorting
# # using second key
# list1 = [(1, 2), (3, 3), (1, 1)]
#
# # sorts the array in ascending according to
# # second element
# list1.sort(key=sortSecond)
# print(list1)
#
# # sorts the array in descending according to
# # second element
# list1.sort(key=sortSecond, reverse=True)
# print(list1)                                                                  ######doubt


#sorted

# s=[2,8,9,3,7,15,11]
# print(sorted(s))
#
# print(sorted(s,reverse=True))
#
# x = {'q': 1, 'w': 2, 'e': 3, 'r': 4, 't': 5, 'y': 6}
# print(sorted(x))


# L = ['aaaa', 'bbb', 'cc', 'd']
# print(sorted(L))
# print(sorted(L,key=len))

#copy
# a=['mango','grapes','banana']
# b=a.copy()
# print("The new created list : " + str(b))

#pop()
# a=['mango','grapes','cherry']
# a.pop()
# print(a)

### reduce
# functools.reduce() function in Python to compute the sum and maximum element of a list

#exa max element n sum

# import functools
#
# lis=[1,3,5,6,2]
#
# print("The sum of the element is : ",end="")
# print(functools.reduce(lambda a,b: a+b,lis))
# print("The maximum element is : ",end="")
# print(functools.reduce(lambda a,b: a if a>b else b,lis))

#operator.add
# import operator
#
# lis=[1,3,5,2,6]
#
# print("sum of the elements is : ",end="")
# print(functools.reduce(operator.add,lis))
#
# print("The product of list element is : ",end="")
# print(functools.reduce(operator.mul,lis))
#
# print(functools.reduce(operator.add,["geeks","for"]))

#exa : accumulate

# import itertools
# import functools
# ls=[1,5,6,3,4]
#
# print(list(itertools.accumulate(ls,lambda x,y: x+y)))
#
# print(functools.reduce(lambda x,y:x+y,ls))

## sum :
#
# numbers=[1,2,3,4,5]
# # sum=sum(numbers)
# # print(sum)
#
# sum_num=sum(numbers,10)
# print(sum_num)

#exa
# my_dict={'a':10,'b':20,'c':30}
# total=sum(my_dict.values())
# print(total)

#exa
# my_set={1,2,3,4,5,6}
# print(sum(my_set))

#exa
# my_tuple=(3,5,8)
# print(sum(my_tuple))

#exa
# numbers=[3,5,2]
# total=0
#
# for num in numbers:
#     total+=num
# print("The total number is :",total)

# check avarage
# numbers=[1,2,3,4,5]
# sum=sum(numbers)
# print(sum)
#
# avarage=sum/len(numbers)
# print(avarage)

#comparision

# list1 = [1, 2, 4, 3]
# list2 = [1, 2, 5, 8]
# list3 = [1, 2, 5, 8, 10]
# list4 = [1, 2, 4, 3]
# list5 = [7, 2, 5, 8]
#
# print("Comparison of list2 with list1 : ")
# print(cmp(list2, list1))                          #doubt

#min
# square = {5: 25, 8: 64, 2: 4, 3: 9, -1: 1, -2: 4}
# print("The smallest key is:",min(square))
#
# key2=min(square,key=lambda k:square[k])
#
# print("The smallest value is:",square[key2])


#filtered
#filter even n odd

# seq=[1,0,2,4,6,8,9,3]
#
# result=filter(lambda x : x % 2 !=0,seq)
# print(list(result))
#
# result=filter(lambda x: x%2==0,seq)
# print(list(result))


### filter

# def fun(variable):
#     letter= ['a', 'e', 'i', 'o', 'u']
#
#     if variable in letter:
#         return True
#     else:
#         return False
#
# sequence = ['g', 'e', 'e', 'j', 'k', 's', 'p', 'r']
#
# filtered=filter(fun,sequence)
# print("The filter value is: ")
# for s in filtered:
#     print(s)

#exa :  find even n odd using filter
# seq=[1,3,8,2,4,7,9]
#
# result=filter(lambda x: x%2!=0,seq)
# print("odd number :",end="")
# print(list(result))
#
# result=filter(lambda x: x%2==0,seq)
# print("even number :",end="")
# print(list(result))

#######  MAP
###### Addition

# def addition(n):
#     return n+n
#
# numbers=[1,2,3,4]
# result=list(map(addition,numbers))
# print(result)

## using lambda ,addition
# numbers=[1,2,3,4]
# result=map(lambda x: x+x,numbers)
# print(list(result))

### add two list using map

# num1=[1,2,3]
# num2=[2,4,6]
#
# result=map(lambda x,y: x+y,num1,num2)
# print(list(result))            ######[3, 6, 9]


#### # map() can listify the list of strings individually

# l = ['sat', 'bat', 'cat', 'mat']
# test = list(map(list, l))
# print(test)
# output:  [['c', 'a', 't'], ['b', 'a', 't'], ['s', 'a', 't'], ['m', 'a', 't']]

#####  # Define a function that doubles even numbers and leaves odd numbers as is

# def double_even(num):
#     if num%2==0:
#         return num*2
#     else:
#         return num
#
# numbers=[1,2,3,5,6]
#
# result=list(map(double_even,numbers))
# print(result)


#####33 lambda ###########
# str1="geeksforgeek"
#
# result=lambda string: string.upper()
# print(result(str1))

#exa:upper
# animals = ['dog', 'cat', 'parrot', 'rabbit']
# upper_animal=list(map(lambda animal: animal.upper(),animals))
# print(upper_animal)
#


### accessing

# List = [['Geeks', 'For'], ['Geeks']]
#
# print(List[0][1])
# print(List[1][0])


# #Taking Input of a Python List
# string=input("enter the number :")
#
# str=string.split()
# print("The splited number is :",str)
#The splited number is : ['Geeks', 'for', 'python']


### exa
# n=int(input("Enter the size of the list : "))
#
# lst=list(map(int,input("Enter the intizer element :").strip().split()))[:n]
#
# print("The list is :",lst)

##adding element in list
# ls=[]
#
# ls.append(1)
# ls.append(2)
# ls.append(3)
#
# print(ls)

#looping
# ls=[]
# for i in range(1,5):
#     ls.append(i)
# print(ls)
#
# ls.append((5,6))
# print(ls)
#
# ls2=["geek","for"]
# ls.append(ls2)
# print(ls)

#insert
# l=[2,3,4,5]
#
# l.insert(5,10)
# l.insert(0,"python")
# print(l)

#extend
# ls=[1,2,3,4]
# ls2=[5,"geek","for"]
# ls.extend(ls2)
# print(ls)

#reverse
# mylist=[1,2,3,"geeks","for"]
# mylist.reverse()
# print(mylist)

# s=["m","k","p"]
# ss=list(reversed(s))
# print(ss)

#remove

# ls=[10,5,3,20,35,4,30]
# ls.remove(3)
# ls.remove(30)
# print(ls)

#pop

# s=[2,3,4,5]
# s.pop()
# print(s)
# s.pop(2)
# print(s)

#odd square numbers double

# odd_squre=[]
#
# for i in range(1,11):
#     if i%2==1:
#      odd_squre.append(i**2)
# print(odd_squre)

## remove dulicate form list
# lis=[1,3,5,6,4,4,2,2,7,7]
# k=[]
#
# for i in lis:
#     if i not in k:
#         k.append(i)
# print(k)


s1="hello,kello,hello,hello,nello,nello"

s2="hello"
# k=s1.count(s2)
# print(k)

#or
# count=0
# m=s1.split(',')
# print(m)

# for i in m:
#     if s2 in i:
#         count+=1
# print(count)

#or
# for i in range(len(m)):
#     if s2==m[i]:
#         count+=1
# print(count)


