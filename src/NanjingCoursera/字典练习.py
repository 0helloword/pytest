# -*-coding:utf-8-*-
# 用字典创建一个平台的用户信息（包含用户名和密码）管理系统，
# 新用户可以用与现有系统帐号不冲突的用户名创建帐号，已存在的老用户则可以用用户名和密码登陆重返系统

systeminfo={'caoyj':123456,'theone':888888}

def newuser():
    name=raw_input('input your name:')
    if name in systeminfo.keys():
        print 'Already exist'
    else:
        pwd=raw_input('input your password:')
        systeminfo[name]=pwd
    print systeminfo
    
def olduser():
    name=raw_input('input your name:')
    pwd=raw_input('input your pwd:')
    if str(systeminfo[name])==pwd:
        print 'login success'
    else:
        print 'username or pwd error'
    
def login():
    print '(N)ew User Login\n(O)ld User Login\n(E)xit'
    choice=raw_input('your choice:')
    if choice=='N':
        newuser()
    elif choice=='O':
        olduser()    
    else:
        print 'exit'
    
if __name__ == '__main__':  
    login()