#-*- coding: utf8 -*-


from xlrd import open_workbook
from xlutils.copy import copy



FilePath1='G:\\pythonCase\\userlogin-sit.xls'
sheetName=None
rb='r+w'


FilePath=FilePath1.replace('\\', '/')
rb=open_workbook(FilePath,'r')

#写数据
def Write_Excel(sheetName,rowIndex,lineIndex,content):
    rbook=open_workbook(FilePath,'w')
    wb=copy(rbook)
    sheetIndex=rbook.sheet_names().index(sheetName)
    wb.get_sheet(int(sheetIndex)).write(int(rowIndex),int(lineIndex),content)
    wb.save(FilePath)
    print 'write file ok'




Write_Excel('Sheet2',0,1,'ddd123')


if __name__ == '__main__':
    pass




