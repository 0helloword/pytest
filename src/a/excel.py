#-*- coding: utf8 -*-

from os.path import join
from xlrd import open_workbook
from xlutils.copy import copy
import os,sys

class ReadAndWriteExcel:

    def __init__(self):
        self.FilePath='G:\\pythonCase\\1.xls'
        self.sheetName='test'
        self.rb='r+w+b'

    def Set_ExcelPath(self,FilePath):
        self.FilePath=FilePath.replace('\\', '/')
        self.rb=open_workbook(self.FilePath,'r+b')

#写数据
    def getfilepath(self,sheetName):
        print self.FilePath
        print self.sheetName
        

    def Write_Excel(self,sheetName,rowIndex,lineIndex,content):
        rbook=open_workbook(self.FilePath,'w')
        wb=copy(rbook)
        sheetIndex=rbook.sheet_names().index(sheetName)
        wb.get_sheet(int(sheetIndex)).write(int(rowIndex),int(lineIndex),content)
        wb.save(self.FilePath)
        print 'write file ok'

# 获取某一行数据
    def Get_RowIndexData_By_SheetName(self,sheetName,rowIndex):
        return self.rb.sheet_name(sheetName).row_values(int(rowIndex))

#获取某一列数据
    def Get_ColIndexData_By_SheetName(self,sheetName,colIndex):
        return self.rb.sheet_by_name(sheetName).col_values(int(colIndex))

#获取总行数
    def Get_RowCount_By_SheetName(self,sheetName):
        return int(self.rb.sheet_by_name(sheetName).nrows)

# 获取总列数
    def Get_columnCount_By_SheetName(self,sheetName):
        return int(self.rb.sheet_by_name(sheetName).ncols)

# 获取某个单元格的值
    def Get_Cell_By_ColIndex_RowIndex(self,sheetName,rowIndex,colIndex):
        return self.rb.sheet_by_name(sheetName).cell_value(int(rowIndex),int(colIndex))
    
    
tt=ReadAndWriteExcel()
tt.getfilepath('test')
tt.Write_Excel('test',0,1,'ddd')
tt.Get_ColIndexData_By_SheetName('test',0)


if __name__ == '__main__':
    pass