#coding=utf-8

import jieba
import jieba.posseg as pseg
import jieba.analyse

jieba.load_userdict("jieba/mydict.txt")

# seg_list = jieba.cut("我来到北京清华大学", cut_all=True)
# print("Full Mode: " + "/ ".join(seg_list))  # 全模式
#
# seg_list = jieba.cut("我来到北京清华大学", cut_all=False)
# print("Default Mode: " + "/ ".join(seg_list))  # 精确模式
# #
# seg_list = jieba.cut("他来到了网易杭研大厦", cut_all=False)
# print("Default Mode: " + "/ ".join(seg_list))  # 精确模式

#words = pseg.cut("我爱北京天安门")
#for word, flag in words:
#   print('%s %s' % (word, flag))
#
# seg_list = jieba.cut_for_search("小明硕士毕业于中国科学院计算所，后在日本京都大学深造")  # 搜索引擎模式
## print(", ".join(seg_list))

testroll = ["想起来新互关了几个可爱的姑娘所以不好骂人太难听。但是真的对贵游戏没话讲[ok]合作跨区的野鸡滚回中国区站好你的街ok？可以说是十分好笑了跨区合作还谩骂针对留学生说留学生卖国贼的野鸡怎么还不立即去世这个游戏从最开始玩到现在都是小学生和号贩子的天下了贵游戏看不惯早日拉黑我[ok] ​...全文",
            "前年有一段时间北京雾霾特别严重，那时候欧洲这边还报道的比较多。瑞航的marketing出过一个广告创意：欢迎大家前来瑞士逃避雾霾，我们除了可以滑雪还有特别干净的空气。后来这个主意被枪毙了，因为有人评价它对不能出国的中国人不尊敬。这也许是商家的底线吧。 ",
            "说攻击造成核泄漏的某博主是心眼坏了。必须打，打完至少要分中国一个东北出海口吧",
            "『【巴厘岛BALI】Happy Birthdayy（龙目岛&蓝梦岛&吉利岛）超强完整攻略 - 1印度尼西亚/2东帝汶 - 论坛 - 穷游网』网页链接"]

for sentence in testroll:
   print "This: ",sentence
   extract = jieba.analyse.extract_tags(sentence, topK=5, withWeight=True, allowPOS=())
   extractline = ""
   for word in extract:
      print word[0]
      co = word[0]
      extractline = extractline +" "+ co

   print "-------------"
   print extractline
