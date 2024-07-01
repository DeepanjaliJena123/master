######### For loop  ##########
#
# l=["geek","for","python"]
#
# for i in l:
#     print(i)

#exa
# d=dict()
# d['xyz']=123
# d['abc']=343
#
# for i in d:
#     print(i,d[i])

#exa
# s="geeks"
# for i in s:
#     print(i)

#exa
# for i in range(0,10,2):
#     print(i)

#exa loop for inside a for loop
#
# for i in range(1,4):
#     for j in range(1,4):
#         print(i,j)

#exa loop with zip
# fruits = ["apple", "banana", "cherry"]
# colors = ["red", "yellow", "green"]
# for fruit,color in zip(fruits,colors):
#     print(fruit,"is",color)

#exa: loop with tuple
# t = ((1, 2), (3, 4), (5, 6))
# for a,b in t:
#     print(a,b)

#exa control statement : continue

# for letter in "geeksforgeek":
#     if letter=='e' or letter=='s':
#         continue
#     print("current letter is :",letter)


#exa: break

# for letter in "geeksforgeej":
#     if letter=='e' or letter=='s':
#         break
# print("current letter is :",letter)


#########  range
# for i in range(10):
#     print(i)

#exa:sum
# sum=0
# for i in range(1,10):
#     sum=sum+i
# print(sum)

######## while loop #######################################
# count=0
# while count<3:
#     count+=1
#     print("hello geek")
#

#exa
# a = [1, 2, 3, 4]
# while a:
#     print(a.pop())

#exa while block
# count=0
# while (count<5): count+=1; print("hello")
#

#qstn:1 palendrome
string=input(("Enter a string:"))
if(string==string[::-1]):
      print("The string is a palindrome")
else:
      print("Not a palindrome")


#qstn:2
lis=[1,2,2,3,3]
output={element:lis.count(element) for element in set(lis)}
print(output)

qstn:3
lis=[(4,5),(4),(8,6,7),(1),(3,4,6,7)]

lis = [(4, 5), (4), (8, 6, 7), (1), (3, 4, 6, 7)]

# Remove tuples with a count of 2
result = [tup for tup in lis if isinstance(tup, tuple) and len(tup) != 2]

print(result)


# In this code:
#
# The list comprehension iterates through each element (tup) in the original list.
# The condition isinstance(tup, tuple) ensures that only tuples are considered.
# The condition len(tup) != 2 checks if the length of the tuple is not equal to 2.
# Tuples meeting both conditions are included in the result.
# As a result, the tuples with a count of 2 are removed from the list, and result contains the modified list.


# lis=[1,5,3,6,4,2]
# lis.sort()
# print(lis)










