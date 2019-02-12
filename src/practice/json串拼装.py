#-*-coding:utf-8-*-
import json

class Customer: 
    def __init__(self, body,header): 
#         self.name = name 
#         self.grade = grade 
#         self.age = age 
        self.body = body
        self.header = header
    def __repr__(self): 
        return repr((self.body, self.header)) 

# class body:
#     def __init__(self):
# #         self.home = home
# #         self.office = office
#     def __repr__(self): 
#         return repr((self.name, self.grade, self.age))
    
class header:
    def __init__(self, token):
        self.token = token
    def __repr__(self): 
        return repr((self.token))

customers = [{"body":{"a":"1"},"header":{"token":"2"}}]

json_str = json.dumps(customers, default=lambda o: o.__dict__, sort_keys=True, indent=4)
print json_str