from pymongo import MongoClient


# client = MongoClient('mongodb://root:password_Welcome%123@192.168.0.247:27017')
client = MongoClient(host='192.168.0.247', port=27017)
db = client.admin
db.authenticate('root', 'password_Welcome%123')
db = client.mjs
col = db.filelogs
re = col.find_one()
print(re)
