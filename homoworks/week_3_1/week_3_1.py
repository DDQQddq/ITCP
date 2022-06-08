# author: Elf Dobby
# Github: https://github.com/DDQQddq/ITCP

import jieba
from wordcloud import WordCloud

file_name = 'drama.txt'
stop = 'stop_words.txt'
font = 'font.TTF'

file = open(file_name, encoding="utf-8")
result = file.read()
file.close()

word_list = jieba.cut(result, cut_all=False)
word = " ".join(word_list)
cloud = WordCloud(scale=3, stopwords=stop, font_path=font)
cloud.generate(word)
cloud.to_file('pic.png')
