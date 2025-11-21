# 将数据添加到XLS文件,XLS的原数据不丢失
#coding:utf-8

# xlrd==2.0.1
# xlutils==2.0.0
# xlwt==1.3.0

# file_path:文件名(可以包括路径)
# oneRowData:一行的数据

from xlutils.copy import copy
import xlrd,xlwt,os
def addToXLS(file_path,oneRowData,rowNum):
    # 打开想要更改的excel文件
    excel_temp = xlrd.open_workbook(file_path, formatting_info=True)
    # 将操作文件对象拷贝，变成可写的workbook对象
    new_excel = copy(excel_temp)
    # 获得第一个sheet的对象
    ws = new_excel.get_sheet(0)
    ncols=len(oneRowData)
    for col in range(ncols):
        ws.write(rowNum, col, oneRowData[col]) #单元格A1开始，即(0,0)
        # break
    # 另存为excel文件，并将文件命名，可以重新命名，应该也可以覆盖掉
    new_excel.save(file_path)
    # print("数据已经保存到xls文件")

if __name__ == '__main__':
    file_path = "./stu_info.xls"
    oneRowData = [1,2,3,4,5,6,7,8,9,10]
    addToXLS(file_path,oneRowData,0)