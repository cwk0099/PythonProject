import json
import os
import socket
from socket import error
from threading import Thread

switch = ''
stop = True

def tcp(datasocket, ne_ip):
    datasocket.settimeout(3.0)
    while True:
        try:
            while True:
                try:
                    msg = datasocket.recv(8)
                except error:
                    # print(f'switch:{switch}')
                    if switch == 'q':
                        datasocket, ne_ip = switch_ip(datasocket, ne_ip)
                        datasocket.settimeout(3.0)
                    continue
                    # 心跳检测
                    # response = os.popen("ping -n 1 " + ne_ip).read()
                    # if "已接收 = 1" in response:
                    #     continue
                    # else:
                    #     datasocket, ne_ip = switch_ip(datasocket, ne_ip)
                    #     continue
                break
            ms = bytesToHexString(msg)
            print(f'报文头为：{ms}')
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
            lenth = int.from_bytes(msg[4:8], byteorder='big') - 8
            print(f'json长度为：{lenth}')
            json_b = datasocket.recv(lenth)
            print(json_b)
            try:
                json_str = json_b.decode()
            except UnicodeDecodeError:
                print('接收json出错，请重新连接')
                return
        except (ConnectionAbortedError, OSError, ConnectionError,
                ConnectionResetError, ConnectionRefusedError, IndexError) as e:
            print(e)
            datasocket.close()
            return
        mjs_json = json.loads(json_str)
        print('发送的json为：')
        print(json.dumps(mjs_json, sort_keys=False, indent=3, separators=(',', ':'), ensure_ascii=False))


def switch_ip(datasocket1, nee_ip):
    global switch
    switch = 'w'
    print('正在切换连接')
    datasocket1.close()
    if nee_ip == '192.168.0.241':
        nee_ip = '192.168.0.242'
    elif nee_ip == '192.168.0.242':
        nee_ip = '192.168.0.241'
    print('正在等待连接...')
    while True:
        datasocket1, addr2 = tps_server.accept()
        ladd2 = list(addr2)
        print(f'{addr2[0]}已连接')
        if ladd2[0] == nee_ip:
            print(f'{nee_ip}已连接！')
            break
    return datasocket1, nee_ip


def validate_ip(ipaddr):
    ips = ipaddr.split('.')
    if len(ips) != 4:
        return False
    for ip in ips:
        try:
            int_ip = int(ip)
        except ValueError:
            return False
        if 0 > int_ip or int_ip >= 255:
            return False
    return True


def bytesToHexString(data):
    temp = []
    for i in data:
        temp.append('0x%02X' % i)
    return temp

def checkSwitch():
    global switch, stop
    while True:
        switch = input('输入q切换连接:')
        if not stop:
            return



if __name__ == '__main__':
    tps_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    IP = ''
    while True:
        try:
            port = int(input('请输入本地监听端口：'))
            tps_server.bind((IP, port))
        except (OSError, ValueError):
            print("地址无效或者端口被占用，请重新输入")
            continue
        break
    tps_server.listen(10)
    buff = 1024
    while True:
        need_ip = input('请输入要连接的堡垒机ip：')
        if validate_ip(need_ip):
            nip = None
            print('正在等待连接...')
            while True:
                dataSocket, addr = tps_server.accept()
                ladd = list(addr)
                nip = ladd[0]
                if nip != need_ip:
                    print(f'{addr[0]}请求连接')
                    continue
                print(f'{addr[0]}已连接！')
                break
            break
        else:
            print('非法ip，请重新输入！')
    thread_tcp = Thread(target=tcp, args=(dataSocket, need_ip))
    thread_check = Thread(target=checkSwitch, args=())
    thread_tcp.start()
    thread_check.start()
    thread_tcp.join()
    stop = False
    os.system('pause')
