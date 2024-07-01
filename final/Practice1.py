# # swap all upper to lower and lower to upper using loop
# x='Hello Welcome to python'
# result = ''
# # for char in x:
# #     if char.isupper():
# #         result += char.lower()
# #     elif char.islower():
# #         result += char.upper()
# #     else:
# #         result += char
# #
# # print(result)

#2
# #find the vowels count
# z="hello welcome to python"
# vowel="a,e,i,o,u"
# count=0
# for i in z:
#     if i in vowel:
#         count+=1
# print(count)

#3
#remove all speacial characters
# a='hel$lo wel*come to@ pyt#&on'
# new_str=""
# sp=''
# for i in a:
#     if i.isalnum() or i.isspace():
#         new_str+=i
# print(new_str)


#4
# x=[5,9,6,8,3,2,4]
# z=[]
#
# y=1
# for i in range(len(x)):
#     z.append(x[-y])
#     y+=1
# print(z)           #[4, 2, 3, 8, 6, 9, 5]


#OR
# for i in range(len(x) - 1, -1, -1):
#     z.append(i)
# print(z)      #[6, 5, 4, 3, 2, 1, 0]


## # #or
# count=1
# for i in range(-1,len(x)): #7            #0,1,2,3,4,5,6
#     z.append(x[i])
#     count=count+1
# print(z)

#exa: Reverse a list using loop
# s=[10,20,30,40]
# z=[]
# for i in range(len(s)):
#     z.append(s[-i])
#
# print(z)
# #or
# s=[10,20,30,40]
# z=[]
# y=1
# for i in range(len(s)):
#     z.append(s[-y])
#     y+=1
# print(z)
#or
# s = [10, 20, 30, 40]
# z = []
# for i in range(len(s) - 1, -1, -1):
#     z.append(s[i])
# print(z)

