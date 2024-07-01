# str='welcome to the world'
# str1="welcome to the world"
# str2='''i' am deepanjali "python"'''
# str3='''i
#         am
#         jena
#       '''
#slicing
#String can be accessed charachter by using the method of Indexing.
# string="geeiks for feek"
# print(string[0])
# print(string[0:3])
# print(string[3:-2])

#reverse string
#exa1
# s="welcome python"
# print(s[::-1])
# #exa2
# s="".join(reversed(s))
# print(s)

#3  Loop through the letters in the word "banana":

# for i in "banana":
#     print(i)

#exa4: len()
# s="hello world"
# print(len(s))

#exa5:Check if "free" is present in the following text:

# txt = "The best things in life are free!"
#
# print("free" in txt)

#exa6:if
# txt = "The best things in life are free!"
# if "free" in txt:
#     print("yes present")

#exa7:Check if "expensive" is NOT present in the following text:

# txt = "The best things in life are free!"
# print("free" not in txt)

#exa8:
# a="welcome to java"

# print(a)
# lis=list(a)
# lis[11]="T"
# aa="".join(lis)
# print(aa)

#or
# a2=a[0:10]+ "T" +a[12:]
# print(a2)

#format
# s="{} {} {}".format("geek","for","life")
# print(s)
#
# a="{1} {0} {2}".format("python","for","testing")
# print(a)

# d="{g} {l} {f}".format(l="geeks",g="for",f="java")
# print(d)

#find duplicate in string
# exa1
# str="geek for geeks"
# emty=""
#
# for i in str:
#     if i not in emty:
#         emty+=i
# print(emty)


#or using def

def find_duplicate_chars(string):
    # Create empty sets to store unique and duplicate characters
    unique_chars = set()
    duplicate_chars = set()

    # Iterate through each character in the string
    for char in string:
        # If the character is already in unique_chars, it is a duplicate
        if char in unique_chars:
            duplicate_chars.add(char)
        # Otherwise, add it to unique_chars
        else:
            unique_chars.add(char)
    return duplicate_chars


# Example usage:
print(find_duplicate_chars("geeksforgeeks"))





