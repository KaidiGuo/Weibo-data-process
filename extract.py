#coding=utf-8
import os
import json
import codecs
from bs4 import BeautifulSoup
from functions import *
import time
import datetime

dateList = creat_date_list("04",18,24)
startTime = datetime.datetime.now()
wbCount = 0

for date in dateList:
    thisDate = date
    datapath = "../WBTestdata/" + thisDate + "/"
    if os.path.exists(datapath):
        print "got data"
    else:
        print "Did not find this day´s data, next day!!"
        time.sleep(5)
        continue

    list_dirs = os.walk(datapath)
    for root, dirs, files in list_dirs:
        for f in files:
            filename = f.decode("gbk").encode("UTF-8")
            thisfilepath = datapath + filename.decode("UTF-8")
            thisCountry = filename.split(thisDate)[0].decode("UTF-8")
            print "----------------------------------------------------------------------------------------------"
            print "Find one: ", json.dumps(filename, encoding="UTF-8", ensure_ascii=False)
            print "----------------------------------------------------------------------------------------------"
            outputPath = "../WBOutputdata/" + thisCountry + "/"
            if not os.path.exists(outputPath):
                os.mkdir(outputPath)
            outputFile = outputPath + thisCountry + thisDate + ".txt"


            with codecs.open(thisfilepath, "r", "utf-8") as thisfile:
                content = thisfile.read()
                thisdata = json.loads(content)
                #### creat_at
                try:
                    thisRequesttime = thisdata['cardlistInfo']['starttime']
                    for i in range(len(thisdata['cards'][0]['card_group'])):
                        itemID = str(thisdata['cards'][0]['card_group'][i]['mblog']['id'])
                        itemCreat = thisdata['cards'][0]['card_group'][i]['mblog']['created_at']
                        itemRepostCount = str(thisdata['cards'][0]['card_group'][i]['mblog']['reposts_count'])
                        itemSource = thisdata['cards'][0]['card_group'][i]['mblog']['source']
                        itemUser = thisdata['cards'][0]['card_group'][i]['mblog']['user']['screen_name']
                        itemText = thisdata['cards'][0]['card_group'][i]['mblog']['text']
                        soup = BeautifulSoup(itemText, "html.parser")
                        itemTextPretty = ""
                        for string in soup.stripped_strings:
                            itemTextPretty += string
                        print "Text: ", itemTextPretty
                        itemUserID = str(thisdata['cards'][0]['card_group'][i]['mblog']['user']['id'])
                        itemUserGender = str(thisdata['cards'][0]['card_group'][i]['mblog']['user']['gender'])
                        itemUserFollower = str(thisdata['cards'][0]['card_group'][i]['mblog']['user']['followers_count'])
                        #print itemID, "<<>>", itemCreat,"<<>>", thisRequesttime,"<<>>", itemRepostCount, "<<>>", itemSource, "<<>>", itemUser, "<<>>", itemUserID, "<<>>", itemUserFollower, "<<>>", itemUserGender, "<<>>" ,itemText
                        dataLine = str(itemID) + "<<>>" + itemCreat.encode("UTF-8") + "<<>>" + str(thisRequesttime) + "<<>>" + str(itemRepostCount) + "<<>>" + itemSource.encode("UTF-8") + "<<>>" + itemUser.encode("UTF-8") + "<<>>" + str(itemUserID) + "<<>>" + str(itemUserFollower) + "<<>>" + itemUserGender + "<<>>" + itemTextPretty.encode("UTF-8") + '\n'

                        with open(outputFile,"a") as output:
                            output.write(dataLine)
                            wbCount += 1
                except Exception,e:
                    print e
                    print "No data in this file! Next!"
                    time.sleep(3)
                    continue
                # thisendtime = thisdata['cards'][0]['card_group'][-1]['mblog']['created_at']
                # word1 = "今天".decode("UTF-8")
                # word2 = "分钟前".decode("UTF-8")
                # if word1 in thisendtime:
                #     print "find today"

endTime = datetime.datetime.now()

print "Use Time: ", endTime - startTime
print "Process total WB: ", wbCount