import xlrd

excel = xlrd.open_workbook("./data/data.xls") #打开excel
sheet = excel.sheet_by_index(0)#指定工作表

print(sheet.nrows)#有效数据行数
print(sheet.ncols)#有效数据列数

print(sheet.row_values(0))#打印标题行
print(sheet.row_values(1))#打印第一行

print(sheet.cell(1,0).value)#打印第二行第一列单元格的值


sheet1 = excel.sheet_by_name("注册")
for i in range(1,sheet1.nrows):
    print(sheet1.row_values(i))