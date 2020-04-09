# importing xlrd library to analayze and examine and excel file
import xlrd 

#### this program reads and interprets elements of a spreadsheet of student grades
    ### and returns information about its elements

# creating a file, file to store grades excel sheet
file = ('Desktop\P2_StudentGrades.xlsx')

# using xlrd to open file to access data while saving it into grades
grades = xlrd.open_workbook(file)

# storing grades into a new sheet, so that the data can be used
sheet = grades.sheet_by_index(0)

# poisitioning the pointer of sheet to cell 0,0
sheet.cell_value(0,0)

# number of rows
print("The number of rows: ", sheet.nrows)

# number of columns 
print("The number of columns: ", sheet.ncols)

# printing the first column
print("First Column:")
for i in range(sheet.nrows):
    print("\t", sheet.cell_value(i,0))

# printing the first row
print("First row: Headers")
for i in range(sheet.ncols):
    print("\t", sheet.cell_value(0,i))

# printing class average 
classAverage= sheet.cell_value(sheet.nrows -1, sheet.ncols-1)
print("The class averege is ", classAverage)

# printing the grades for each student 
for i in range(sheet.nrows):
    print()
    for j in range(sheet.ncols):
        print(sheet.cell_value(0,j), ":", sheet.cell_value(i,j) )