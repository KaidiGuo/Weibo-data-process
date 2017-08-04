#coding=utf-8
import json
from collections import Counter


total_counts = Counter()
sentence='让 不丹 莲 呵 呵 呵'



def wordscounter(text, n):
    wordDict = {}
    wordlist =text.split(" ")
    for word in wordlist:
        if word in wordDict:
            wordDict[word] = wordDict[word] + 1
        else:
            wordDict[word] = 1
    count = Counter(wordDict)
    rank = count.most_common()[:n]
    print json.dumps(count.most_common()[:n], encoding="UTF-8", ensure_ascii=False)
    print type(rank)


wordscounter(sentence, 3)