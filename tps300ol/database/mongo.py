import time
from pymongo import MongoClient, InsertOne
import datetime
from threading import Thread
# mongodb多线程批量插入1KW条数据

def insertmongo(host, port):
    global num
    client = MongoClient(host=host, port=port)
    db = client.admin
    db.authenticate('root', 'password_Welcome%123')
    db = client.mjs
    col = db.clientlogs
    arr = list()
    now = (datetime.datetime.now() - datetime.timedelta(hours=8)).strftime("%Y-%m-%d %H:%M:%S")
    for i in range(10):
        for j in range(200000):
            data = {
                'ip': "192.168.0.111",
                'username': "admin",
                'name': "",
                'action': "用户登录",
                'content': "用户登录",
                'code': 0,
                'createTime': now,
                '__v': 0
            }
            arr.append(InsertOne(data))
        col.bulk_write(arr)
        arr = []


if __name__ == '__main__':
    h = input('请输入mangodb的ip：')
    p = input('请输入端口:')
    p = int(p)
    threads = list()
    start_time = time.time()
    for k in range(5):
        threads.append(Thread(target=insertmongo, args=(h, p)))
        threads[k].start()
        time.sleep(0.5)
    print('正在执行中，请稍候6-8分钟...')
    for t in threads:
        t.join()
    end_time = time.time()
    print(f'执行完成,共运行了：{end_time-start_time}s')