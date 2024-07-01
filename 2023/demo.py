# write 2nd largest number in list
x=[5,6,7,8,1,2]
x.sort()
print(x)
x.pop()
print(x)
print(x[-1])
# #



# #check whether the number is prime or not

num=10

for i in range(2,num):
    if num%i==0:
        print("not prime")
        break
else:
    print("prime")
#
# # write a program to sort charachter to string, first allphabate symbol followed by digit.
# ch=input("Enter a character:")
# if ch.isdigit():
#     print(ch, "is a digit")
# else:
#     print(ch,"is not a digit")


# Write a program to find the number of occurance of each vowel is present in the given string.

vowel=("a","e","i","o","u")

if "a" in vowel:
    print("a is vowel")
else:
    print("a is not vowel")

#check whether the given two strings are anagrams or not(without sorting)

str1=input("string1:")
str2=input("string2:")
sorted_str1=sorted(str1)
sorted_str2=sorted(str2)

if sorted_str1==sorted_str2:
    print("given strings are anagram")
else:
    print("not anagram")
#
# #or
#
# if len(str1)==len(str2):
#    if sorted_str1==sorted_str2:
#      print("given strings are anagram")
#    else:
#      print("not anagram")
# else:
#     print("given strings are not anagram")

#find number of occurance of each character present in the given string without using count method (using dictionary)

# s=[1,2,3,4,5,6,7,8,9,10]
# #get 4 and 5 using slice
# sliced_list=s[3:7]
# print(sliced_list)

#duplication find
# s=[2,2,4,5,6,8,6,7]
# new_list=list(set(s))
# print(new_list)
#
# test_list = [1, 5, 3, 6, 3, 5, 6, 1]
# print("The original list is : " + str(test_list))
#
# res = []
# for i in test_list:
#     if i not in res:
#         res.append(i)
#
# print(res)


#25. convert all to uper
# x="my name is ashok"
# upper_case=x.upper()
# print(upper_case)













































