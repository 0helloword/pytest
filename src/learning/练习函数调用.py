# -*-coding:UTF-8 -*-

def helloworld():
    print 'helloworld'
    
def three_hellos():
    for i in range(3):
        helloworld()
helloworld()

if __name__=='__main__':
    three_hellos()
    