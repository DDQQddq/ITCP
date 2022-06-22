# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class LearnScItem(scrapy.Item):
    # define the fields for your item here like:
    # 文本内容
    text = scrapy.Field()
    # 作者信息
    author = scrapy.Field()
    # 标签
    tags = scrapy.Field()
