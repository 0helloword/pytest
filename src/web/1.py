#-*-coding:utf-8-*-

from flask import Flask
from flask import request

#app是Flask的实例，它接收包或者模块的名字作为参数，但一般都是传递__name__。
#让flask.helpers.get_root_path函数通过传入这个名字确定程序的根目录，以便获得静态文件和模板文件的目录
app = Flask(__name__)

#使用app.route装饰器会将URL和执行的视图函数的关系保存到app.url_map属性上。
#处理URL和视图函数的关系的程序就是路由，这里的视图函数就是home。
@app.route('/', methods=['GET', 'POST'])
def home():
    return '<h1>Home</h1>'

@app.route('/signin', methods=['GET'])
def signin_form():
    return '''<form action="/signin" method="post">
              <p><input name="username"></p>
              <p><input name="password" type="password"></p>
              <p><button type="submit">Sign In</button></p>
              </form>'''

@app.route('/signin', methods=['POST'])
def signin():
    # 需要从request对象读取表单内容：
    if request.form['username']=='admin' and request.form['password']=='password':
        return '<h3>Hello, admin!</h3>'
    return '<h3>Bad username or password.</h3>'

if __name__ == '__main__':
    app.run()#执行app.run就可以启动服务了