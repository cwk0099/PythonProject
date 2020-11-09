from pythink import ThinkModel, ThinkDatabase
import pymysql
pymysql.install_as_MySQLdb()
# from urllib import parse
passwd = 'password_Welcome%123'
# 防止密码含有特殊字符，把密码url编码化，防止报错
# npasswd = parse.quote_plus(passwd)
db_url = f'mysql://root:{passwd}@192.168.0.237:9902/tps300ol'

db = ThinkDatabase(db_url)

class Tps300olThinkModel(ThinkModel):
    database = db

class DeviceThinkModel(Tps300olThinkModel):
    tn = 'device'


if __name__ == '__main__':
    # 查询数量
    print(DeviceThinkModel.count())
    # 查询记录，修改了*的内容
    rows = DeviceThinkModel.select(["*"], where='devName="华三交换机" and ip="192.168.0.253"')
    for row in rows:
        print(row.duid)