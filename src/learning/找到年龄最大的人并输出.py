# -*-coding:UTF-8 -*-

if __name__=='__main__':
    person={"li":33,"wang":89,"zhang":12}
    max="li"
    for key in  person.keys():
        if person[max]<person[key]:
             max=key
    print '%s  %d'%(max,person[max])
