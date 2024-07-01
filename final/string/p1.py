# x=['1',2,'3',4,5]
# for i in x:
#     print(type(i))
#
# x=['hi,hello','wel:come:to']
# for i in x:
#     print(i.split(':'))

################################################
#string.ascii_letters:
# import string
#
# result=string.ascii_letters
# print(result)


#exa2
 # Given code checks if the string input has only ASCII characters or not.

import string

def check(value):
    for letter in value:
        if letter not in string.ascii_letters:
            return False

        return True

input="geek"
print(input,check(input))

input2="python_java"
print(input2,check(input2))

