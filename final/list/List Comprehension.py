# Python – List Comprehension
# easy to read, compact, and elegant way of creating a list from any existing iterable object
#or proveds a certain syntax while creating a new list from the exsting list.

# exa: increment 2
# s=[10,20,30,40,50]
# new=[]
# for i in s:
#     new.append(i+2)
# print(new)

#or
#comprehesion:
# s=[10,20,30,40,50]
# new=[i+2 for i in s]
# print(new)
#exa:find out even number
# cube=[]
# for i in range(11):
#     if i%2==0:
#         cube.append(i**3)
# print(cube)

# #comprehension
# new=[x**3 for x in range(11) if x%2==0]
# print(new)
#exa
# numbers=[12,13,15,16]
# doubles=[x*2 for x in numbers]
# print(doubles)

#exa:
# ch=[i for i in [1,2,3]]
# print(ch)

#exa"
# matrix=[[j for j in range(3)] for i in range(3)]
# print(matrix)

#exa:
# new=[]
# for i in "geekforgeek":
#     new.append(i)
# print(new)

#exa:
# num=list(map(lambda i:i*10,[i for i in range(1,6)]))
# print(num)







