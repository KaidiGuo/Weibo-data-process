#coding=utf-8

from functions import *

date = "04-18"
datapath = "../WBOutputdata/"
list_dirs = os.walk(datapath)
for root, dirs, files in list_dirs:
    for thisdir in dirs:
        countryName = thisdir.decode("gbk").encode("UTF-8")
        filename = datapath + countryName.decode("UTF-8") +"/" + countryName.decode("UTF-8") + date + ".txt"
        print filename
        if os.path.exists(filename):
            print "find one!"
            os.remove(filename)
            print "remove one: ", filename
