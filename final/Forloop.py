#exa
# for i in range(1,4):
#     for j in range(1,4):
#         print(i,j)

#exa
# fruits = ["apple", "banana", "cherry"]
# colors = ["red", "yellow", "green"]
#
# for fruit,color in zip(fruits,colors):
#     print(fruit,"is",color)

#exa
# t = ((1, 2), (3, 4), (5, 6))
# for a,b in t:
#     print(a,b)

#Loop Control Statements
# for letter in "geeksforgeeks":
#     if letter=="e" or letter=="s":
#         continue
#     print("letter",letter)
#
#
#
# #exa
# for letter in "geeksforgeek":
#     if letter=="e" or letter=="s":
#         break
# print("letter :",letter)


#Python for loop with range function

#exa:performing sum of first 10 numbers
# sum=0
# for i in range(10):
#     sum=sum+i
# print(sum)

#exa
# clothes = ["shirt", "sock", "pants", "sock", "towel"]
# paired_socks = []
# for item in clothes:
#     if item=="sock":
#         continue
#     else:
#         print(f"washing {item}")
#
# paired_socks.append("sock")
# print(f"washing {paired_socks}")

#or only print 'sock'
# clothes = ["shirt", "sock", "pants", "sock", "towel"]
# new=[]
# for i in clothes:
#     if i=='sock':
#         continue
#     else:
#         new.append(i)
# print(new)


# s="deepanjali"
# reverse=""
# for i in s:
#     reverse=i+reverse
# print(reverse)

# or

# for i in range(1,len(s)+1):
#     reverse+=s[-i]
# print(reverse)












