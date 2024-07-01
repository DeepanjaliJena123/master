# string="amaama"
# half=int(len(string)/2)
#
# first=string[:half]
# second=string[half:]
#
# #symmetric
# if first==second:
#     print(string,"string is symmetrical")
# else:
#     print(string,"string is not symmetrical")
#
#
# #palindrom
# if first==second[::-1]:
#     print(string,"string is palindrome")
# else:
#     print(string,"string is not palindrome")


######reverse
# string = "geeks quiz practice code"
#1st reverse as it is
# rev=""
# for i in string:
#     rev=i+rev
# print(rev)

#2nd reverse string n store in a new string
# rev=""
# z=string.split()
# for i in z:
#     rev=i+" "+rev
# print(rev)

#3rd 1st reverser n store in a list
# string = "geeks quiz practice code"
# z=string.split()
# rev=[]
# for i in range(1,len(z)+1):
#     rev.append(z[-i])
# print(rev)

#4th reverse string n store in a string using range func
# string = "geeks quiz practice code"
# z=string.split()
# rev=''
# for i in range(1,len(z)+1):
#     rev=rev+' '+z[-i]
# print(rev)

#5 using def func
# def revese(str):
#     rev=""
#     for i in str:
#         rev=i+rev
#     print(rev)
#
# str="geek is python"
#
# revese(str)

#or

# def revese(string):
#     z = string.split()
#     rev = ''
#     for i in range(1, len(z) + 1):
#         rev =rev+' '+z[-i]
#     print(rev)
#
# string="This is java program"
#
# revese(string)
#

############ Remove Letters From a String in Python

# string="geeksforgee"
# Removing char at pos 3
# new_str=string.replace("e","")
# print(new_str)   #gksforg

## Removing 1st occurrence of s, i.e 5th pos.
# new=string.replace('s','',1)
# print(new)     #geekforgee


## using loop n continue
# string="geeksforgee"
# for i in string:
#     if i=='e':
#         continue
#     print(i)

###  or remove 123
# str = 'Geeks123For123Geeks'
# new_str=''
# for i in str:
#     if i.isalpha()==True:
#         new_str+=i
# print(new_str)

## remove pos 3
# str="GowksForGeek"
# new=''
# for i in range(len(str)):
#     if i!=2:
#         new=new+str[i]
# print(new)

#or
# new_str=str[:2]+str[3:]
# print(new_str)
#

# or
## Removing char at pos 3
# using join() + list comprehension
# str="GowksForGeek"
#
# new=''.join([str[i] for i in range(len(str)) if i != 2])
# print(new)


########  Check if String Contains Substring in Python
# MyString1 = "A geek in need is a geek indeed"
# if 'need' in MyString1:
#     print("its present")
# else:
#     print("not present")
#

#or

# string = "geeks for geeks"
# substring = "geeks"
# s=string.split()
# if substring in s:
#     print('yes')
# else:
#     print('no')
#
#

#or using def func n usung find
# def check(string,sub_str):
#     if (string.find(sub_str)==-1):
#         print("yes")
#     else:
#         print("no")
# string = "geeks for geeks"
# sub_str = "geek"
#
# check(string,sub_str)
#

#or using count
# def check(s2,s1):
#     if (s2.count(s1)>0):
#         print("yes")
#     else:
#         print("no")
#
# s2 = "A geek in need is a geek indeed"
# s1 = "geeks"
# check(s2,s1)
#

#or  Check Python Substring in string using Index() method
any_string = "Geeks for Geeks substring "
substring="Geeks"
start=0
end=1000
print(any_string.index('substring',start,end))