import os

from read_configure import ReadConfigure
import requests


rc = ReadConfigure()
class InterfaceTest:
    global rc

    def __init__(self):
        self.__protocol = rc.getmethod('protocol')
        self.__method = rc.getmethod('method')
        self.__url = rc.geturl('url')
        pidict = rc.getparameters_int()
        self.__pdict = rc.getparameters_string()
        self.__pdict.update(pidict)

    # 发送http请求，返回
    def sendrequest(self):
        method = self.__method
        if method == 'get':
            res = requests.get(url=self.__url, params=self.__pdict)
            print(res)
            print(res.text)
            print(type(res.text))


if __name__ == '__main__':
    it = InterfaceTest()
    it.sendrequest()