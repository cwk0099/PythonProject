import socket
import os
import json
from time import sleep
from tps_thread import TpsThread


def print_ip():
    while True:
        print('已连接客户端：', end='')
        if len(ads) == 0:
            print('')
        else:
            print('')
            for index, add in enumerate(ads):
                print(f'{index + 1}:{add}')
        ci = input('请输入要通讯的客户端序号，按回车刷新:')
        if ci == '':
            continue
        else:
            c = int(ci) - 1
            t = TpsThread(target=json_send, args=(socks[c], addrs[c]))
            global t_s
            t_s = t
            t.start()
            break
    return


def connect():
    while True:
        dataSocket, addr = tps_server.accept()
        socks.append(dataSocket)
        addrs.append(addr)
        # t = threading.Thread(target=json_send, args=(dataSocket, addr))
        # th.append(t)
        ad = f'{addr[0]}:{addr[1]}'
        ads.append(ad)


def json_send(d_Socket, adr):
    ts = t_s
    t3 = TpsThread(target=is_connectd, args=(d_Socket, adr, 1024, ts))
    t3.start()
    while True:
        print(f'{adr[0]}:{adr[1]}:')
        target_dir = '..\\data\\'
        fname = []
        fi = 0
        for (dirpath, dirname, filename) in os.walk(target_dir):
            fname += filename
        print(f'1:重新选择客户端')
        for index, fn in enumerate(fname):
            fi = index + 2
            if fi % 2 == 0:
                file_name = f'{fi}：{fn}'
                l1 = len(file_name.encode('GBK'))
                le = 60 - l1 + len(file_name)
                print(f'{file_name:<{le}}\t', end='')
            else:
                print(f'{fi}：{fn}')
        if fi % 2 == 0:
            print('')
        fid = int(input('请输入你需要发送的文件序号：'))
        if fid == 1:
            break
        fpath = os.path.join(target_dir, fname[fid - 2])
        try:
            with open(fpath, 'r', encoding='utf8') as fp:
                data = json.load(fp)
            j_data = json.dumps(data, ensure_ascii=False).encode('utf-8')
            a = '<?begn?>'.encode('utf-8')
            b = int(1).to_bytes(length=2, byteorder='big', signed=True)
            b1 = int(0).to_bytes(length=2, byteorder='big', signed=True)
            c = (len(j_data) + 64).to_bytes(length=4, byteorder='big', signed=True)
            c1 = int(0).to_bytes(length=64, byteorder='big', signed=True)
            d = '<?endn?>'.encode('utf-8')
            msg = a + b + b1 + c + j_data + c1 + d
            if not ts.check():
                print('连接中断，请重新选择客户端!')
                break
            d_Socket.send(msg)
        except json.decoder.JSONDecodeError as e:
            print('json解析失败，请检查json格式并重新选择文件发送，失败原因如下')
            print(e)
            continue
        print('发送成功')
        sleep(3)
        continue
    t1 = TpsThread(target=print_ip)
    t1.start()
    return


def is_connectd(da_Socket, addr, Bufflen, ts):
    while True:
        recved = da_Socket.recv(Bufflen)
        if not recved:
            bro_ip = f'{addr[0]}:{addr[1]}'
            print(f'{bro_ip}的连接已中断')
            for index in range(len(ads)):
                if ads[index] == bro_ip:
                    del (ads[index])
            ts.stop()
            break
    return


if __name__ == '__main__':
    tps_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    IP = ''
    port = 8802
    tps_server.bind((IP, port))
    tps_server.listen()
    ads = []
    socks = []
    addrs = []
    print(f'模拟探针程序启动成功')
    t1 = TpsThread(target=print_ip)
    t2 = TpsThread(target=connect)
    t1.start()
    t2.start()
