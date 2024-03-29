#!/usr/bin/python
# -*- coding: UTF-8 -*-
import json
import MySQLdb
from collections import Counter
import datetime
import conter
import functions

wbdb = MySQLdb.connect("localhost","root","WIND327976003", "test", charset='utf8' )
cursor = wbdb.cursor()

# SQL 查询语句
# SQL 查询语句
# sql = "SELECT text FROM wbdata WHERE keyword = '德国'"
# sql = "select * from tbl_user"

# sql_total_country_rank = "select keyword,count(*) from wbdata group by keyword order by count(*) desc;"
# sql_total_platform_rank = "select platform2,count(*) from wbdata group by platform2 order by count(*) desc limit 5;"
# sql_total_gender_rank = "select gender,count(*) from wbdata group by gender;"
# sql_gender_rank_german = "SELECT gender,count(*) FROM wbdata WHERE keyword = '德国' group by gender;"
# sql_max_follower = "select * from wbdata where follower in (select max(follower) from wbdata);"
sql_select_time = "select creat_at, count(*) from wbdata where creat_at > '2017-04-26 00:00:00' and creat_at <'2017-04-27 00:00:00';"


starttime = datetime.datetime.now()

def structure_result(myresult):
    datalist = []
    textlist = []
    outputdata =[]
    for something in myresult:
        datalist.append(int(something[1]))
        textlist.append(str(something[0].encode("utf-8")))
    outputdata.append(datalist)
    outputdata.append(textlist)
    return outputdata

# sql_total_gender_rank = "select gender,count(*) from wbdata group by gender;"
sql_tags_all = "select tags from wbdata where keyword = '德国' ;"
cursor.execute(sql_tags_all)
sql_tags_all_result = cursor.fetchall()

def turn_tags_tostring(sql_result):
    outputstring = ""
    for row in sql_result:
        longlist = row[0].split(" ")
        for i in range(len(longlist)-1):
            outputstring = outputstring + longlist[i+1] +","
    return outputstring


def wordscounter(text, n):
    wordDict = {}
    wordlist =text.split(",")
    for word in wordlist:
        if word in wordDict:
            wordDict[word] = wordDict[word] + 1
        else:
            wordDict[word] = 1

    removelist = ["秒拍", "视频", "网页", "分享", "全文", "链接", "00", "01","1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11",
                  "12", "13", "14", "15","16","17","18","19","20", "21", "22", "23", "24", "25", "26", "27", "28","29", "30","31","100", "20",  "40", "50",
                  "60", "70", "80","90"]

    for word in removelist:
        try:
            del wordDict[word.decode("utf-8")]
            # print "delet", word
        except Exception:
            pass
    count = Counter(wordDict)
    rank = count.most_common()[:n]
    countmax = rank[1][1]
    countmin = rank[-1][1]
    # print countmax
    # print countmin
    diclist = []
    for item in rank:
        rankdic = {}
        rankdic['text'] = item[0]
        rankdic['size'] = functions.linear_scale(countmin,countmax,10,110,item[1])
        diclist.append(rankdic)
    diclist[0]['size'] = 120
    print json.dumps(diclist, encoding="UTF-8", ensure_ascii=False)


def smallcounter(text, n):
    wordDict = {}
    wordlist =text.split(",")
    for word in wordlist:
        if word in wordDict:
            wordDict[word] = wordDict[word] + 1
        else:
            wordDict[word] = 1

    removelist = ["秒拍", "视频", "网页", "分享", "全文", "链接", "00", "01","1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11",
                  "12", "13", "14", "15","16","17","18","19","20", "21", "22", "23", "24", "25", "26", "27", "28","29", "30","31","100", "20",  "40", "50",
                  "60", "70", "80","90"]

    for word in removelist:
        try:
            del wordDict[word.decode("utf-8")]
            # print "delet", word
        except Exception:
            pass
    count = Counter(wordDict)
    rank = count.most_common()[:n]

    print json.dumps(rank, encoding="UTF-8", ensure_ascii=False)

print "try!"
# print
# wordscounter(turn_tags_tostring(sql_tags_all_result),120)

smallcounter(turn_tags_tostring(sql_tags_all_result),120)

def count_word(longstring):
    result = {}
    for word in longstring.split():
        if word not in result:
            result[word] = 0
        result[word] += 1
    return result



def collection_count(input, n):

    wordDict = {}
    wordlist = input.split(" ")
    for word in wordlist:
        if word in wordDict:
            wordDict[word] = wordDict[word] + 1
        else:
            wordDict[word] = 1
    for item in bag:
        try:
            del wordDict[item.decode("utf-8")]
            print "Delet:", item
        except:
            print "did not find:",item
            pass

    count = Counter(wordDict)
    print type(count)
    rank = count.most_common()[:n]
    print json.dumps(count.most_common()[:n], encoding="UTF-8", ensure_ascii=False)


# print text
# print collection_count(text, 10)
endtime = datetime.datetime.now()
print "Time: ", endtime-starttime
# print "row: ", rowcount
