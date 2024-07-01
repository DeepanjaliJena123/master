#exa
import string
# result=string.digits
# print(result)

# def check(value):
#     for letter in value:
#         if letter not in string.digits:
#             return False
#     return True
#
# res="geek123"
# res2="12345"
#
# print(res,check(res))
# print(res2,check(res2))
def check(value):
    for letter in value:
        if letter in string.digits:
            return True
        return False
res="12345"
r="gd456"
print(check(res))












