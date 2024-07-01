#calculator::
# class Calculator:
#     def operation(self, action,*args):
#
#         if action=='add':
#             total = 0
#             for i in args:
#                 total+=i
#         print(total)
#
# obj=Calculator()
# obj.operation('add',1,5,6)


# class Calculator:
#     def operation(self, action,a,b):
#         if action=='add':
#             total = a+b
#             print(total)
#
#     def sub(self, action,a,b):
#         if action=='sub':
#             total=b-a
#             print(total)
#
#
# obj=Calculator()
# obj.operation('add',a=2,b=3)
# obj.sub('sub',a=2,b=5)


# class Reversed_NAME:
#
#     def name_rev(name):
#         name="i am deepanjali jena"
#         v=name.split()
#         rev = ""
#         for i in v:
#             rev=i+' '+rev
#         print(rev)
#
# obj=Reversed_NAME()
# obj.name_rev()



#######
# class Reversed_NAME:
#
#
#     def name_rev(name):
#         name=input("enter string :")
#         v=name.split()
#         rev = ""
#         for i in v:
#             rev=i+' '+rev
#         print(rev)
#
# obj=Reversed_NAME()
# obj.name_rev()



#find even odd number using class method
#
# class EvenOdd():
#     def even_number(even):
#         even_num=[]
#         for i in s:
#             if i % 2 == 0:
#                 even_num.append(i)
#         print(even_num)
#
#
#     def Odd_number(odd):
#         odd_num=[]
#         for i in s:
#             if i % 2 != 0:
#                 odd_num.append(i)
#         print(odd_num)
#
# s=[4,5,7,9,11,10]
#
# obj=EvenOdd()
# obj.even_number()
# obj.Odd_number()



# Define a class called Calculator to perform basic arithmetic operations
# class Calculator:
#     # Define a method for addition that takes two arguments and returns their sum
#     def add(self, x, y):
#         return x + y
#
#     # Define a method for subtraction that takes two arguments and returns their difference
#     def subtract(self, x, y):
#         return x - y
#
#     # Define a method for multiplication that takes two arguments and returns their product
#     def multiply(self, x, y):
#         return x * y
#
#     # Define a method for division that takes two arguments and returns the result if the denominator is not zero,
#     # or an error message if the denominator is zero
#     def divide(self, x, y):
#         if y != 0:
#             return x / y
#         else:
#             return ("Cannot divide by zero.")
#
# # Example usage
# # Create an instance of the Calculator class
# calculator = Calculator()
#
# # Perform addition and print the result
# result = calculator.add(7, 5)
# print("7 + 5 =", result)
#
# # Perform subtraction and print the result
# result = calculator.subtract(34, 21)
# print("34 - 21 =", result)
#
# # Perform multiplication and print the result
# result = calculator.multiply(54, 2)
# print("54 * 2 =", result)

# # Perform division and print the result
# result = calculator.divide(144, 2)
# print("144 / 2 =", result)
#
# # Attempt to perform division by zero, which raises an error, and print the error message
# result = calculator.divide(45, 0)
# print("45 / 0 =", result)


#exa:
#separate all value and numbers:
# def separate(values):
#     z=''
#     for i in values:
#         if i.isnumeric():
#             pass
#         else:
#             z+=i
#     print(z)
# values="hello wel1come t2o pyth4on"
# separate(values)


#exa:
#find vowels count
# def vowels_count(alphabates):
#     count=0
#     for i in alphabates:
#         if i in vowel:
#             count+=1
#     print(count)
# vowel="a,e,i,o,u"
# alphabates = "hello welcome to python"
# vowels_count(alphabates)

#
#exa:
#remove all speacial characters
# def charachter(a):
#     new_str = ""
#     for char in a:
#         if char.isalnum() or char.isspace():
#             new_str += char
#     print(new_str)
#
# a = 'hel$lo wel*come to@ pyt#&on'
# charachter(a)
#
#

# #exa: Reverse a list using loop
# s=[10,20,30,40]
# z=[]
# y=1
# for i in range(len(s)):
#     z.append(s[-y])
#     y+=1
# print(z)


#
# s = "ABAABBCA"
# chr=[]
# y=[]
# for i in s:
#   if i not  in chr:
#       chr.append(i)
# print(y)

# x = "5,0.2,1,0.9,2"
# y = x.split(',')
# print("Original:", y)
#
# # Convert string elements to float
# y = [float(num) for num in y]
#
# # Bubble sort algorithm
# for i in range(len(y)):
#     for j in range(i+1, len(y)):
#         if y[i] > y[j]:
#             y[i], y[j] = y[j], y[i]
#
# # Convert sorted float list back to string
# sorted_x = ','.join(map(str, y))
# print("Sorted:", sorted_x)








#Exa
# x="5,0.2,1,0.9,2"   #ascending
#
# # for i in range(len(x)):
# y=x.split(',')
# print(y)
# for i in range(len(y)):
#     for j in range(i,len(x)):
#         if x[i]>x[j]:
#             x[i],x[j]=x[j],x[i]
#             print(x)
#



# x="deepa"
# y="jena"
# # print common letter, if common letter not there print else block not there
#
# ltr=[]
# for i in x:
#     if i in y:
#         ltr.append(i)
# print("common letter :",ltr)
#
#









#
#
# x = "deepa"
# y = "jena"
#
# # Initialize a list to store common letters
# common_letters = []
#
# # Iterate over each letter in x
# for letter in x:
#     # Check if the letter is in y
#     if letter in y:
#         common_letters.append(letter)
#
# # Check if there are any common letters
# if common_letters:
#     print("Common letter(s):", common_letters)
# else:
#     print("No common letter")



















