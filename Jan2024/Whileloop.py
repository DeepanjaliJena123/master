####  While loop

# A while loop is a control flow statement which repeatedly executes a block of code until the condition is satisfied.
# It stops executing the block only if the condition fails.
# One should use a 'while' loop when one needs to perform a repeated operation,
# but doesn't know in advance how many iterations would be needed.

#orrm   repeat the peace of code until the condition false

### print geek 3times using whileloop
# count=0
#
# while count<3:
#     count=count+1
#     print("geek")

# #exa ::Python while loop with continue statement
#
# i = 0
# a = 'geeksforgeeks'
#
# while i<len(a):
#     if a[i]=="e" or a[i]=="s":
#         i+=1
#         continue
#     print("current letter :",a[i])
#     i+=1
#

#break

# i=0
# a="geeksforgeeks"
#
# while i<len(a):
#     if a[i]=="e" or a[i]=="s":
#         i+=1
#         break
#     print("current letter :",a[i])
#     i+=1

#pass

# i=0
# a="geeksforgeek"
#
# while i<len(a):
#     i+=1
#     pass
# print("value of i :",i)
#
#

##while loop with else:
#exa
# i=0
# while i<4:
#     i+=1
#     print(i)
# else:
#     print("no break")

#exa

# i=0
# while i<4:
#     i+=1
#     print(i)
#     break                            #doubt in break
# else:
#     print("no break")

#Sentinel Controlled Statement
# a = int(input("enter the number(-1 to quite):"))
#
# while a!=-1:
#     a=int(input("enter the number(-1 to quite)::"))
#

##
# a=[1,2,3,5]
# while a:
#     print(a.pop())

#
# count=0
# while count<5:
#     count+=1
#     print("geekforgeek")


#
#

# countdown=10
# while countdown>0:
#     countdown-=1
#     print(countdown)
# print("done")



#######  break
# for i in range(10):
#      print(i)
#      if i==2:
#          break


#exa
# s="geeksforpython"
#
# for j in s:
#     print(j)
#     if j=="k" or j=="s":
#         break
# print("out of the loop")
# print()

# i=0
#
# while True:
#     print(s[i])
#     if s[i]=="k" or s[i]=="s":
#         break
#     i+=1
# print("out loop")
#

#exa
num=0
# for i in range(10):
#     num+=1
#     if num==8:
#         break
#     print("The num value is :",num)
# print("Out of loop")
#or
while True:
    num+=1
    if num==8:
        break
    print("value is :",num)
print("out of loop")




