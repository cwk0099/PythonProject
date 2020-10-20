from pythink import ThinkDatabase, ThinkModel
import pymysql
pymysql.install_as_MySQLdb()

db_url = 'mysql://chase:Jumho_123@192.168.0.237:9902/tps300ol'
db = ThinkDatabase(db_url)

class BaseDbModel(ThinkModel):
    database = db

class DeviceDbModel(BaseDbModel):
    table_name = 'device'


if __name__ == '__main__':
    rows = DeviceDbModel.select(['duid'], where='ip="192.168.0.253" and devName="华三交换机"',)
    for row in rows:
        print(row.duid)
    # db = pymysql.connect(host='192.168.0.237', user='root', password='password_Welcome%123', port=9902,
    # database='tps300ol')
    # cur = db.cursor() row = cur.execute('select duid from device where ip="192.168.0.253" and
    # devName="华三交换机" ')
    # print(row)