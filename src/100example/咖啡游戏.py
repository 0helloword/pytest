# -*-coding:utf-8 -*-

# 有一个咖啡列表['32Latte', '_Americano30', '/34Cappuccino', 'Mocha35']，列表中每一个元素都是由咖啡名称、价格和一些其他非字母字符组成，
# 编写一个函数clean_list()处理此咖啡列表，处理后列表中只含咖啡名称，并将此列表返回。
# __main__模块中初始化咖啡列表，调用clean_list()函数获得处理后的咖啡列表，并利用zip()函数给咖啡名称进行编号后输出，输出形式如下：
# 1 Latte 
# 2 Americano 
# 3 Cappuccino 
# 4 Mocha



def clean_list(lst):
    cleanlist=[]
    for item in(lst):
        for c in item:
            if c.isalpha()!=True:      #判断字符ch是否为英文字母，若为英文字母，返回非0
                item=item.replace(c,'')
        cleanlist.append(item)
    return cleanlist




if __name__=='__main__':
    cofelist=['32Latte', '_Americano30', '/34Cappuccino', 'Mocha35']
    cleanlist=clean_list(cofelist) 
    for k,v in zip(range(1,len(cleanlist)+1),cleanlist):
        print(k,v)
    
    
    
    
    
    