#Isidentifier
#Check whether a string is a valid identifier or not.
# @Note: A string is considered as a valid identifier if:
#
# It only consists of alphanumeric characters and underscore (_)
# Doesn’t start with a space or a number

#exa
# str="geek for noop"
# print(str.isidentifier())
#
# s1="geeforjdskjksd"
# print(s1)
#
# s2=""
# print(s2.isidentifier())

#exa

string = "geeks101"
if string.isidentifier():
    print(string, "is an identifier.")
else:
    print(string, "is not an identifier.")

string = "GeeksForGeeks"
if string.isidentifier():
    print(string, "is an identifier.")
else:
    print(string, "is not an identifier.")

string = "admin#1234"
if string.isidentifier():
    print(string, "is an identifier.")
else:
    print(string, "is not an identifier.")

string = "user@12345"
if string.isidentifier():
    print(string, "is an identifier.")
else:
    print(string, "is not an identifier.")














