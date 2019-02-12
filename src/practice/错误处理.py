# -*-coding:utf-8-*-

try:
    print 'try……'
    a=10/int('b')
    print 'result:',a
except ZeroDivisionError as e:
    print 'except:',e
except ValueError as e:
    print 'except:',e
finally:
    print 'finally...'
print 'end'