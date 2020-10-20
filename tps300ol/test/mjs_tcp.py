import socket
import sys
from tps_thread import TpsThread


def wait_input():
    while True:
        k = input('请输入n退出：\n')
        if k == 'n':
            dataSocket.close()
            break

def tcp(datasocket):
    while True:
        try:
            msg = datasocket.recv(1024)
            print(msg)
        except (ConnectionAbortedError, OSError):
            break


if __name__ == '__main__':
    tps_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    IP = '192.168.0.119'
    port = 8808
    tps_server.bind((IP, port))
    tps_server.listen(15)
    buff = 1024
    need_ip = input('请输入要连接的ip：')
    nip = ''
    while nip != need_ip:
        dataSocket, addr = tps_server.accept()
        ladd = list(addr)
        nip = ladd[0]
        print(nip)
        print(f'{addr[0]}已连接')
    thread = TpsThread(target=wait_input)
    thread.start()
    thread_tcp = TpsThread(target=tcp, args=(dataSocket,))
    thread_tcp.start()
    sys.exit(0)
