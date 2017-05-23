#!/usr/bin/python
# -*- coding: UTF-8 -*-
import MySQLdb

wbdb = MySQLdb.connect("localhost","root","WIND327976003", "Test", charset='utf8' )

cursor = wbdb.cursor()

# SQL 查询语句
sql = "SELECT text, user FROM wbdata WHERE keyword = '不丹' AND gender = 'f'"

# sqlInsert = """CREATE TABLE wbdata (
#     creat_at DATETIME NOT NULL,
#     keyword VARCHAR(30) NOT NULL,
#     wid BIGINT NOT NULL,
#     repost INT NOT NULL,
#     platform CHAR(35) NOT NULL,
#     user CHAR(45) NOT NULL,
#     uid INT NOT NULL,
#     follower INT NOT NULL,
#     gender VARCHAR(2),
#     text VARCHAR(500)
# ) character set = utf8;"""

try:
   # 执行SQL语句
   cursor.execute(sql)

   # 获取所有记录列表
   results = cursor.fetchall()
   for row in results:
       # creattime = row[0]
       # wbid = row[1]
       # repost = row[2]
       # platform = row[3]
       # user = row[4]
       # uid = row[5]
       # follower =row[6]
       # gender = row[7]
       # text = row[8]
       # 打印结果
       text = row[0]
       user = row[1]
       print text, "   ", user
       # print creattime, wbid, user, text, gender
except:
   print "Error: unable to fecth data"
