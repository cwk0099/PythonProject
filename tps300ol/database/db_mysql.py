import datetime
from pythink import ThinkModel, ThinkDatabase
import os
import pymysql

pymysql.install_as_MySQLdb()
# from urllib import parse
passwd = 'password_Welcome%123'
# 防止密码含有特殊字符，把密码url编码化，防止报错
# npasswd = parse.quote_plus(passwd)
# 校验ip
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


while True:
    url = input('请输入要连接的数据库url：')
    if validate_ip(url):
        break
    else:
        print('ip有误，请重新输入!')
        continue
while True:
    port = input('请输入mysql的端口:')
    try:
        port = int(port)
        if 0 > port or port > 65535:
            print('非法端口！')
            continue
    except ValueError:
        print('非法端口')
        continue
    break
db_url = f'mysql://root:{passwd}@{url}:{port}/mjs'
db = ThinkDatabase(db_url)


class MjsThinkModel(ThinkModel):
    database = db


class DeviceThinkModel(MjsThinkModel):
    tn = 'device'


if __name__ == '__main__':
    # 查询最后一条记录的id
    # rows = DeviceThinkModel.select(["id"], where='id is not null order by id desc', limit=1)
    # row = None
    # for r in rows:
    #     row = r.id
    # did = row
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(now)
    ip1 = 0
    ip2 = 0
    ip3 = 0
    ip4 = 0
    idata = list()
    print('正在插入资产数据中')
    for i in range(2000):
        if ip1 < 254 and ip4 != 254:
            ip1 += 1
        elif ip1 >= 254 and ip2 < 254 and ip4 != 254:
            ip2 += 1
        elif ip2 >= 254 and ip3 < 254 and ip4 != 254:
            ip3 += 1
        elif ip3 >= 254 and ip4 < 254:
            ip4 += 1
        elif ip4 >= 254 and ip3 > 0:
            ip3 = ip3 - 1
        elif ip3 <= 0 and ip2 > 0:
            ip2 = ip2 - 1
        elif ip2 <= 0 and ip1 > 0:
            ip1 = ip1 - 1
        else:
            ip4 = ip4 - 1
        # did += 1
        data = {
            "devName": f"testDev{i}",
            "nodeId": 0,
            "ip": f"{ip4}.{ip3}.{ip2}.{ip1}",
            "typeId": 1,
            "systemId": 1,
            "model": '',
            "online": 1,
            "remark": '',
            "createTime": now,
            "updateTime": now
        }
        idata.append(data)
        if len(idata) == 100:
            DeviceThinkModel.insert(idata)
            idata = list()
    print('脚本执行完成！')
    os.system('pause')
