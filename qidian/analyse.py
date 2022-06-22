import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import jieba
from wordcloud import WordCloud

# 导入字体文件
font = 'font.TTF'
# csv文件读取
novel = pd.read_csv('novel.csv')
type_2 = novel['type_2']

_type = ''
for i in type_2:
    _type = f"{_type} {i}"
# 词云绘制
word = jieba.lcut(_type, cut_all=False)
word = "".join(word)
cloud = WordCloud(scale=4, font_path=font)
cloud.generate(word)
cloud.to_file('type.png')

# 饼图绘制
type_1 = novel['type_1']
_type_1 = []
for i in type_1:
    _type_1.append(i)
city = _type_1.count('都市')
sci = _type_1.count('科幻')
gods = _type_1.count('仙侠')
mys = _type_1.count('玄幻')
lite = _type_1.count('轻小说')
history = _type_1.count('历史')
hero = _type_1.count('武侠')
game = _type_1.count('游戏')

nums = [city, sci, gods, mys, lite, history, hero, game]
names = ['都市', '科幻', '仙侠', '玄幻', '轻小说', '历史', '武侠', '游戏']

# 设置字体
matplotlib.rcParams['font.sans-serif'] = ['SimHei']

plt.figure(figsize=(8, 8), dpi=100)
plt.pie(nums, labels=names, autopct="%1.2f%%", colors=['b', 'r', 'g', 'y', 'c', 'm', 'y', 'k'])
plt.legend(loc="best")
plt.title('起点中文网月榜各类型小说占比')
# 图片保存至本地
plt.savefig(fname='pie.png')
plt.show()
