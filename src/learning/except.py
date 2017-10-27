#-*-coding:utf-8 -*-
from _ssl import err_codes_to_names

while True:
    try:
        a=int(raw_input('input a:'))
        b=int(raw_input('input b:'))
        c=a/b
        print c
        break
# except ValueError:
#     print 'please input a digit'
#     
# except ZeroDivisionError:
#     print 'the second number can not be zero'
    
# 等同于
# except (ValueError,ZeroDivisionError):
#     print 'invalid input'    

#等同于(将所有的异常情况都包含了)
# except:
#     print 'some error'

#等同于(将所有的异常情况都包含了,并且打印错误信息)    
    except Exception as err:
        print 'someting went wrong'
        print (err)
    else:
        print 'everything is ok'