# s="geek for python"
# print(s[0])
# print(s[-1])

#slicing
# string="hello to python"
# # print(string[1:3])
# print(string[-1:-6])

# #asci ltr
# print(ord("A"))
# print(chr(65))

#min,max
# print(max("abc"))
# print(min("xyz"))

#in, not in operator
# s="welcome"
# print("come" in s)
# print("lone" in s)
# print("note " not in s)

#lowercase
# import string
#
# result=string.ascii_lowercase
# print(result)

# # exa
#
# import string
#
# def check(value):
#     for letter in value:
#         if letter not in string.ascii_lowercase:
#             return False
#     return True
#
# input1="geeksforgeek"
# input2="PYTHON"
#
# print(check(input1))
# print(check(input2))

#endwith
s="geeks for geek."
# print(s.endswith("geek."))
#
# result=s.endswith("geek.",10)
# print(result)

# result=s.endswith("geek.",10,15)
# print(result)

## check mail id is valid or not
#
# user_email=input("Enter ur GFG email id :").lower()
#
# if user_email.endswith("geek.org"):
#     print("valid id")
# else:
#     print("not valid")


###startwith

# var="geeks for java"
# # print(var.startswith("geeks"))
# # print(var.startswith("java"))
#
# print(var.startswith("for",6,9))
#

#isdigit
# s="1234"
# k="jjahd123"
# print(s.isdigit())
# print(k.isdigit())


newstring = ''

# Initialising the counters to 0
count = 0

# Incrementing the counter if a digit is found
# and adding the digit to a new string
# Finally printing the count and the new string

# for a in range(53):
#     b = chr(a)
#     if b.isdigit() == True:
#         count += 1
#         newstring += b
#
# print("Total digits in range :", count)
# print("Digits :", newstring)                ##doubt

##isalpha

# string="Deepanjali"
# count=0
# new_string=""
#
# for i in string:
#     if i.isalpha()==True:
#         count+=1
#         new_string+=i
# print(count)
# print(new_string)

#exa

# text = "Hello, World! How are you today?"
# alphabetic_text = ""
#
# for char in text:
#     if char.isalpha():
#         alphabetic_text+=char
# print(alphabetic_text)

#isdecimal

# s="100"
# print(s.isdecimal())
#
# k="123456"
# print(k.isdecimal())
#
# ss="afh235"
# print(ss.isdecimal())
#
# kk="10/3"
# print(kk.isdecimal())
#

#exa

# def convert_int(num_str):
#     if num_str.isdecimal():
#         return int(num_str)
#     else:
#         return None
#
# print(convert_int("555"))
# print(convert_int("10.11"))



# ###    format  ###
# Definition and Usage.
# The format() method formats the specified value(s) and insert them inside the string's placeholder.
# The placeholder is defined using curly brackets: {}.

#exa
# name="Deepa"
# age=29
#
# messg="my name is {0},my age is {1}.{1} is my fev number".format(name,age)
# print(messg)


##       string_index   #########
# s="random"
# print(s.index("and"))
#
# string="geeks for geeks"
# sub="geeks"
# pos=string.index(sub,2)
# print(pos)
#
# The index() method is similar to find().
# The only difference is find() returns -1 if the searched string is not found and index() throws an exception in this case.

#
# test_string = "1234gfg4321"
#
# print(test_string.index("gfg",4,8))
# print(test_string.index("32",5,-1))

# ####   isspace ####
#
# s="geeksforgeeks"
# print(s.isspace())
#
# k="hello python"
# print(k.isspace())
#
# string="welcome to geeks for geeks"
# count=0
#
# for i in string:
#     if i.isspace()==True:
#         count+=1
# print(count)

#####  swapcase() Method  #####
# s="geekforgeeks"
# print(s.swapcase())
#
# k="heLLO PYthon"
# print(k.swapcase())
#
# g="HELLO"
# print(g.swapcase())

####  replace()  ####
# The replace() method replaces a specified phrase with another specified phrase.

# s="Good Morning"
# print(s.replace("Good","Great"))
#
# hh="replace"
# print(hh.replace("replace","replaced"))

#exa
# string = "geeks for geeks geeks geeks geeks"
# print(string.replace("e","a"))
# print(string.replace("eks","a",3))

#exa

####  String.partition #####
# splits the string at the first occurrence of the separator and returns a tuple.
# or The partition() method searches for a specified string,
# and splits the string into a tuple containing three elements.

#exa
#
# s="i love geeks for geeks"
# print(s.partition("for"))
#
# k="lights attracts the bugs"
# print(k.partition("attracts"))

#exa
# string = "geeks for geeks"
# print(string.partition('are'))
#
# l="node or snore"
# print(l.partition("is"))


# #exa
# url = "https://www.example.com/index.html"
# result=url.partition("//")
# print(result)     ### ('https:', '//', 'www.example.com/index.html')
#
# result=result[2].partition('/')
# print(result)
# print(result[0])



########   String.Isidentifier  ####
# Check whether a string is a valid identifier or not.
# Note: A string is considered as a valid identifier if:
#
# It only consists of alphanumeric characters and underscore (_)
# Doesn’t start with a space or a number

# string="coding_101"
# print(string.isidentifier())
#
# s="geeks for geek"
# print(s.isidentifier())
#
# k="geeksfirjhcsdjhh"
# print(k.isidentifier())
#
# d="dhj6khfejf0dfjk4"  ##alphanumrical string
# print(d.isidentifier())
#
# hh="56jshdhk0jsj5j8kjk"   #begin with integer, so its is false
# print(hh.isidentifier())

#exa
# string="hello123"
# if string.isidentifier():
#     print("is a identifier")
# else:
#     print("not a identifier")


#string.rindex
# Returns the highest index of the substring inside the string if substring is found.

#exa
# text="geeks for geeks"
# print(text.rindex("geeks"))
#
# d="geeks"
# print(d.rindex("e"))

####  splits

# string="one,two,three"
# word=string.split(",")
# print(word)

# s="geek for geeks"
# # print(s.split())
# k="geek, for, geeks"
#
# print(k.split(','))
#
# j="geek:for:geek"
# print(j.split(":"))

#exa
# str="geeks ,for, python, only"
# print(str.split(',',0))
# print(str.split(',',4))
# print(str.split(',',1))

## rsplit

# split the given string into three parts. rpartition() starts looking for separator from the right side,
# till the separator is found and return a tuple which contains part of the string before separator,
# the separator and the part after the separator.
#
# s="geek@for@seek@not@of@the@set"
# print(s.rpartition("@"))
#
# k="sita is going to school"
# print(k.rpartition('not'))


##### count ###
# Python String count() function returns the number of occurrences of a substring within a String.

# s="apple"
# print(s.count('a'))
#
# k="geeks for geeks"
# print(k.count("geeks"))
#
# h="geeksforseek"
# print(h.count('h'))

#exa
# strings="geeks for neek"
# char_count="e"
# total=sum(string.count(char_count) for string in strings)
# print(total)

#exa
# import re
# my_string = "Good Morning and Morning is Great."
# substring = "Morning"
# total=len(re.findall(substring,my_string))
# print(total)

#exa
# string="geek for geek"
# print(string.count('geek',0,5))
# print(string.count('geek',0,15))


####  join     ########
# Python join() provides the functionality of joining elements from the iterable separated by a string operator

# h="hello"
# print('_'.join(h))

# list=['g','e','e','k']
# print(''.join(list))
#
# lis=" geeks "
# print('$'.join(lis))

# #tuple
# tuple=('1','2','3','4','5')
# s='_'
# print(s.join(tuple))

#dic
# list1 = {'1', '2', '3', '4', '4'}
# s='_#_'
# print(s.join(list1))

#exa
# dic = {'Geek': 1, 'For': 2, 'Geeks': 3}
# s='_'
# print(s.join(dic))
#
#exa
# words = ["apple", "", "banana", "cherry", ""]
# separator = "@ "
# print(separator.join(word for word in words if word))

#####   strip   #####
# It returns a copy of the string with both leading and trailing white spaces removed

# string=" hello world?  "
# print(string.strip())

#exa
# s="geeks for geeks"
# print(s.strip('geeks'))
#
#

####  rstrip   #####
# string="geeks"
# print(string.rstrip('s'))


# s="geek for feek"
# print(s.rstrip('eek'))

#
# j="welcome   "
# print(j.rstrip())



###########################################################################

#1: find vowel of strings?

# s="i am deepanjali jena"
#
# v=['a','e','i','o','u']
#
# for i in v:
#     count=0
#     for j in range(len(s)):
#         if i==s[j]:
#             count+=1
#     print(i,count)




#### reverse
# name="Deepanjali Jena"
# word=name.split()
# reversed_name=" ".join(reversed(word))
# print(reversed_name)


#loop
# newstring=""
# for i in reversed(name):
#     newstring+=i
# print(newstring)       ##aneJ ilajnapeeD


#or/
# name="Deepanjali Jena"
# new_str=""
#
# for i in name:
#     new_str=i+new_str
# print(new_str)           ###aneJ ilajnapeeD


##########   find duplicate in string
# # exa1
# str="geek for geeks"
# emty=""
#
# for i in str:
#     if i not in emty:
#         emty+=i
# print(emty)



###### conditional statemnt  ####

###########  odd n even
# number=8
# if number%2==0:
#     print("its even")
# else:
#     print("its odd")

#### eligible for vote
# age=15
# if age>=18:
#     print("eligible for vote")
# else:
#     print("not eligible")

########### sum of n natural numbers??????
# n=int(input("enter n value :"))
# sum=0
#
# for i in range(1,n+1):
#     sum+=1
# # print(f"sum of first {n} natural numbers is {sum}")
# print("sum natural number",sum)

###### split the string into word and count how many words avaliable?

# s="hello python and this is my fvrt languange"
# count=0
#
# for word in s.split():
#     count+=1
# print(count)

####accessing keys in dic
s={"name":"python","number":2}
# for i in s:
#     print(i)
# output:
# name
# number

#orr

# for i in s.keys():
#     print(i)

##acessing value in dic
# s={"name":"python","number":2}
# for i in s:
#     print(s[i])

# ##orr
# for i in s.values():
#     print(i)


### accessing key n value using item method?
# s={"name":"python","number":2}
#
# for x,y in s.items():
#     print(x,y)



####nested while loop
# list1=[1,2,3]
# list2=[4,5,6]
# i=0
#
# while i<len(list1):
#     j=0
#     while j<len(list2):
#         print(list1[i],list2[j])
#         j+=1
#     print()
#     i+=1

######## separate even and odd number

# li=list(range(1,25))
# even_num=[]
# odd_num=[]
#
# for item in li:
#     if item%2==0:
#         even_num.append(item)
#     else:
#         odd_num.append(item)
# print(odd_num)
# print(even_num)







