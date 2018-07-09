# -*-coding:UTF-8 -*-
N=5
if __name__=='__main__':
    s=[]
    for i in range (N):
        s.append(int(raw_input('input num:')))
    print s
    
    for i in range (N/2):
        t=s[i]
        s[i]=s[N-1-i]
        s[N-1-i]=t
    print s    
