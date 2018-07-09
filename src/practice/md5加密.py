#-*-coding:utf-8-*-
import hashlib
#将用户密码使用md5加密，并且进行加盐,与数据库中数据进行对比，判断用户是否登录成功
db={'caoyj':'d330ec7ec97c3b3109d7c98376bf308c','theone':'79c094c17bc0377d40a0e45f374d72e2'}

def get_md5(password):
    md5=hashlib.md5()
    md5.update(password)
    return md5.hexdigest()

def salt_get_md5(password,username):
    return get_md5(password+username+'salt')

def isuser(username):
    if username in db:
        return 1
    else:
        return 0


def login(username,password):

    if isuser(username)==1 and salt_get_md5(password, username)==db[username]:
        print 'login success'
    else:
        print 'password or username error'
#     print salt_get_md5(password, username)
    

login('caoyj','123456')
login('caoyj1','123456')

