# -*-coding:utf-8-*-
# 编写input()和output()函数输入，输出5个学生的数据记录。
student=[]
N=2
for i in range (5):
    student.append(['','',[]])
    
def input_stu(stu):
    for i in range (N):
        stu[i][0]=raw_input('input student num:')
        stu[i][1]=raw_input('input student name:')
        for j in range (3):
            stu[i][2].append(int(raw_input('input student score:')))
            
def output_stu(stu):
    for i in range (N):
        print '%s  %s'%(stu[i][0],stu[i][1])
        for j in range (3):
            print '%d'%(stu[i][2][j])
            
if __name__=='__main__':
    input_stu(student)
    output_stu(student)