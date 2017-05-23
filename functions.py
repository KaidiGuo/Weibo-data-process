#coding=utf-8
import os
import time
import re

line = "『【巴厘岛BALI】Happy Birthdayy（龙目岛&蓝梦岛&吉利岛）超强完整攻略 - 1印度尼西亚/2东帝汶 - 论坛 - 穷游网』网页链接"

def puncfilter(line):
    r1 = u'[’!"#$%&\'()*+,-./:;<=>?@，。?；；：．｜～\≧▽—°❄×🍀🐾🍓🐋▲♥♀☀●巜「」☕／↓→<=>?@，。?⁄•ω★💊🙈☕💰😂·、…★、…【】《》『』（）？“”‘’！[\\]^_`{|}~]+'
    # r1 = u'[’!"#$%&\'()*+,-—./:;；；：．｜～\≧▽—�✨��°❄▲♥♀☀●巜「」☕／↓→<=>?@，。?⁄•ω★💊🙈☕💰😂·、…【】《》『』（）？“”‘’！[\\]^_`{|}~]+'

    return re.sub(r1, '', line)

def removeEmoji(text):
    # emoji_pattern  = re.compile(u'[\uD800-\uDBFF][\uDC00-\uDFFF]')
    nomoji = re.compile(u'['
                      u'\U0001F300-\U0001F5FF'
                      u'\U0001F600-\U0001F64F'
                      u'\U0001F680-\U0001F6FF'
                      u'\u2600-\u26FF\u2700-\u27BF]+',
                      re.UNICODE)
    return nomoji.sub(r'', text)  # no emoji

print puncfilter(line.decode("utf-8"))
print removeEmoji("I love")


def get_files_from_folder(rootDir):
    list_dirs = os.walk(rootDir)
    for root, dirs, files in list_dirs:
        for f in files:
            print f
            print "like you:", f
            #print os.path.join(root, f)


get_files_from_folder("../WBTestdata/proxy")

def creat_date_list(month,i,j):
    dates = []
    for n in range(i,j):
        date = month + "-" +str(n).zfill(2)
        dates.append(date)
    return dates

# print creat_date_list("04",01,15)

def process_time(input, starttime):
    if "今天" in input:
        thisStartTime = time.localtime(float(starttime))
        otherStyleTime = str(time.strftime("%Y-%m-%d", thisStartTime))
        creatTime = otherStyleTime + " " + input.split(" ")[1]+":00"
        return creatTime
    elif "分钟前" in input:
        creatTime = 60 * float(input.strip("分钟前"))
        thisStartTime = time.localtime(float(starttime) - creatTime)
        otherStyleTime = str(time.strftime("%Y-%m-%d %H:%M:%S", thisStartTime))
        return otherStyleTime
    else:
        return "2017-"+input+":00"

