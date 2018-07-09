# Score    Grade
# 90~100    A
# 70~89    B
# 60~69    C
# 0~59    D
# others    Invalid score
# 运用try-except语句让程序可以处理非数字输入的情况，如果是非数字输入，打印消息并允许用户再次输入，直到输入正确类型值计算出结果后退出

def grade(score):
    if score>90 and score<=100:
        print 'your grade is A'
    elif score>70 and score<90:
        print 'your grade is B'
    elif score>60 and score<70:
        print 'your grade is C'
    elif score>0 and score<60:
        print 'your grade is D'
    else:
        print 'invalid score'
          
    
while True:   
    try: 
        score=int(raw_input('input your score:'))
        grade(score)
    except ValueError:
        print 'error,please input a digit:'





