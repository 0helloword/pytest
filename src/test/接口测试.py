#-*-coding=utf-8-*-
import sys
reload(sys)
# sys.setdefaultencoding( "utf-8" )
import requests,xlrd

def jiekou():
    workbook=xlrd.open_workbook( u"E:/个人信息.xls")
#     sheet=workbook.sheet_by_index(0)
    sheet=workbook.sheet_by_name(u'111')
    nrows=sheet.nrows
    if nrows==11:
        url = str(sheet.cell(0, 0).value)
        headers = eval(str(sheet.cell(1, 0).value))
        req=requests.post(url=url,data=None,headers=headers)
    else:
        url = str(sheet.cell(0, 0).value)
        headers = eval(str(sheet.cell(1, 0).value))
        body = eval(str(sheet.cell(2, 0).value))
        req = requests.post(url=url, data=body, headers=headers)
    print req.text
    print headers

if __name__ == "__main__":
    jiekou()
    pass