import csv

class ReadCsv:
    def __init__(self, path, encoding=None):
        self.__path = path
        self.__encoding = encoding
        self.__csvfile = open(self.__path, 'r+', encoding=self.__encoding)

    # 读取每行,返回一个带元组的列表
    def readline(self):
        data = list()
        csv_reader = csv.reader(self.__csvfile)
        for line in csv_reader:
            line_t = tuple(line)
            data.append(line_t)
        del data[0]
        return data

    # 获取行头，返回一个列表
    def readtitle(self):
        # 通过seek重置文件指针，不然再次读取的内容为空
        self.__csvfile.seek(0, 0)
        csv_reader = csv.DictReader(self.__csvfile)
        title = csv_reader.fieldnames
        str_row = str()
        for index, row in enumerate(title):
            if index + 1 == len(title):
                str_row += row
            else:
                str_row += row + ','
        return str_row

    # 根据标题获取列
    def onerow(self, title):
        self.__csvfile.seek(0, 0)
        csv_reader = csv.DictReader(self.__csvfile)
        one_row = [row[title] for row in csv_reader]
        return one_row

    def closecsv(self):
        self.__csvfile.close()