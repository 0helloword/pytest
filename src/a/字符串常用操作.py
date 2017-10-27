# -*-coding:utf-8 -*-

#s.capitalize() 返回字符串s首字母大写其余小写的形式
s='hello WORLD'
print s.capitalize()

#s.lower() 返回字符串s的小写形式
print s.lower()

#s.upper() 返回字符串s的大写形式
print s.upper()

#s.title() 返回字符串s的标题形式即单词首字母大写形式
print s.title()

#s.format(*args, **kwargs) 格式化字符串操作,foramt会把参数按位置顺序来填充到字符串中，第一个参数是0，然后1 ……
print 'this is {} book'.format('a', 'b','c')
print 'this is {} book,that is a {},{}'.format('a', 'ball','hello')
print 'this is {1} book,that is a {0},{2}'.format('a', 'ball','hello')

#s.count(sub[, start[, end]]) 返回指定字符在[指定位置的]字符串s中出现的次数
print s.count('l')
print s.count('l',5,10)

#s.find(sub[, start[, end]]) 返回指定字符在[指定位置的]字符串s中出现的索引号，找不到则返回-1
print s.find('h')
print s.find('h',5,10)

#s.index(sub[, start[, end]]) 与 find()类似，不同的是如果找不到会引发ValueError异常
print s.index('h')
# print s.index('h',5,10)

#s.replace(old, new[, count]) 把字符串s中的old（旧字符串）替换成new（新字符串）。如果指定第三个参数count，则仅仅替换前count次出现的子串
s1='hello world'
print s1.replace('o', 'a')
s2='hello world'
print s2.replace('o', 'a',1)

#s.lstrip([chars]) 移除字符串s左边的指定字符（默认为空格），返回移除字符串s左边指定字符后生成的新字符串
s='  hello,  world  '
print s.lstrip()
s='hello,  world  '
print s.lstrip('h')

#s.rstrip([chars]) 移除字符串s末尾的指定字符（默认为空格），返回移除字符串s末尾指定字符后生成的新字符串
s='  hello,  world  '
print s.rstrip()
s='  hello,  world'
print s.rstrip('d')

#s.strip([chars]) 移除字符串s头尾指定的字符（默认为空格），返回移除字符串s头尾指定字符后生成的新字符串
s='  hello,  world  '
print s.strip()
s='hello,  worlh'
print s.strip('h')

#s.join(a) 用字符串s来分隔/连接字符串a
s='sunny'
print s.join('123')
print ''.join('123')
print ':'.join('123')

#s.split(sep=None, maxsplit=-1) 以指定的字符作为分隔符（默认为空格）分割字符串s，maxsplit指分割次数（默认为不限制次数）
s='hello everyone'
print s.split('o',2)
print s.split()

#s.endswith(suffix[, start[, end]]) 判断字符串s[的指定位置]是否以后缀suffix结尾
print s.endswith('one')
print s.endswith('o',0,5)

#s.startswith(prefix[, start[, end]]) 判断字符串s[的指定位置]是否以前缀prefix开头
print s.startswith('he')
print s.startswith('e',6,10)