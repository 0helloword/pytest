# -*-coding:UTF-8 -*-


a=(raw_input('input string:'))
letters=0
space=0
digit=0
others=0
for c in a:
    if c.isalpha():
        letters+=1
    elif c.isspace():
        space+=1
    elif c.isdigit():
        digit+=1
    else:
        others+=1
print 'letters is %d,space is %d,digit is %d,others is %d' %(letters,space,digit,others)




