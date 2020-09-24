import threading

class TpsThread(threading.Thread):
    def __init__(self, *args, **kwargs):
        super(TpsThread, self).__init__(*args, **kwargs)
        self.__running = True

    def stop(self):
        self.__running = False

    def check(self):
        return self.__running



