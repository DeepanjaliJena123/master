#read existing file
# file=open("file1.text","r")
# for i in file:
#     print(i)0

#or normal reading only
# file=open("file1.text",'r')
# print(file.read())

#for with statement
# with open("file1.text",'r') as file:
#     data=file.read()
# print(data)

# #print 1st 5 character
# file=open("file1.text",'r')
# print(file.read(5))

#splits the lines
# with open('file1.text','r') as file:
#     data=file.readlines()
#     for line in data:
#         split_chr=line.split()
#         print(split_chr)

#create file
# file=open('create_file.text','w')
# file.write("this is create file")
# file.write("\nthis is python handling file")
# file.close()

#or using 'with open'
# with open('create_file1.text','w') as f:
#     f.write("this is with open file")

#append
# file=open('create_file1.text','a')
# file.write("\nthis is for geek n geek")
# file.close()

#creat  file n print only mail.id
# file='welcome to abc@gmail.com and zyx@yahoo.com and akj@gov.in python'
# file=open('practice.text','w')
# file.write("welcome to abc@gmail.com and zyx@yahoo.com and akj@gov.in python")
# # file.close()
#
# file='welcome to abc@gmail.com and zyx@yahoo.com and akj@gov.in python'
# #print only emails id
# with open('practice.text','r') as file:
#     rd=file.read()
#     for i in rd.split():
#         for j in range(len(i)):
#             if i[j]=='@':
#                 print(i)



#####
#1,2,45,55,86,76
# count=0
# with open('p1.text','r') as f:
#     num=f.read()
#
#     nums=num.split(',')
#     for i in nums:
#         if int(i)%2==0:
#             count+=1
#     print(count)
# #

#######excel
#cell value
# import openpyxl
# path=("C:\\DOWNLOAD\\file_handling\\excel_file.xlsx")
# obj=openpyxl.load_workbook(path)
# obj1=obj.active
# cell_obj=obj1.cell(row=3,column=3)
# print(cell_obj.value)

#or
# import openpyxl
# path=("C:\\Users\\deepa\\PycharmProjects\\pyprogram\\final\\OOPS\\practice.xlsx")
# obj=openpyxl.load_workbook(path)
# obj1=obj.active
# cell_obj=obj1.cell(row=3,column=3)
# print(cell_obj.value)

#exa:: We can get the count of the total rows and columns using the max_row and max_column respectively
# import openpyxl
# path=("C:\\DOWNLOAD\\file_handling\\excel_file.xlsx")
# wb_obj=openpyxl.load_workbook(path)
# sheet_obj=wb_obj.active
# row=sheet_obj.max_row
# column=sheet_obj.max_column
# print("column size :",column)
# print("row size :",row)
#

# import openpyxl
# path=("C:\\Users\\deepa\\PycharmProjects\\pyprogram\\final\\OOPS\\practice.xlsx")
# wb_obj=openpyxl.load_workbook(path)
# sheet_obj=wb_obj.active
# row_count=sheet_obj.max_row
# column_count=sheet_obj.max_column
# print("row count:",row_count)
# print("column count:",column_count)

#or print row n column value
# # for i in range(1,row_count+1):
# #     cell_obj=sheet_obj.cell(row=i,column=1)
# #     print(cell_obj.value)
# #
# for i in range(1,column_count+1):
#     cell_obj=sheet_obj.cell(row=2,column=i)
#     print(cell_obj.value)


# print("\nvalue of first column :")
# for i in range(1,row+1):
#     cell_obj=sheet_obj.cell(row=i,column=1)
#     print(cell_obj.value)
#
# print("\nvalue of 1st row")
# for i  in range(1,column+1):
#     cell_obj1=sheet_obj.cell(row=2,column=i)
#     print(cell_obj1.value)

####Read from Multiple Cells Using the Cell Name
# import openpyxl
# path=("C:\\DOWNLOAD\\file_handling\\excel_file.xlsx")
# wb_obj=openpyxl.load_workbook(path)
# sheet_obj=wb_obj.active
# cell_obj=sheet_obj['A1':'C11']
# for cell1,cell2,cell3 in cell_obj:
#     print(cell1.value,cell2.value,cell3.value)



######### Print a particular row value

# import openpyxl
# path=("C:\\DOWNLOAD\\file_handling\\excel_file.xlsx")
# wb_obj=openpyxl.load_workbook(path)
# sheet_obj=wb_obj.active
# col_max=sheet_obj.max_column
# for i in range(1,col_max+1):
#     cell_obj=sheet_obj.cell(row=1,column=i)
#     print(cell_obj.value,end=" ")        ### NO NAME AGE

########## Python Write Excel File/create
# from openpyxl import Workbook
# workbook=Workbook()
# workbook.save("sampledemo.xlsx")

# After creating an empty file, let’s see how to add some data to it using Python.
# from openpyxl import Workbook
# workbook=Workbook()
# workbook.save("sampledemo.xlsx")
#
# import openpyxl
# wb=openpyxl.Workbook()
# sheet=wb.active
# c1=sheet.cell(row=1,column=1)
# c1.value="hello"
# c2=sheet.cell(row=1,column=2)
# c2.value="Python"

# c3=sheet["A2"]
# c3.value="a2"
# c4=sheet['A4']
# c4.value="a3"
# c5=sheet['B3']
# c5.value="java"
# wb.save("sampledemo.xlsx")
#
#


###########################################################################################################
#exa: read existing file
# file=open("o1.text","r")
# # for i in file:
# #     print(i)          #doubt giving space
# #or
# print(file.read())


#exa read lines
# with open("o1.text","r") as file:
#     data=file.readlines()
#     for line in data:
#         word=line.split()
#         print(word)

#exa write
# file=open("g.text","w")
# file.write("This is Python Program")
# file.close
# #for read the file
# file=open("g.text","r")
# print(file.read())

#or
# with open("g.text",'w+') as file:
#     file.write("Hello Print,\n")
#     file.write("hi JAVA")
#
# #for read
# with open("g.text",'r') as file:
#     print(file.read())

#exa
# file=open("g.text",'a')
# file.write("\ni am mama")
#

#delete file
# import os
# os.remove("g.text")
# print("file deleted")


######################################## excel


























