# -*- coding: utf-8 -*-
import ast
import time

import sys
sys.path.append("/kaiyo/my_mod")

#------------------------------------------------------------------------------


def get_log():
    vals = {}
    cnt = 0

    # print
    # print "Please file name :",
    # filename = raw_input()
    # file = open('/kaiyo/log/'+filename+'.txt', 'r')

    file_name = "181003_172402.txt"
    file = open('/kaiyo/log/'+file_name, 'r')
    data = file.readline()
    data = ast.literal_eval(data)

    print
    print "File name :", file_name
    print "vals :",
    for key in data.keys():
        print key,

    print
    print "Please value :",
    val = raw_input()


    while True:
        try:
            data = file.readline()
            data = ast.literal_eval(data)

            vals[str(cnt)] = data[val]
            cnt+=1
            # print cnt
            print data[val]
        except Exception as e:
            print "----------------------------"
            print "Number of data :", cnt
            print "MIN :", min(vals.values())
            print "MAX :", max(vals.values())
            print "----------------------------"
            break


if __name__ == '__main__':
    # get_log("roll")
    get_log()
