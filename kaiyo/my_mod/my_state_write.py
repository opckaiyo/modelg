# coding:utf8
from datetime import datetime


def state_write(state):
    file = open('/kaiyo/log/state_log.txt', 'a')
    file.writelines(str(state) + " : " + str(datetime.now()) + "\n")
    file.close()

if __name__ == '__main__':
    state_write("浮上")
