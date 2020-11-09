import socket
import sys
from tps_thread import TpsThread
import json
import time

def tcp(datasocket):
    while True:
        try:
            msg = datasocket.recv(8)
            b = b'\xc2'
            if msg[0] == ord('\xa0'):
                print('日志标识为:0xa0')
            elif msg[0] != ord('\xa0'):
                print(f"日志标识错误，为:{chr(msg[0]).encode().replace(b, b'')}")
            if msg[1] == ord('\x00'):
                print('保留字段为:0x00')
            elif msg[1] != ord('\x00'):
                print(f"保留字段错误,为:{chr(msg[1]).encode().replace(b, b'')}")
            if msg[2] == ord('\x26'):
                print('日志类型编码为:0x26，日志类型为:告警日志')
                if msg[3] == ord('\x01'):
                    print('日志子类型编码为:0x01，日志子类型为:高风险操作日志')
                elif msg[3] == ord('\x02'):
                    print('日志子类型编码为:0x02，日志子类型为:堡垒机多点登陆日志')
                elif msg[3] == ord('\x03'):
                    print('日志子类型编码为:0x03，日志子类型为:备机心跳丢失日志')
                else:
                    print(f"日志子类型编码有误，为:{chr(msg[3]).encode().replace(b, b'')}")
            elif msg[2] == ord('\x27'):
                print('日志类型编码为:0x27，日志类型为:会话日志')
                if msg[3] == ord('\x01'):
                    print('日志子类型编码为:0x01，日志子类型为:会话开始日志')
                elif msg[3] == ord('\x02'):
                    print('日志子类型编码为:0x02，日志子类型为:会话结束日志')
                else:
                    print(f"日志子类型编码有误，为:{chr(msg[3]).encode().replace(b, b'')}")
            elif msg[2] == ord('\x28'):
                print('日志类型编码为:0x28，日志类型为:安全运行日志')
                if msg[3] == ord('\x11'):
                    print('日志子类型编码为:0x11，日志子类型为:主备机切换日志')
                elif msg[3] == ord('\x12'):
                    print('日志子类型编码为:0x12，日志子类型为:cpu使用率日志')
                elif msg[3] == ord('\x13'):
                    print('日志子类型编码为:0x13，日志子类型为:内存使用率日志')
                else:
                    print(f"日志子类型编码有误，为：{chr(msg[3]).encode().replace(b, b'')}")
            else:
                print(f"日志子类型编码有误，为：{chr(msg[2]).encode().replace(b, b'')}")
            lenth = int.from_bytes(msg[4:8], byteorder='big')
            print(f'json长度为：{lenth}')
            json_b = datasocket.recv(lenth)
            print(json_b)
            try:
                json_str = json_b.decode()
            except UnicodeDecodeError:
                print('接收出错，请重新连接')
                dataSocket.close()
                ne_ip = input('请输入要连接的ip：')
                n_ip = ''
                print('正在等待连接...')
                while n_ip != ne_ip:
                    dataSocket, addr = tps_server.accept()
                    ladd = list(addr)
                    n_ip = ladd[0]
                    print(n_ip)
                    print(f'{addr[0]}已连接')
                continue
            mjs_json = json.loads(json_str)
            print('发送的json为：')
            print(mjs_json)
        except (ConnectionAbortedError, OSError):
            break


if __name__ == '__main__':
    tps_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    IP = ''
    k = 0
    while k == 0:
        port = int(input('请输入监听端口：'))
        try:
            tps_server.bind((IP, port))
        except OSError:
            print("地址无效或者端口被占用，请重新选择")
            continue
        k = 1
    tps_server.listen(10)
    buff = 1024
    need_ip = input('请输入要连接的ip：')
    nip = ''
    print('正在等待连接...')
    while nip != need_ip:
        dataSocket, addr = tps_server.accept()
        ladd = list(addr)
        nip = ladd[0]
        print(nip)
        print(f'{addr[0]}已连接')
    thread_tcp = TpsThread(target=tcp, args=(dataSocket,))
    thread_tcp.start()
    while True:
        k = input('连接成功，请输入n退出：\n')
        if k == 'n':
            dataSocket.close()
            break
    time.sleep(1)
    sys.exit(0)
