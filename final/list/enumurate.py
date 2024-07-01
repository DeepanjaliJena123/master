# The enumerate function is a built-in function that allows you to iterate through a sequence
# and keep track of the index of each element.

#exa
# marks=[50,20,40,80,90,10]
# for index,mark in enumerate(marks):
#     print(mark)
#     if (index==4):
#         print("Conguratulatios, u r qualify")

# s=[50,20,40,80,90,10]
# for index, i in enumerate(s):
#     print(i)
#     if index==2:
#         break
# print("congrat")

#exa:loop over list,print index and value of each element
# fruits=["apple","banana","mango"]
# for index,fruit in enumerate(fruits):
#     print(index,fruit)
#     print(type(fruit))           #return type tuple

#exa:
# fruits=["apple","banana","mango"]
# for index,fruit in enumerate(fruits,start=1):
#     print(index,fruit)
#exa
# fruits=["apple","banana","mango"]
# for index,fruit in enumerate(fruits):
#     print(f'{index+1}:{fruit}')
#

#exa:loop over string,print index and value of each element

# s="Hello"
# for index,i in enumerate(s):
#     print(index,i)

#exa
#
# lis1= ["eat", "sleep", "repeat"]
# lis2= "geek"
# print(list(enumerate(lis1)))
# # print(list(enumerate(lis2)))
# print(list(enumerate(lis2)))































#exa
# l1 = ["eat", "sleep", "repeat"]
#
# # printing the tuples in object directly
# for ele in enumerate(l1):
#     print(ele)
#
# # changing index and printing separately
# for count, ele in enumerate(l1, 100):
#     print(count, ele)
#
# # getting desired output from tuple
# for count, ele in enumerate(l1):
#     print(count)
#     print(ele)


# #exa
# l1 = ["eat", "sleep", "repeat"]
# for i in enumerate(l1):
#     print(i)
#
#
# for count, i in enumerate(l1,100):
#     print(count,i)

# for count,i in enumerate(l1):
#     print(count)
#     print(i)

#exa:
fruits = ['apple', 'banana', 'cherry']
enum_fruits = enumerate(fruits)
print(type(enum_fruits))
#
# next_element = next(enum_fruits)
# print(f"Next Element: {next_element}")
#
#












