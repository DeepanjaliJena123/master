#
# # # Step 1: Create a text file and add content
# file_path = 'sample_file.txt'
#
# with open(file_path, 'w') as file:
#     file.write("Name: Your Name\nTitle: Your Title")
#
# # Step 2: Read the content of the file
# with open(file_path, 'r') as file:
#     file_content = file.read()
#     print("Content of the file:")
#     print(file_content)

# # # # Step 3: Delete the file
# # # import os
# # #
# # # os.remove(file_path)
# # # print(f"\nFile '{file_path}' has been deleted.")
#
#
# #PRACTICE
#
# # F=open('C:\DOWNLOAD\SAMPLE.txt','r')
#
# # for each in F:
# #     print(each)
#
# # # Python code to illustrate read() mode
# # print(F.read())
#
#
# #exa2: we will see how we can read a file using the with statement in Python.
#
# # with open('C:\DOWNLOAD\SAMPLE.txt') as file:
# #     data=file.read()
# # print(data)
#
# #exa3:Python code to illustrate split() function
#
# # with open('C:\DOWNLOAD\SAMPLE.txt','r') as file:
# #     data=file.readline()
# #     for line in data:
# #         word=line.split()
# #         print(word)
# C:\\Users\\deepa\\PycharmProjects\\pyprogram\\final\\OOPS\\demo.txt
# #exa4:
# #python code create a file
# import os
# with open('../../Selenium/geek.txt', 'w+') as file:
#     file.write("Hello Python\n")
#     file.write("This is programming language")
# # file.close()
#
# # file=open('geek.txt','w+')
#     data=file.readlines()
#     # print(data[0])
# # os.remove('geek.txt')
#
#
# x=['hello hi','welcome to','python class']
#
# for i in x:
#     i.split()
#     print(i.__dict__split())
#
#
#
#
#
#
# #exa4:written statement along with the  with() function.
#
# # with open('C:\DOWNLOAD\SAMPLE.txt','w') as f:
# #     f.write("hello world")
#


##############################################################################
#new
# Python supports file handling ,and allows users to handle files i.e.,
# to read and write files, along with many other file handling options, to operate on files.
#

#exa:
# r: open an existing file for a read operation.
# w: open an existing file for a write operation. If the file already contains some data,
# then it will be overridden but if the file is not present then it creates the file as well.
# a:  open an existing file for append operation. It won’t override existing data.
# r+:  To read and write data into the file. The previous data in the file will be overridden.
# w+: To write and read data. It will override existing data.
# a+: To append and read data from the file. It won’t override existing data.
#


#exa: a file named "demo.text", will be opened with the reading mode.

# file=open('demo.txt','r')
# for each in file:
#     print(each)

#exa2:
# file=open('demo.txt','r')
# print(file.read())
#

#exa3: read file 'with' statement, it will be closed the file atumatically after the execute.
# with open('demo.txt') as file:
#     data=file.read()
# print(data)

#exa4: it will give 1st 5 character of stored data
# file=open('demo.txt','r')
# print(file.read(5))

#exa5:We can also split lines while reading files in Python
# with open('demo.txt','r') as file:
#     data=file.readlines()
#     for line in data:
#         word = line.split()
#         print(word)

###### Creating a File using the write() Function
# file=open('demo_create.txt','w')
# file.write("This is file handling in python.")
# file.write("This file handling by geek for geeks")
# file.close()

#or We can also use the written statement along with the  with() function.
# with open('demo2.text','w') as f:
#     f.write("This is the writing option")

########  Working of Append Mode
# file=open('demo2.text','a')
# file.write("\n We can also append the data in file using 'a'.")
# file.close()

########### Practice #####
# file='welcome to abc@gmail.com and zyx@yahoo.com and akj@gov.in python'
# file=open('practice.text','w')
# file.write("welcome to abc@gmail.com and zyx@yahoo.com and akj@gov.in python")
# # file.close()
#
# #print only emails id
# with open('practice.text','r') as file:
#     rd=file.read()
#     for i in rd.split():
#         for j in range(len(i)):
#             if i[j]=='@':
#                 print(i)

#### 
#exa:from file containing numbers separated by comma,print the count of even numbers.
#1,2,45,55,86,76
# count=0
# with open("demo.txt",'r') as f:
#     data=f.read()
#
#     nums=data.split(',')
#     for val in nums:
#         if (int(val)%2==0):
#             count+=1
# print(count)

#################### Excel Handling ###########
# import openpyxl
# path=("C:\\DOWNLOAD\\excel_prac.xlsx")
# obj=openpyxl.load_workbook(path)
# obj1=obj.active
# cell_obj=obj1.cell(row=1,column=1)
# print(cell_obj.value)



#exa:: We can get the count of the total rows and columns using the max_row and max_column respectively
# import openpyxl
# path=("C:\\DOWNLOAD\\excel_prac.xlsx")
# wb_obj=openpyxl.load_workbook(path)
# sheet_obj=wb_obj.active
# row=sheet_obj.max_row
# column=sheet_obj.max_column
# print("max row",row)
# print("max coloumn",column)


#
# #print value of 1st column
# for i in range(1,row+1):
#     cell_obj=sheet_obj.cell(row=i,column=1)
#     print(cell_obj.value)
#
# #print value of 1st row
# for i in range(1,column+1):
#     cell_obj=sheet_obj.cell(row=2,column=i)
#     print(cell_obj.value,end=" ")

#exa::Read from Multiple Cells Using the Cell Name
#
# import openpyxl
# path="C:\\DOWNLOAD\\excel_prac.xlsx"
# wb_obj=openpyxl.load_workbook(path)
# sheet_obj=wb_obj.active
# cell_obj=sheet_obj['A1':'B5']

# for cell1,cell2 in cell_obj:
#     print(cell1.value,cell2.value)



##exa::create a new spreadsheet, and then we will write some data to the newly created file.
# An empty spreadsheet can be created using the Workbook() method.
# from openpyxl import Workbook
# workbook=Workbook()
# workbook.save(filename="sample.xlsx")
#
# import openpyxl
# wb = openpyxl.Workbook()
# sheet=wb.active
# c1=sheet.cell(row=1,column=1)
# c1.value="Name"
# c2=sheet.cell(row=1,column=2)
# c2.value="Program"
#
# # c3=sheet.cell(row=2,column=1)
# # c3.value="Deepa"
# # c4=sheet.cell(row=2,column=2)
# # c4.value="Python"
#
# c3=sheet['A2']
# c3.value="Deepa"
# c4=sheet['B2']
# c4.value = "java"
# wb.save("sample.xlsx")


##exa:: adding rows with values (1, 2, 3) and (4, 5, 6).
# import openpyxl
# wb=openpyxl.load_workbook("sample.xlsx")
# sheet=wb.active
# data=(
#     (1,2,3),
#     (4,5,6)
# )
# for row in data:
#     sheet.append(row)
#     print(row)
# wb.save("sample.xlsx")


#Arithmetic Operation on Spreadsheet

# import openpyxl
# wb=openpyxl.Workbook()
# sheet=wb.active
# sheet['A10']=200
# sheet['A11']=300
# sheet['A12']=100
#
# sheet['A13']='SUM=A10:A12'
#
# wb.save("sample.xlsx")


# ##########    Python Delete File #######
# import os
# os.remove("create_file1.text")

#########  Check if File exist: ######3
# import os
# if os.path.exists("sample5.text"):
#     os.remove("sample5.text")
# else:
#     print("file not exist")

###### Delete Folder
# To delete an entire folder, use the os.rmdir() method:
# import os
# os.rmdir("lkl")



##################################










