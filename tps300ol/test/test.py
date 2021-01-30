# from selenium import webdriver
import re
import json
import os

# wd = webdriver.Edge()
# wd.get('http://192.168.0.247:3000')

# db_url = 'mysql://root:123456@127.0.0.1:3306/demo'
# db_name = re.findall('mysql://.*/(.*)', db_url)
# print(db_name)

# b = b'\xa0\x00\xc2'
# a = chr(b[1]).encode()
# a1 = a.replace(b'\xc2', b'')
# print(a)
# print(a1)
# print(b)
# print(type(b[2]))
b = b'\x00\xa0'
a = chr(b[0]).encode()
print(a)
str1 = '''
[{
    "name": "Tom",
    "gender": "male"
}, {
    "name": "Jack",
    "gender": "male"   
}]
'''
# 将字符串转为json格式
print(type(str1))
data = json.dumps(str1)
print(type(data))
print(data)
print(os.getcwd())

