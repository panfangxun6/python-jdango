import numpy as np
import pandas as pd

import jieba
import jieba.analyse



txt = open(r"/Users/zuchebao/Downloads/全职高手【完本】.txt", "r", encoding='utf-8').read()
def getKeyWord(txt):
        keywords_textrank = jieba.analyse.extract_tags(txt)

        return(keywords_textrank)

print(getKeyWord(txt))

# words = jieba.lcut(txt)     # 使用精确模式对文本进行分词
# counts = {}     # 通过键值对的形式存储词语及其出现的次数
#
# for word in words:
#     if  len(word) == 1:    # 单个词语不计算在内
#         continue
#     else:
#         counts[word] = counts.get(word, 0) + 1    # 遍历所有词语，每出现一次其对应的值加 1
#
# items = list(counts.items())  #将键值对转换成列表
# items.sort(key=lambda x: x[1], reverse=True)    # 根据词语出现的次数进行从大到小排序
#
# for i in range(15):
#     word, count = items[i]
#