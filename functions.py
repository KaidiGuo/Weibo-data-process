#coding=utf-8
import os
import time
import re


def puncfilter(line):
    # r1 = u'[a-zA-Z0-9’!"#$%&\'()*+,-./:;<=>?@，。?★、…【】《》？“”‘’！[\\]^_`{|}~]+'
    r1 = u'[’!"#$%&\'()*+,-./:;<=>?@；；：．｜～\≧▽—°❄×🍀🐾🍓🐋▲♥♀☀●巜「」☕／↓→<=>?@⁄•ω★💊🙈☕💰😂·、…★、​…【】《》『』（）？“”‘’！[\\]^_`{|}~]+'
    # r1 = u'[’!"#$%&\'()*+,-—./:;；；：．｜～\≧▽—�✨��°❄▲♥♀☀●巜「」☕／↓→<=>?@，。?⁄•ω★💊🙈☕💰😂·、…【】《》『』（）？“”‘’！[\\]^_`{|}~]+'
    # r1 = u'[’!"#$%&\'()*+,-—./:;；；：．｜～\≧▽—�✨��°❄▲♥♀☀●巜「」☕／↓→<=>?@，。?⁄•ω★💊🙈☕💰😂·、…【】《》『』（）？“”‘’！[\\]^_`{|}~]+'

    line1 = re.sub(r1, '', line)
    line2 = line1.replace('\\', '')
    return line2

# line1= "『【巴厘岛@BALI】\≧Happy Birthdayy（龙目岛&蓝梦岛&吉利岛）超强完整攻略 - 1印度尼西亚/2东帝汶 - 论坛 - 穷游网』网页链接"
# line1="【丹麦生蚝成灾，网友：那都不是事儿】 目前，丹麦被太平洋生蚝这一新物种入侵，对海岸的生态环境造成极大破，科学家和渔民都束手无策。我国网友瞬间正义感爆棚，纷纷支招。（视频来源 网络）"
#
# print puncfilter(line1.decode("utf-8"))
# print puncfilter(line.decode("utf-8"))

# line2 = "哈哈哈哈@丹麦驻华大使馆//@梅原蓉一:我就说嘛//@无奈的订书机:嗯"
p1 = "萌萌哒iPhone 6s灰色"
p2 = '被糖淹沒的Android'
p3 ="iPhone客户端"
p4 =" 三星 Galaxy"

def platformUni(platform):
    if 'iPhone' in platform:
        iphonelist =[ "iPhone 5s", "iPhone 5c", "iPhone 5",  "iPhone 6 Plus", "iPhone 6s Plus", "iPhone 6s","iPhone 6", "iPhone 7 Plus", "iPhone 7","iPhone SE", "iPhone"]
        for phone in iphonelist:
            if phone in platform:
                new = phone
                return new
        # new = "iPhone" + platform.split('iPhone')[1]
    elif 'iOS' in platform:
        new = "iPhone"
        return new
    elif 'Android' in platform:
        new = "Android" + platform.split('Android')[1]
        return new
    elif 'iPad' in platform:
        new = "iPad" + platform.split('iPad')[1]
        return new
    elif '360手机' in platform:
        new = "360手机"
        return new
    elif '魅族' in platform:
        new = "魅族" + platform.split('魅族')[1]
        return new
    elif 'MEIZU' in platform:
        new = "魅族" + platform.split('MEIZU')[1]
        return new
    elif '魅蓝' in platform:
        new = "魅族 魅蓝" + platform.split('魅蓝')[1]
        return new
    elif 'Galaxy' in platform:
        new = "三星 Galaxy" + platform.split('Galaxy')[1]
        return new
    elif 'GALAXY' in platform:
        new = "三星 Galaxy" + platform.split('GALAXY')[1]
        return new
    elif 'Samsung' in platform:
        new = "三星" + platform.split('Samsung')[1]
        return new
    elif '360' in platform:
        new = "360" + platform.split('360')[1]
        return new
    elif '小米' in platform:
        new = "小米" + platform.split('小米')[1]
        return new
    elif '红米' in platform:
        new = "小米 红米" + platform.split('红米')[1]
        return new
    elif 'xiaomi' in platform:
        new = "小米" + platform.split('小米')[1]
        return new
    elif '荣耀' in platform:
        new = "华为荣耀" + platform.split('荣耀')[1]
        return new
    elif 'vivo' in platform:
        new = "vivo" + platform.split('vivo')[1]
        return new
    elif 'HUAWEI' in platform:
        new = "华为" + platform.split('HUAWEI')[1]
        return new
    elif 'OnePlus' in platform:
        new = "一加" + platform.split('OnePlus')[1]
        return new
    elif 'Smartisan' in platform:
        new = "锤子" + platform.split('Smartisan')[1]
        return new
    elif '坚果' in platform:
        new = "锤子 坚果" + platform.split('坚果')[1]
        return new
    elif 'Xperia' in platform:
        new = "索尼 Xperia" + platform.split('Xperia')[1]
        return new
    else:
        return platform

def platformSimp(platform):
    platformlist = ["iPhone", "iPad", "秒拍", "三星", "华为", "小米", "OPPO", "vivo", "魅族","索尼","锤子","一加","Android"]
    thisphone = platform
    for phone in platformlist:
        if phone in platform:
            return phone
    return platform

# print platformUni(p1)
# print platformSimp(p1)
# print platformSimp(p4)


def removepeople(peopleline):
    pattern = peopleline.split("//@")
    outputline = ""
    for name in pattern:
        name = name.split(":")[-1]
        outputline += name
    return outputline

# print str(removepeople(line1)).decode('string_escape')


def removeurl(urlline):
    results = re.compile(r'http://[a-zA-Z0-9.?/&=:]*', re.S)
    dd = results.sub("", urlline)
    return dd



def removeEmoji(text):
    # emoji_pattern  = re.compile(u'[\uD800-\uDBFF][\uDC00-\uDFFF]')
    nomoji = re.compile(u'['
                      u'\U0001F300-\U0001F5FF'
                      u'\U0001F600-\U0001F64F'
                      u'\U0001F680-\U0001F6FF'
                      u'\u2600-\u26FF\u2700-\u27BF]+',
                      re.UNICODE)
    return nomoji.sub(r'', text)  # no emoji




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


def linear_scale(inputmin,inputmax,outputmin,outputmax,item):
    a = float(outputmax-outputmin)/float(inputmax-inputmin)
    b = outputmax - a*inputmax
    output = a*item +b
    return output




