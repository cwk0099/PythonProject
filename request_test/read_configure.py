import os
import codecs
import configparser

# 读取configure配置文件的类
class ReadConfigure:
    def __init__(self):
        fd = open("configure.ini", 'r', encoding='UTF-8')
        data = fd.read()
        # 去除BOM头
        if data[:3] == codecs.BOM_UTF8:
            data = data[3:]
            file = open('configure.ini', 'w', encoding='UTF-8')
            file.write(data)
            file.close()
        fd.close()

        self.cf = configparser.ConfigParser()
        self.cf.read('configure.ini', encoding='UTF-8')

    def geturl(self, url):
        return self.cf.get('request', url)

    def getmethod(self, method):
        value = self.cf.get('request', method)
        return value

    # 读取字符串参数，返回一个列表
    def getparameters_string(self):
        plist = self.cf.items('parameters')
        if len(plist) == 0:
            print('字符串参数列表为空')
            return {}
        else:
            pdict = dict()
            for index, l in enumerate(plist):
                i = {plist[index][0]: plist[index][1]}
                pdict.update(i)
            return pdict

    # 读取整形参数，返回一个字典
    def getparameters_int(self):
        pilist = self.cf.items('iparameters')
        if len(pilist) == 0:
            print('整形参数列表为空')
            return {}
        else:
            pidict = dict()
            for index, l in enumerate(pilist):
                pi = int(pilist[index][1])
                i = {pilist[index][0]: pi}
                pidict.update(i)
            return pidict
