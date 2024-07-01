########  Forloop

# Looping means repeating something over and
# over until a particular condition is satisfied. A for loop in Python is a control flow statement
# that is used to repeatedly execute a group of statements as long as the condition is satisfied.

# s=["geek","for","python"]
#
# for i in s:
#     print(i)

#exa Python For Loop in Python Dictionary
# d=dict()
# d["xyz"]=123
# d["abc"]=456
#
# for i in d:
#     print(i,d[i])


# #exa
# string="python"
# for i in string:
#     print(i)

#exa
#
# for i in range(0,10,2):
#     print(i)

#exa:::Python For Loop inside a For Loop

# for i in range(1,4):
#     for j in range(1,4):
#
#         print(i,j)
#

#######  For Loop with Zip()
# fruits = ["apple", "banana", "cherry"]
# colors = ["red", "yellow", "green"]
#
# for fruit,color in zip(fruits,colors):
#     print(fruit,"is",color)

###### for loop tupple
# tup=((1,2),(3,4),(5,6))

# for a,b in tup:
#     print(a,b)

####### Loop Control Statements
#continue
# for letter in "geeksforseek":
#     if letter=="e" or letter=="s":
#         continue
#     print("letter is :",letter)


#break
# for letter in "geeksforseek":
#     if letter=="e" or letter=="s":
#         break
#     print("letter is :",letter)

#pass
# for i in "geeksfeeks":
#     pass
# print(i)

##########33 forloop with range function

# for i in range(10):
#     print(i,end="")


####sum of 10 number

# sum=0
# for i in range(1,10):
#     sum=sum+i
# print(sum)

# ###exa
# clothes = ["shirt", "sock", "pants", "sock", "towel"]
# paired_socks = []
# 
# for i in clothes:
#     if i=="sock":
#         continue
# paired_socks.append("sock")
# print(f"washing {paired_socks}")










