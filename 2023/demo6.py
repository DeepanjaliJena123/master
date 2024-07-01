# # "abcabcbb"
# # Output: 3
#
# x="abcabcbb"
# uniq=""
# count=0
# for i in x:
#     if i not in uniq:
#         uniq+=i
# print(uniq)
#

nums = [4,3,2,7,8,2,3,1]
uniq=[]
dup=[]
for i in nums:
    if i not in uniq:
        uniq.append(i)
    else:
        dup.append(i)
print(dup)
print(uniq)
















