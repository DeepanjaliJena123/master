# join elements of the sequence separated by a string separator
#This function joins elements of a sequence and makes it a string.

# string='-'.join("hello")
# print(string)
#

#exa2:
# list1=['g','e','e','k','s']
# print("".join(list1))

#exa3:
# list2="geeks"
# print("$".join(list2))

#exa3:
# lis=('1','2','3','4')
# s="-"
# s=s.join(lis)
# print(s)

#exa4:
# list={'1','2','3','4','5'}
# s="-#-"
# print(s.join(list))
#

#exa5:
# dic={'geek':1,'for':2,'geeks':3}
# string='-'.join(dic)
# print(string)

#exa6:
words=["apple","","banana","cherry",""]
separator="@"
# print(separator.join(words))
result=separator.join(word for word in words if word)
print(result)










