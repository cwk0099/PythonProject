import time
import datetime
from pymongo import MongoClient, InsertOne, errors
from threading import Thread
import os
# mongodb多进程批量插入700W条数据

# 插入数据进程
class InMongo:
    def __init__(self):
        self.__host = None
        self.__port = None

    @staticmethod
    def insertmongo(host, port):
        global num
        client = MongoClient(host=host, port=port, serverSelectionTimeoutMS=20000, socketTimeoutMS=30000)
        db = client.admin
        db.authenticate('root', 'password_Welcome%123')
        db = client.mjs
        col = db.clientlogs
        arr = list()
        now = (datetime.datetime.now() - datetime.timedelta(hours=8)).strftime("%Y-%m-%d %H:%M:%S")
        for i in range(10):
            for j in range(20000):
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

    # 验证ip是否正确
    @staticmethod
    def validate_ip(ipaddr):
        ips = ipaddr.split('.')
        if len(ips) != 4:
            return False
        for index, ip in enumerate(ips):
            try:
                int_ip = int(ip)
            except ValueError:
                return False
            if 0 > int_ip or int_ip >= 255:
                return False
        return True

    # 验证能否连得上目标mongodb
    def validate_conn(self):
        while True:
            while True:
                self.__host = input('请输入mongodb的ip：')
                if self.validate_ip(self.__host):
                    break
                else:
                    print('非法ip！')
                    continue
            while True:
                self.__port = input('请输入mongodb的端口:')
                try:
                    self.__port = int(self.__port)
                    if 0 > self.__port or self.__port > 65535:
                        print('非法端口！')
                        continue
                except ValueError:
                    print('非法端口')
                    continue
                break
            try:
                client = MongoClient(host=self.__host, port=self.__port, serverSelectionTimeoutMS=10000, socketTimeoutMS=10000)
                db = client.admin
                db.authenticate('root', 'password_Welcome%123')
            except (errors.ConnectionFailure, errors.ServerSelectionTimeoutError, errors.ExecutionTimeout,
                    errors.NetworkTimeout, errors.PyMongoError, TypeError, WindowsError) as e:
                print('连接错误，请检查设置或网络环境!')
                print(f'错误信息如下:{e}')
                en = input('请输入enter键重新输入，输入其他键退出：')
                if en == '':
                    continue
                else:
                    return False
            break
        return True

    def gethp(self):
        return self.__host, self.__port


if __name__ == '__main__':
    insermong = InMongo()
    if insermong.validate_conn():
        threads = list()
        start_time = time.time()
        ho, po = insermong.gethp()
        print('连接成功，正在执行中，请稍等...')
        for k in range(5):
            threads.append(Thread(target=insermong.insertmongo, args=(ho, po)))
            threads[k].start()
            time.sleep(0.5)
        for t in threads:
            t.join()
        end_time = time.time()
        print(f'执行完成,共运行了：{(end_time - start_time):.2f}s')
        os.system('pause')
    else:
        print('程序退出！')
        os.system('pause')