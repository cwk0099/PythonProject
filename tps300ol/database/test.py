# from pymongo import MongoClient
#
#
# # client = MongoClient('mongodb://root:password_Welcome%123@192.168.0.247:27017')
# client = MongoClient(host='192.168.0.247', port=27017)
# db = client.admin
# db.authenticate('root', 'password_Welcome%123')
# db = client.mjs
# col = db.filelogs
# re = col.find_one()
# print(re)
# import datetime
import time

# from dateutil import parser
#
# now = parser.parse(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
# now1 = (datetime.datetime.now() - datetime.timedelta(hours=8)).strftime("%Y-%m-%d %H:%M:%S")
# print(now)
# print(now1)
import IPy
stime = time.time()
for i in range(1000):
    for j in range(1000):
        i += 1
etime = time.time()
t = etime-stime
print(f'{t:.3}')

print(IPy.IP('111'))