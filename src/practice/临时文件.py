#-*-coding:utf-8-*-

import json

def update_Prd(data,productId):
    a=json.loads(data)
    a['body']['productId']=productId
    return a
pass
    
if __name__ == "__main__":
    pass