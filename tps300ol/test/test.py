# from selenium import webdriver
import re

# wd = webdriver.Edge()
# wd.get('http://192.168.0.247:3000')

# db_url = 'mysql://root:123456@127.0.0.1:3306/demo'
# db_name = re.findall('mysql://.*/(.*)', db_url)
# print(db_name)

b = b'\xa0\x00\xc2'
a = chr(b[1]).encode()
a1 = a.replace(b'\xc2', b'')

print(a1)
print(type(b[2]))

