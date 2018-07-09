# #-*-coding:utf-8-*-
# 
# 
# import json
# 
data='{"body":{"mobile":"15611112222","memberId":"123456"},"header":{"format":"json9","token":"2881D7178BC76AE21647CB67DB116911"}}'
# a = json.loads(b)
# print a['header']['token']


# -*- coding: utf-8 -*-

import json

def update_token(data,token):
    a=json.loads(data)
    a['header']['token']=token
    print a
pass
    
if __name__ == "__main__":
    pass