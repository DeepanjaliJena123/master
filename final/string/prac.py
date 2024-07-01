# x='Hello Welcome to python'
# # swap all upper to lower and lower to upper
#
#
# y="hello wel1come t2o pyth4on"
#separate all value and numbers
# new=""
# for i in y:
#     print(i)
#     if i.isalpha()==True:
#         new+=i
# print(new)

#
# z="hello welcome to python"
# #find the vowels count
#
# vowel="a,e,i,o,u"
# count=0
#
# for i in z:
#     if i in vowel:
#         count+=1
# print(count)
#
#
# a='hel$lo wel*come to@ pyt#&on'
# #remove all speacial characters
# new_str=""
# for i in a:
#     if i.isalpha():
#         new_str+=i
# print(new_str)
#


# #or
# s= b.split()
# t=""
# for i in t:
#
#
#
#
#
# c=" hello welcome to python "
# #remove first and last spaces
# c.strip()
# print(c)
#
#
#
#
#
#
# #
# x=[5,9,6,8,3,2,4]
# z=[]
# y=1
# # # for i in range(len(x)):1...7
# # #     z.append(x[-y])
# # #     y+=1
# # # print(z)
# #
# # #or
# count=1
# for i in range(-1,len(x)): #7            #0,1,2,3,4,5,6
#     z.append(x[i])
#     count=count+1
# print(z)


# #exa: Reverse a list using loop
# s=[10,20,30,40]
# z=[]
# y=1
# for i in range(len(s)):
#     z.append(s[-y])
#     y+=1
# print(z)













###################################################################################
# Example 1: Print the first 10 natural numbers using for loop.
# n=11
# for i in range(1,n):
#     print(i)
#
#

# Example 2: Python program to print all the even numbers within the given range.
# given_range=11
# for i in range(given_range):
#     if i%2==0:
#         print(i)

# Example 3: Python program to calculate the sum of all numbers from 1 to a given number.
# n=11
# count=0
# for i in range(1,n):
#     count+=i
# print(count)

# or
# for i in range(1,n+1):
#     count+=i
# print(count)

# Example 4: Python program to calculate the sum of all the odd numbers within the given range.
# num=10
# sum=0
# for i in range(num):
#     if i%2!=0:
#         sum+=i
# print(sum)
#

#Example 5: Python program to print a multiplication table of a given number
# n=5
# for i in range(1,11):
#     print(n,'X',i,'=',n*i)
#


# Example 6: Python program to display numbers from a list using a for loop.
# list = [1,2,4,6,88,125]
# for i in list:
#     print(list)
#

# Example 7: Python program to count the total number of digits in a number.
# given_number = 129475
# total=0
# for i in range(len(str(given_number))):
#     total+=1
# print(total)


# Example 8: Python program to check if the given string is a palindrome.
# given_string="madam"
# reverse_string="m"
# for i in given_string:
#     reverse_string=i+reverse_string
# if given_string==reverse_string:
#     print("it is palindrome")
# else:
#     print("not palindrome")           #doubt

# Example 9: Python program that accepts a word from the user and reverses it.

# given_string=input()       #deepa
# r=""
# for i in given_string:
#     r=i+r
# print(r)

# Example 10: Python program to check if a given number is an Armstrong number
# number that equals the sum of its individual digits, each raised to the power of the number of digits



# Example 11: Python program to count the number of even and odd numbers from a series of numbers.
# num_list = [1, 3, 5, 6, 99, 134, 55]
# for i in num_list:
#     if i % 2 == 0:
#         print(i, "is an even number.")
#     else:
#         print(i, "is an odd number."



#exa:find the 2nd largest number:
# x=[2,4,1,3,6,5]
# x.sort()
# number=25
# second_largest=[]
# for i in x:
#     if number%i==0:
#         number=number+i
# print(second_largest)

#check prime number
# n=10
# for i in range(2,n):
#     if n%i==0:
#         print("not prime number")
#         break
# else:
#         print("prime number")
#

#sort character of string? 1st alphabet,sy,bol followed by digit?
# name="geekforpython"
# print("".join(sorted(name)))
#
# ch=input("enter character :")
# if ch.isdigit():
#     print("is digit")
# else:
#     print("not digit")
#
# print("".join(sorted(ch)))
#

#find number of occurance of each vowel present in the given string?
# s="geekforpython"
# vowel="a,e,i,o,u"
#
# for i in s:
#     if vowel in i:
#         print()



#Count number of vowels in a String in Python
# s="geek for python"
# vowel=['a','e','i','o','u']
# count=0
# for i in range(len(s)):
#     if s[i] in vowel:
#         count+=1
# print(count)
#


#exa::
#ABAABBCA
#ans. 4A3B1C
s="ABAABBCA"
count_chr=""
# for i in range(len(s)):
#     count_chr.count(s[i])
# print(count_chr)

# for i in range(len(s)):
#     for j in range(1,len(s)):
#         count_chr.count()

# X="aaBBccDDeeFgHii"
# ch=""
#
# for i in range(len(X)):     #1,15
#     if X[i]==i:
#         continue
#         ch+=i
#




#exa: Reverse a list using loop
# s=[10,20,30,40]
# z=[]
# y=1
# for i in range(len(s)):
#     z.append(s[-y])
#     y+=1
# print(z)

#exa or
# lst = [10, 11, 12, 13, 14, 15]
#
# l = []
# for i in lst:
#     l.insert(0, i)
# print(l)

#exa or
# original_list = [1, 2, 3, 4, 5]
# reversed_list = []
# for value in original_list:
#   reversed_list = [value] + reversed_list
# print(reversed_list)

#exa or
# s= [1, 2, 3, 4, 5]
# k= []
# for value in range(len(s)):
#   k.append(s.pop())
# print(k)

#Using recursion,without the use of any built-in functions.
# def list_reverse(original_list ):
# if(len(original_list) == 0):
#   return original_list
# else:
#   return list_reverse(original_list [1: ])+original_list[0]
#
# original_list = [1, 2, 3, 4, 5]
# print("List before reverse : ",original_list)
# print("List after reverse : ", list_reverse(original_list))


#get 4 snd 5 uding slicing
# s=[1,2,3,4,5,7,8,9,10]
# sliced_list=s[3:5]
# print(sliced_list)

#################################  Duplicate   ###################
#remove duplicate from list
# s=[2,2,3,4,5,6,5,1]
# chr_uniqe=[]
# for i in s:
#     if i not in chr_uniqe:
#         chr_uniqe.append(i)
# print(chr_uniqe)

#exa
# mylist = ["a", "b", "a", "c", "c"]
# lis1=list(dict.fromkeys(mylist))
# print(lis1)

#exa
# mylist = ["a", "b", "a", "c", "c"]
# s=list(set(mylist))
# print(s)

#



################################
# Make all the first letter as capital.
#xa
# x="my name is deepa"
# k=x.split()
# print(k)

# for i in k:
#     z=i[0].upper()+i[1:]
#     print(z,end=" ")

#Or
# z=''
# for i in k:
#     d=i[0].upper()+i[1:]
#     z=z+d+" "
# print(z)


#exas1 = "abcdefg"
# s1 = "abcdefg"
# s2 = "xyz"
# s3 = '12345'
#
# result = ''
# for i in range(max(len(s1), len(s2), len(s3))):
#     if i < len(s1):
#         result += s1[i]
#     if i < len(s2):
#         result += s2[i]
#     if i < len(s3):
#         result += s3[i]
#
# print(result)

##exa: x=baNaNa
# x='banana'
# y=[]
# for i in x:
#     if i=='n':
#         y.append(i.upper())
#     else:
#         y.append(i)
# print("".join(y))



#exa ['my', 'NAME', 'is', 'NAME', 'deepanjali', 'NAME', 'jena']
# s="m@y name is na@me deepanjali name j@ena"
# k=s.split()
# y=[]
# for i in k:
#     if i=="name":
#         y.append(i.upper())
#     else:
#         y.append(i)
# print(y)


#exa
# s=
# y=[]

# for i in s:
#     if i!="@":
#         y+=i
# print("".join(y))

#or
# for i in "m@y name is na@me deepanjali name j@ena":
#     if i=="@":
#         continue
#     print("".join(i),end="")       #my name is name deepanjali name jena
#
#

#or
# s="m@y name is na@me deepanjali name j@ena"
# y=[]
#
# for i in s:
#     if i=="@":
#         y
#         continue
# print(y)                                  #another way


#exa:
# clothes = ["shirt", "sock", "pants", "sock", "towel"]
# paired_socks = []
#
# for item in clothes:
#     if item == "sock":
#         continue
#     else:
#         print(f"Washing {item}")
# paired_socks.append("sock")
# print(f"washing{paired_socks}")
#

#exa:
# s=['john','jimmy','Aman','jisu','jini']
# empty=[]
# for i in s:
#     if i.islower():
#         empty.append(i[0].upper()+i[1:])
# print(empty)


#exa: odd word middle ltr will be uper
# x='hello welcome to python'
# k=x.split()
# modified=[]
# for i in k:
#     if len(i)%2!=0:
#         ltr=len(i)//2
#         modified.append(i[0:ltr]+i[ltr].upper()+i[ltr+1:])
#     else:
#         modified.append(i)
# print(modified)


#exa: increment 2
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
#
# #comprehension
# new=[x**3 for x in range(11) if x%2==0]
# print(new)


#3xa
d = "35 0.67 12 4"

k=d.ase
for i in d:



