import pandas as pd
from wordcloud import WordCloud
import jieba

font = 'font.TTF'

# 数据文件读取
quotes = pd.read_csv('quotes.csv')
# 获取目标
tags = quotes['tags']
quotes = quotes['text']

tag = ''
for i in tags:
    tag = f"{tag} {i}"
quote = ''
for i in quotes:
    quote = f"{quote} {i}"
# 词云绘制
word_list = jieba.cut(tag, cut_all=False)
word = " ".join(word_list)
cloud = WordCloud(scale=4, font_path=font)
cloud.generate(word)
cloud.to_file('tags.png')
word_list = jieba.cut(quote, cut_all=False)
word = " ".join(word_list)
cloud = WordCloud(scale=4, font_path=font)
cloud.generate(word)
cloud.to_file('quotes.png')
