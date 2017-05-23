#coding=utf-8

import jieba
import jieba.posseg as pseg
jieba.load_userdict("jieba/mydict.txt")

# seg_list = jieba.cut("我来到北京清华大学", cut_all=True)
# print("Full Mode: " + "/ ".join(seg_list))  # 全模式
#
# seg_list = jieba.cut("我来到北京清华大学", cut_all=False)
# print("Default Mode: " + "/ ".join(seg_list))  # 精确模式
# #
# seg_list = jieba.cut("他来到了网易杭研大厦", cut_all=False)
# print("Default Mode: " + "/ ".join(seg_list))  # 精确模式

seg_list = jieba.cut("『【巴厘岛BALI】去丹麦吃生蚝吧Happy Birthdaz 价值1元（龙目岛&蓝梦岛&吉利岛）超强完整攻略 - 印度尼西亚/东帝汶 - 论坛 - 穷游网』网页链接​")  # 默认是精确模式
print(" ".join(seg_list))
#
# seg_list = jieba.cut_for_search("小明硕士毕业于中国科学院计算所，后在日本京都大学深造")  # 搜索引擎模式
# print(", ".join(seg_list))
