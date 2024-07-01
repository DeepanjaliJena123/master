#argument
# def add(num1:int,num2:int):
#     num3=num1+num2
#     return num3
# num1,num2=5,15
# ans=add(num1,num2)
# print(f"the addition of {num1} and {num2} results {ans}.

## prime number
# def is_prime(n):
#     if n in [2,3]:
#         return True
#     if (n==1) or (n%2==0):
#         return False
#     r=3
#     while r*r<=n:
#         if n%r==0:
#             return False
#         r+=2
#     return True
# print(is_prime(78),is_prime(79))       more practice

##### even n odd
# def evenOdd(x):
#     if (x%2==0):
#         print("even")
#     else:
#         print("odd")
# evenOdd(2)
# evenOdd(5)
#
# #default argument
# def myfun(x,y=50):
#     print("x:",x)
#     print("y:",y)
# myfun(10)
# #x: 10
# #y: 50

##keyword argument:
# def student(firstname,lastname):
#     print(firstname,lastname)
#
# student(firstname="geeks",lastname="practice")

# #positional argument:
# def nameAge(name,age):
#     print("Hi, i am ",name)
#     print("My age is",age)
# # nameAge("suraj",27)

#Arbitrary Keyword  Arguments
# def myfun(*argv):
#     for arg in argv:
#         print(arg)
# myfun("hello","welcome")

# def myfun(**kwargs):
#     for key,value in kwargs.items():
#         print("%s==%s" % (key,value))
#
# myfun(first="geeks",mid="for",last="geeks")

#function within function:
# def f1():
#     s='i love geeksforgeeks'
#
#     def f2():
#         print(s)
#     f2()
# f1()

#Anonymous Functions in Python (lamda)

# def cube(x):return x*x*x
#
# cube_v2=lambda x:x*x*x
#
# print(cube(7))
# print(cube_v2(7))

#exa:
# def square_value(num):
#     return num**2
# print(square_value(2))
# print(square_value(-4))

#Pass by Reference and Pass by Value
# def myfun(x):
#     x[0]=20
#
# lisst=[10,11,12,13,14,15]
# myfun(lisst)
# print(lisst)
#

# def myfun(x):
#     x=[20,30,40]
# lists=[10,11,12,13,14,15]
#
# myfun(lists)
# print(lists)

# def myfun(x):
#     x=20
#
# x=20
# myfun(x)
# print(x)



# class car():
#     def __init__(self,*args):
#         self.speed=args[0]
#         self.color=args[1]
#
# audi=car(200,"red")
# bmw=car(250,"black")
# mb=car(190,"white")
#
# print(audi.color)
# print(bmw.speed)
#
###lambda

# calc=lambda num:"even number" if num%2==0 else "odd number"
# print(calc(20))

# string='geeks'
# print(lambda string:string)


# filter_nums=lambda s:''.join([ch for ch in s if not ch.isdigit()])
# print("filter_nums():",filter_nums("geeks101"))
#
# do_exclaim=lambda s:s+"!"
# print("do_exclaim():",do_exclaim("i am tired"))
#
# find_sum=lambda n:sum([int(x) for x in str(n)])
# print("find_sum():",find_sum(101))

#if
# i=10
# if (i>15):
#     print("10 is less than 15")
# print("i am not in if")
#
#if else statement:
# i=20
# if i<15:
#     print("i is smaller than 15")
#     print("im in if block")
# else:
#     print("i is greater than 15")
#     print("im not in if block")
# print("im not in if and not in else block")

# def digitsum(n):
#     dsum=0
#     for ele in str(n):
#         dsum+=int(ele)
#         return dsum
# list=[367,111,562,945,6726,873]
#
# newlist=[digitsum(i) for i in list if i & 1]
# print(newlist)  doubt

#nested
# i=10
# if i==10:
#     if i<15:
#         print("i is smaller than 15")
#     if i<12:
#         print("i smaller than 12 too")
#     else:
#         print("i is greater than 15")
#if elif else
# i=20
# if i==10:
#     print("i is 10")
# elif i==15:
#     print("i is 15")
# elif i==20:
#     print("i is 20")
# else:
#     print("i is not present")

# i=10
# if i<15:print("i is less than 15")
#
# i=10
# print(True) if i<15 else print(False)

# x=5
# print(1<x<10)
# print(10<x<20)
# print(x<10<x*10<100)
# print(10>x<=9)
# print(5==x>4)

#loop

# L=["geeks","for","geeks"]
# for i in L:
#     print(i)
#
# d=dict()
# d["xyz"]=123
# d["abc"]=345
# for i in d:
#     print("%s %d" % (i, d[i]))

# s="geeks"
# for i in s:
#     print(s)

# for i in range(0,10,2):
#     print(i)

# for i in range(1,4):
#     for j in range(1,4):
#         print(i,j)
#         print(i)    doubt i value

#zip loop
# fruits=["apple","bannan","cherry"]
# colors=["red","yellow","green"]
# for fruit,color in zip(fruits,colors):
#     print(fruit,"is",color)

# t=((1,2),(3,4),(5,6))
# for a,b in t:
#     print(a,b)

# for letter in "geeksforgeeks":
#     if letter=="e" or letter=="s":
#         continue
#     print("current letter:", letter)

# for letter in "geeksforgeeks":
#     if letter=="e" or letter=="s":
#         break
#     print("current letter:", letter)

# for letter in "geeksforgeeks":
#     pass
# print("last letter:", letter)

# for i in range(10):
#     print(i,end=" ")

# sum=0
# for i in range(1,10):
#     sum=sum+i
# print(sum)        imp

# for i in range(1,4):
#     print(i)
# else:
#     print("no break")
#

##while loop:
# count=0
# while count<3:
#     count=count+1
#     print("hello geek")


## checks if list still
# contains any element
# a=[1,2,3,4]
#
# while a:
#     print(a.pop())    imp

# count=0
# while count<5: count+=1; print("Hello Geek")
#
# i=0
# a="geeksforgeeks"
#
# while i<len(a):
#     if a[i]=="e" or a[i]=="s":
#         i+=1
#         continue
#     print("current letter:",a[i])
#     i+=1


# i=0
# a="geeksforgeeks"
# while i<len(a):
#     if a[i]=="e" or a[i]=="s":
#         i+=1
#         break
#     print("current letter:",a[i])
#     i+=1

# i=0
# a="geeksforgeeks"
# while i<len(a):
#     i+=1
#     pass
# print("value of i :",i)

# i=0
# while i<4:
#     i+=1
#     print(i)
# else:
#     print("no break")

# i=0
# while i<4:
#     i+=1
#     print(i)
#     break
# else:
#     print("no break")
#

#Sentinel Controlled Statement
# a=int(input('enter a number (-1 to quit):'))
# while a!=-1:
#     a=int(input('enter a number (-1 to quit):'))
#

# count=0
# while True:
#     count+=1
#     print(f"count is {count}")
#
#     if count==10:
#         break
# print("the loop has ended")

#break
# for i in range(10):
#     print(i)
#     if i==2:
#         break

# s="geeksforgeeks"
# for letter in s:
#     print(letter)
#     if letter=="e" or letter=="s":
#         break
# print("out of loop")
# num=0
# for i in range(10):
#     num+=1
#     if num==8:
#         break
#     print("the num has value",num)

#list:
# list=["geeks","for","geeks"]
# print(list[0])
# print(list[2])
# Creating a list with multiple distinct or duplicate elements
# list=[1,2,4,4,3,3,3,6,6]
# print("list with the use of numbers:")
# print(list)

# list=[1,2,"geeks",3,"for"]
# print(list)

#Accessing elements from list
# list=["geeks","for","geeks"]
# print(list[0])
# print(list[2])

#Accessing elements from a multi-dimensional list
# list=[["geeks","for"],["geeks"]]
# print("accessing a element from a multi-dimensional list")
# print(list[0][1])
# print(list[1][0])          doubt idex

##### Taking Input of a Python List:
# string=input("enter elements(space-separated):")
# ls=string.split()
# print("the list is:",ls)      #split imp

# n=int(input("enter the size of list:"))
# lists=list(map(int,input("enter the integer\elements:").strip().split()))
# print("the list is ",lists)       imp

#adding element:
# list=[]
# print("initial blank list: ")
# print(list)
# list.append(1)
# list.append(2)
# list.append(4)
# print("new list after addition of three elements: ")
# print(list)
# list=[]
# for i in range(1,4):
#     list.append(i)
# print("new list print:")
# print(list)
#
# list.append((5,6))
# print(list)

#insert
# list=[1,2,3,4]
# print("initial list: ")
# print(list)
#
# list.insert(3,12)
# list.insert(0,"geeks")
# print(list)

#Using extend() method
#append() and extend() methods can only add elements at the end.
# list=[1,2,3,4]
# print("initial list: ")
# print(list)
# list.extend([8,"geeks","always"])
# print(list)


#reversed list
# list1=[1,2,3,4,5]
# list2=list(reversed(list1))
# print(list2)

#Removing Elements from the List
# list=[1,2,3,4,5,6,7,8,9]
# print(list)
# list.remove(5)
# list.remove(9)
# print(list)
#

# list=[1,2,3,4,5,6,7,8,9]
#
# for i in range(1,5):
#     list.remove(i)
# print(list)

#Using pop() method
# list=[1,2,3,4,5]
# list.pop()
# print(list)
# list.pop(2)
# print(list)

#slicing of a list
# list=["g","k","l","e","d","a","q"]
# print(list)
# sliced_list=list[1:5]
# print(sliced_list)


# odd_square=[x**2 for x in range(1,11) if x%2==1]
# print(odd_square)

# odd_sqaure=[]
# for x in range(1,11):
#     if x%2==1:
#         odd_sqaure.append(x**2)
# print(odd_sqaure)

#
# test_list=[1,4,5,6,7]
# print("original list : " + str(test_list))

# for i in range(len(test_list)):
#     print(i,end=" ")
#     print(test_list[i])      doubt



#isalpha
# string="Ayush Saxena"
# count=0
#
# new_string1=""
#
# for a in string:
#     if (a.isalpha())==True:
#         count+=1
#         new_string1+=a
# print(count)
# print(new_string1)

# new_string2=""
# string="Ayush2012"
# count=0
# for a in string:
#     if (a.isalpha())==True:
#         count+=1
#         new_string2+=a
# print(count)
# print(new_string2)


# text="Hello world"
# new_text=""
# for char in text:
#     if char.isalpha():
#         new_text+=char
# print(new_text)


######  expandtab   ######
# string="\t\tCenter\t\t"
# print(string.expandtabs())

# s="i\tlove\tgfg"
# print("modified string: ", end="")
# print(s.expandtabs(2))

#find
#it will find index no of string
#if u not specify start and end index it will bydefault give 0 and lenth -1

# word="geeks for geeks"
# print(word.find("geeks"))
# print(word.find("for"))
#
# if word.find("pawan")!=1:
#     print("substring")
# else:
#     print("not substring")

#######  rfind#######
#Python String rfind() method returns the rightmost index of the substring if found in the given string. If not found then it returns -1
#Returns the highest index of the substring inside the string if substring is found.

# s="geeksforgeeks"
# print(s.rfind("geeks"))
#
# x="geeks for geeks"
# print(x.rfind("for"))

#if we pass start and end paramenter,then it will search for the
#substring in the portion from its right side

# s="geeks for geeks"
# print(s.rfind("ge",2))
# print(s.rfind("geeks",2))
# print(s.rfind("for",4,11))
# print(s.rfind("geeks",-5))

# email="userxyz.com@domain.xyz"
# last=email.rfind(".",1)
# print(last)
# l_sting=email[last:]
# print(l_sting)
#
# if l_sting==".com":
#     print("matched")
# else:
#     print("not matched",l_sting)


###### string.count ######
#Return the number of (non-overlapping) occurrences of substring sub in string
# s="geeksforgeeks"
# char_count=s.count("e")
# print(char_count)
# ## counts the number of times substring occurs in
# print(s.count("geeks"))

# x=["red","green","orange"]
# ch="e"
# total_conut=sum(i.count(ch) for i in x)
# print(total_conut)        doubt


# import re
#
# my_string="good morning and morning is great"
# # sub_string="morning"
# # sub_count=len(re.findall(sub_string,my_string))
# # print(sub_count)

# string="geeks for geeks"
# print(string.count("geeks",0,5))
# print(string.count("geeks",0,15))

# s="welcome"
# print(s.swapcase())

##### join ####
# str="_".join("hello")
# print(str)

# list1=["g","e","e","k","s"]
# print("".join(list1))
# print("$".join(list1))

# list2=("1","2","3","4")
# s="_"
# s=s.join(list2)
# print(s)

# dic={"geek":1,"for":2,"geeks":3}
# string="_".join(dic)
# print(string)

# words=["apple","","banana","cherry",""]
# separator="@"
# result=separator.join(word for word in words if word)
# print(result)

### strip() ####
#In Python, the strip() method is used to remove leading and trailing whitespace characters (spaces, tabs, and newlines) from a string
##It returns a new string with the whitespace characters removed.

# string="  Hello, world!  "
# s_string=string.strip()
# print(s_string)
#
# s="  geeks for geeks  "
# # print(s.strip())
# print(s.strip("geeks"))
#
# s="geeks for geeks"
# s2="ekgs"
# print(s.strip(s2))


###### rstip  ######
# string="geeks for geeks"
# print(string.rstrip("ske"))

# s="geeks  "
# print(s.rstrip())  #it removes the spaces from ryt side
#
#

#### upper()##
# user_input=input("enter choice: ")
# up_input=user_input.upper()
#
# if up_input=="OK":
#     print("correct")
# else:
#     print("incorrect")

##  rjust()   ####
# it wil remove from the left side of string
#The string rjust() method returns a new string of given length after substituting a given character in left side of original string.

# s="geeks"
# len=8
# print(s.rjust(len))

# x="geeks"
# len=8
# fillchar="*"
# print(x.rjust(len,fillchar))

##  ljust  ####
##The string ljust() method returns a new string of given length after substituting a given character in right side of original string.
# s="geeks"
# len=8
# print(s.ljust(len))

# x="geeks"
# len=8
# fillchar="*"
# print(x.ljust(len,fillchar))

#### string Program  #######
# string = "geeks quiz practice code"
# print(string.split()[::-1])

#or
# string = "geeks quiz practice code"
# # reversing words in a given string
# s = string.split()[::-1]
# l = []
# for i in s:
#     # appending reversed words to l
#     l.append(i)
# # printing reverse words
# print(" ".join(l))

     
######### string practice ####
# def string_length(str1):
#     count=0
#     for char in str1:
#         count+=1
#     return count
# print(string_length("w3resource.com"))
#



#####  string reversed  #####
# s="geeksforgeeks"
# # s="".join(reversed(s))
# # print(s)
# # output=skeegrofskeeg
# #
#
# rev_str=""
# for i in s:
#     rev_str=i+rev_str
# print(rev_str)

# def reverse(s):
#     str=""
#     for i in s:
#         str=i+str
#     return str
# s="geeks"
# print("The original string is :", end="")
# print(s)
#
# # print("The reversed string is :", end="")
# # print(reverse(s))
#
# class Public:
#     def __init__(self,number):
#         self.number=number
#     def __len__(self):
#         return self.number
# obj=Public(15)
# print(len(obj))
# string="ASTRING"
# s1=slice(3)
# s2=slice(1,5,2)
# s3=slice(-1,-12,2)
# print(string[s1])
# print(string[3])
# print(string[s2])
# print(string[s3])


# ch=R"i\nlove\tIndia"
# print(ch)
# # print(repr(ch))
# print(ch)
#
# import string
# result=string.ascii_letters
# print(result)
#
# result=string.digits
# print(result)

# import string
# def check(value):
#     for letter in value:
#         if letter not in string.digits:
#             return False
#         return True
#
# input1="0123 456 789"
# print(input1,check(input1))
#
# input2="12.01234"
# print(input2,check(input2))
#
# email=input("enter your mail id :").lower()
# if email.endswith("@geeks.org"):
#     print("hello geek")
# else:
#     print("invalid")
#
#
# output:
# enter your mail id :@geeks.org
# hello geek

# name="Ram"
# age=22
# message="my name is {0} and i am {1} years old.{1} is my favorite number.".format(name,age)
#
# print(message)

# text="I have {an:2f} Rupees!"
# print(text.format(an=4))

# name="name"
# age=22
# message="my name is {0} and i am {1} years old".format(name,age)
# print(message)
#

# text="i have {an:2f} Rupees!"
# print(text.format(an=10))

# print("{}, A computer science portal for geeks.".format("Geeksforgeeks"))

# type="bug"
# result="troubling"
#
# print("why the program was %s me.Then it was me a %s."%(result,type))
#

# string="geeksforgeeks"
# res=string.startswith(("geek","geeks","geeks","geeks"))
# print(res)

# string="apple"
# res=string.startswith(('a','e','i','o','u'))
# print(res)
#
#
# string = "mango"
# res = string.startswith(('m','e', 'i', 'o', 'u'))
# print(res)


# newstring=''
# count=0
#
# for a in range(53):
#     b=chr(a)
#     if b.isdigit()==True:
#         count+=1
#         newstring+=b
# print("Total digits in range :",count)
# print("Digits :",newstring)
#
#
# Total digits in range : 5
# Digits : 01234

# str="ayush Sexena"
# count=0
# new_str=""
# for a in str:
#     if (a.isalpha())==True:
#         count+=1
#         new_str+=a
# print(count)
# print(new_str)

# text="hello, world! how are you today?"
# new_text=""
# for chr in text:
#     if chr.isalpha():
#         new_text+=chr
# print(new_text)
#
#
#
# print("100".isdecimal())
#
# s="12/35"
# print(s.isdecimal())

# def convert_int(num_str):
#     if num_str.isdecimal():
#         return int(num_str)
#     else:
#         return None
# print(convert_int("555"))
# print(convert_int("11.11"))

# print("The temperature today is {0:2f} degrees outside !"
#       .format(35.567))

# string="random"
# print(string.index("and"))

# ch="geeksforgeeks"
# ch1="geeks"
# pos=ch.index(ch1,2)
# print(pos)
#
# string="\n\t\n"
# print(string.isspace())

# str="geeksforgeeks"
# print(str.isspace())
#
# s="\n \n \n"
# print(s.isspace())
#
# k="geeks\nfor\ngeeks"
# print(k.isspace())
#
# str='my name is ayush'
# count=0
#
# for i in str:
#       if i.isspace()==True:
#             count+=1
# print(count)

#
# string="geeksForGEEKS"
# print(string.swapcase())

# str="good morning"
# new_str=str.replace("good","great")
# print(new_str)


# my_string = "geeks for geeks "
# old_substring = "k"
# new_substring = "x"
#
# split_list = my_string.split(old_substring)
# print(split_list)
# new_list = [new_substring if i < len(split_list) - 1 else '' for i in range(len(split_list) - 1)]
# new_string = ''.join([split_list[i] + new_list[i] for i in range(len(split_list) - 1)] + [split_list[-1]])
#
# print(new_string)


# str="I love Geeks for geeks"
# print(str.partition("for"))
#

# url = "https://www.example.com/index.html"
# result = url.partition("//")
# print(result)
# result=result[2].partition("/")
# print(result)
# print(result[0])
# tuple=(1,2,3)
# print(len(tuple))

# text='geeks for geeks'
# result=text.rindex("geeks")
# print(result)
#
# str="ring ring"
# print(str.rindex("ring",0,4))
# print(str.rindex("ring",0,-5))
#
# s="1010000101"
# print(s.rindex("101",2))

# str="geeks"
# print(max(str))
#
# k="raj"
# print(max(k))

# str="welcome everyone to\r the world\ngeeks"
# print(str.splitlines())
# string="geeks for geeks"
# print(string.capitalize())

# word="geeks for geeks"
# print(word.find("for"))
# print(word.find("geeks"))

# w="geeks for geeks"
# print(w.find("ge",2))
# print(w.find('geeks',2))
# print(w.find('g',4,10))
# print(w.find('for',4,11))
#
# main_strin="Hello,Hello,hello,HELLO,hello"
# sub_string="hello"
# count=0
# start_index=0
# for i in range(len(main_strin)):
#     j=main_strin.find(sub_string,start_index)
#     if (j!=-1):
#         start_index=j+1
#         count+=1
# print("Total occurances are: ",count)
#
# str="geeksforgeeks"
# print(str.rfind("geeks"))
#
# word="geeks for geeks"
# result=word.rfind('geeks')
# print("subsiting 'geeks' found at index: ",result)
#
# result=word.rfind('for')
# print(result)
# word = 'CatBatSatMatGate'
#
# # Returns highest index of the substring
# result = word.rfind('ate')
# print("Substring 'ate' found at index :", result)
#

# email = 'userxyz.com@domain.xyz'
# last_dot=email.rfind(".",1)
# print(last_dot)
# tld_string=email[last_dot:]
#
# if tld_string==".com":
#     print("email matched")
# else:
#     print("email not matched",tld_string)
#
#
# str="geeksforgeeks"
# char_count=str.count('e')
# print(char_count)
#
# k="geeks for geeks"
# print(k.count('geeks'))
# strings = ["Red", "Green", "orange"]
# char_to_count = 'e'
# total_count = sum(string.count(char_to_count) for string in strings)
# print(total_count)

# import re
# str="good morning and morning is great"
# sub_str="morning"
# # print(str.count(sub_str))
# sub_count=len(re.findall(sub_str,str))
# print(sub_count)

# string="one,two,three"
# words=string.split(",")
# print(words)
#
# word="geek,for,geeks,pawan"
# print(word.split(',',0))
# print(word.split(',',3))

# s="geek@for@geeks"
# print(s.rpartition('@'))
#
# k="india is the best country and this is my fav"
# print(k.rpartition('is'))
#
# y='sita is going to school'
# print(y.rpartition('not'))

# s="Hello"
# print('_'.join(s))
#
# j=["k","o","n","p"]
# print("".join(j))
# print("$".join(j))
# o="*"
# print(o.join(j))

# dic={"k":1,"p":3,"n":5}
# s="_"
# print(s.join(dic)) #it will join only keys


# s=["apple","","mango","","grapes"]
# separator="@"
# # print(separator.join(s))
# result=separator.join(word for word in s if word)
# print(result)


# s="  hello,world!  "
# print(s.strip())
#
# k="geeks for geeks"
# print(k.strip("geeks")) #only remove beggining and ending for the sting

# s="geeks for geeks"
# s2="ekgs"
# print(s.strip(s2))
#
# k="geeks for geeks"
# print(k.rstrip("eks"))

# translation = {103: None,101: None}
#
# string = "geeks"
# print(string.translate(translation))
#
#
# table = {119: 103, 121: 102, 117: None}
# # target string
# trg = "weeksyourweeks"
# print(trg.translate(table))


# table=str.maketrans("aeiou","12345")
# text="This is a test"
# tranlated_test=text.translate(table)
# print(tranlated_test)
#

# # First String
# firstString = "gef"
#
# # Second String
# secondString = "eks"
#
# # Third String
# thirdString = "ge"
#
# # Original String
# string = "geeks"
# print("Original string:", string)
#
# translation = string.maketrans(firstString,
#                                secondString,
#                                thirdString)
# print(translation)
#
# # Translated String
# print("Translated string:",
#       string.translate(translation))


# string = "12345"
# s="."
# print(s.join(string))
#
# ls=["geeks","for","geeks"]
# print(ls)
# print(ls[0])
# print(ls[2])
#
# lss=[1,2,3,4,5,6]
# print(lss)
#
# k=[["geeks","for"],["python"]]
# print(k)
# print(k[1])
# print(k[0][1])

# string=input("Enter the elements: ")
# lst=string.split()
# print("The list is: ",lst)

# # input size of the list
# n = int(input("Enter the size of list : "))
# # store integers in a list using map,
# # split and strip functions
# lst = list(map(int, input("Enter the integer\
# elements:").strip().split()))[:n]
# print('The list is:', lst)                             #do it agaian after map

# ls=[]

# ls.append(1)
# ls.append(2)
# ls.append(3)
# ls.append(4)
# print(ls)
#extract numbers from string and add all numbers
#add 100 200 300

# import re
#
# def extract_and_sum_numeric(input_string):
#     numeric_values = re.findall(r'\d+', input_string)
#     total_sum = sum(map(int, numeric_values))
#     return total_sum
#
# input_string = "I am deep100anjali je200na i know py300thon"
# result = extract_and_sum_numeric(input_string)
# print("Sum of numeric values:", result)


# import re
#
# def findsum(str):
#     return sum(map(int,re.findall('\d+', str)))
#
# str="I am deep100anjali je200na i know py300thon"
# print(findsum(str))
#

# prints the start and end indices of the matched word within the string.
# import re
#
# s="Its primary function is to offer a search"
# match=re.search(r'offer',s)
# print("start index: ",match.start())
# print("end index: ",match.end())

#######################################  string    #################
# string="Computer is my favorite subject"
#
# print("The first character of string is: ",end="")
# print(string[0])
#
#
# s="geeks for geeks"
# print("slicing character from 3-12")
# print(s[3:12])

# s="geeks for geeks"
# s="".join(reversed(s))
# print(s)

# str="Hello, i am Geek"
#
#updating character
# lis=list(str)
# lis[2]="p"
# str1="".join(lis)
# print(str1)
#
# str3=str1[0:2]+"p"+str[3:]
# print(str3)

#deleting

# s="hello python"
# s2=s[0:2]+s[3:]
# print(s2)
#

# escaping
# s='''I' am "geek"'''
# print(s)
#
# k='I\'am "geek"'
# print(k)
# h="I' am \"geek\""
# print(h)
#
# o="c:\\python\\Geek\\"
# print(o)
#
# tab="python\tjava"
# print(tab)
#
# newline="python\nRobot"
# print(newline)


#r,R
#
# String1 = "\110\145\154\154\157"
# print("\nPrinting in Octal with the use of Escape Sequences: ")
# print(String1)
#
# String2 = R"\110\145\154\154\157"
# print(String2)

#formatting

# s="{} {} {}".format("Geek", "For", "Life")
# print(s)
# k="{1} {0} {2}".format("geeks","for","neeks")
# print(k)
#
# d="{a} {b} {l}".format(a="geeks",b="kars",l="123")
# print(d)

# k="|{:<10}|{:^10}|{:>10}|".format("geeks","for","seek")
# print(k)

# print(ord("A"))
# print(chr(65))
#
# print(max("abc"))
# # print(min("xyz"))
# s="welcome"
# print("come" in s)
# print("wel" not in s)
#
# print(s.capitalize())
# print(s.title())
# print(s.lower())
# print(s.upper())
# print(s.swapcase())
# print(s.casefold())
# print(s.replace("c","d"))

# s="welcome python"
# k=s.replace("e","o")
# print(k)

#reversed
# s="geeksforgeeks"
# rev_str=""
# for i in s:
#     rev_str=i+rev_str
# print(rev_str)

#### check prime
# number=10
#
# for i in range(2,10):
#     if number%i==0:
#         print("not prime")
#         break
#     else:
#         print("prime")

### remove duplicate of string

# string="satish"
# new=""
# for i in string:
#     if i not in new:
#         new=new+i
# print(new)

# write 2nd largest number in list
# x=[5,6,7,8,1,2]
# x.sort()
# print(x)
#
# print(x[-1])


# ch=input("enter character: ")
# if ch.isdigit():
#     print("is a digit")
# else:
#     print("not digit")

# str1=input("string1:")
# str2=input("string2:")
# sorted_str1=sorted(str1)
# sorted_str2=sorted(str2)
#
# if sorted_str1==sorted_str2:
#     print("given strings are anagram")
# else:
#     print("not anagram")


# s=[2,2,4,5,6,8,6,7]
# new_list=list(set(s))
# print(new_list)

# s='ashok kumar panda is in interview'
# print(s[::-1])
# rev=""
# for i in s:
#     rev=i+rev
# print(rev)

#find count of vowels:
# string = "GeekforGeeks!"
# vowels = set("aeiouAEIOU")
# count=0
# count=sum(string.count(vowel) for vowel in vowels)
# print(count)

# for i in string:
#     if i in vowels:
#         count=count+1
# print("The vowel count is :",count)

#check substring in string

# s="geeks for freeks"
#
# if "geek" in s:
#     print("yes")
# else:
#     print("no")

#or
# s="geeks for freeks"
# sub_str="freeks"
# d=s.split()
#
# if sub_str in d:
#     print("yes")
# else:
#     print("no")

#or

# def check(string,sub_str):
#     if string.find(sub_str)==-1:
#         print("no")
#     else:
#         print("yes")
#
# string="geeks for seek"
# sub_str="seek"
# check(string,sub_str)

#or

# def check(s2,s1):
#     if (s2.count(s1)>0):
#         print("yes")
#     else:
#         print("no")
#
# s2="geeks for python"
# s1="python"
# check(s2,s1)

#find index
# s="geeks for python"
# start=0
# end=1000
# print(s.index("python",start,end))
#

# import re
#
# MyString1 = "A geek in need is a geek indeed"
#
# if re.search("need",MyString1):
#     print("yes")
# else:
#     print("no")


# Remove all duplicates
# s = "Python is great and Java is also great"
# l=s.split()
# k=[]
# for i in l:
#     if (s.count(i)>=1) and i not in k:
#         k.append((i))
# print(" ".join(k))

#or
# g= "Python is great and Java is also great"
# print(" ".join(set(g.split())))

#count
#
# my_string = "GeeksForGeeks"
# char_count = my_string.count('e')
# print(char_count)














