#exa   Continue with While Loop

# i=0
# while i<10:
#     if i == 5:
#         i += 1
#         continue
#     print(i)
#     i += 1                                  dpubt
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









# ## input size of the list
# n = int(input("Enter the size of list : "))
# # store integers in a list using map,
# # split and strip functions
# lst = list(map(int, input("Enter the integer\
# elements:").strip().split()))[:n]
#
# # printing the list
# print('The list is:', lst)                                      doubt





l = [1, 1, 2, 2, 2, 3, 3, 4, 4, 5, 5]
ele=1
x=[i for j,i in enumerate(l) if i==ele]
print("the element",ele,"occurs",len(x),"times")


#exa
# function that filters vowels
def fun(variable):
    letters = ['a', 'e', 'i', 'o', 'u']
    if (variable in letters):
        return True
    else:
        return False


# sequence
sequence = ['g', 'e', 'e', 'j', 'k', 's', 'p', 'r']

# using filter function
filtered = filter(fun, sequence)

print('The filtered letters are:')
for s in filtered:
    print(s)



##my_tuples = [(1, "one"), (3, "three"), (2, "two"), (4, "four")]
sorted_tuples = sorted(my_tuples, key=lambda x: x[1])
print(sorted_tuples)

#[(4, 'four'), (1, 'one'), (3, 'three'), (2, 'two')]






