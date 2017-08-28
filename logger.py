import time
import os


class Logger:
    def __init__(self):
        self.path = os.path.dirname(os.path.abspath(__file__))

    def log_write(self, content):
        filename = 'log-' + time.strftime('%d-%m-%Y') + '.txt'
        file = open(filename, "a")
        file.write('[' + time.strftime("%H:%M:%S") + '] ' + content)
        file.write('\n')
        file.close