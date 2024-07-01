
#exa
# x=['m','k','a','e','o','s','i','l']
# y=['a','e','i','o','u']
#
# new=[]
# for i in x:
#     for j in y:
#         if i==j:
#             new.append(i)
# print(new)

#exa: ######### star pattern
# *
# **
# ***
# ****

# for i in range(1,5):
#     for j in range(1,i+1):
#         print("*",end="")
#     print("\r")

#exa:
# *****
# ****
# ***
# **
# *

# for i in range(6,0,-1):
#     for j in range(1,i+1):
#         print("*",end="")
#     print("\r")

#exa: sort by ascending order
# l1 = [76, 23, 45, 12, 54, 9]
# print("Original List:", l1)
#
# # sorting list using nested loops
# for i in range(0, len(l1)):
#     for j in range(i + 1, len(l1)):
#         if l1[i] >= l1[j]:
#             l1[i], l1[j] = l1[j], l1[i]
#
# # sorted list
# print("Sorted List", l1)

#exa
# for i in range(2):
#     print(i)
#     for j in range(10,13):
#         print(j)


#exa
# list_fruit=['apple','mango','grapes','orange']
# for fruit in list_fruit:
#     for i in fruit:
#         print(i,end="@")
#     print('\r')

#exa
# color=['red','green','blue']
# item=['apple','vaggies','shirts']
#
# for i in color:
#     for j in item:
#         print(i,j)
#         print('')

#exa append two list:
# z=[]
# x=[10,20,30,40]
# y=[50,60,70,80]
# for i in x:
#     for j in y:
#         z.append(i+j)
# print(z)

#exa:multiplying two list
# x=[2,4,6]
# y=[2,4,6]
# for i in x:
#     for j in y:
#         if i==j:
#             continue
#         print(i,'*',j,'=',i*j)



#exa:
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

# for i in range(1,5):
#     for j in range(1,i+1):
#         print(j,end='')
#     print()

#Exa
# 4444
# 333
# 22
# 1
# for i in range(4,0,-1):
#     for j in range(1,i+1):
#         print(i,end='')
#     print()


#exa:
# ****
# ***
# **
# *
# for i in range(4,0,-1):
#     for j in range(1,i+1):
#         print('*',end='')
#     print()


#exa
# 1
# 22
# 333
# 4444
# 55555

# for i in range(1,6):
#     for j in range(1,i+1):
#         print(i,end="")
#     print()

#exa
# 11111
# 2222
# 333
# 44
# 5
#
# n=0
# for i in range(5,0,-1):
#     n+=1
#     for j in range(1,i+1):
#         print(n,end="")
#     print()

#exa:
# 55555
# 5555
# 555
# 55
# 5
# n=5
# for i in range(5,0,-1):
#     for j in range(1,i+1):
#         print(n,end="")
#     print()

#exa:
# 1
# 2 1
# 3 2 1
# 4 3 2 1
# 5 4 3 2 1

# for i in range(1,6):
#     for j in range(i,0,-1):
#         print(j,end=" ")
#     print()

#exa
# 0 1 2 3 4 5
# 0 1 2 3 4
# 0 1 2 3
# 0 1 2
# 0 1

# for i in range(5,0,-1):
#     for j in range(0,i+1):
#         print(j,end=" ")
#     print()

#exa:
# 1
# 2 3 4
# 5 6 7 8 9

# n=1
# c=0
# for i in range(1,10):
#     c+=1
#     for j in range(n,n+1):
#         print(j,end=" ")
#         n=n+1
#     print()












