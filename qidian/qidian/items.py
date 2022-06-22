# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class QidianItem(scrapy.Item):
    # define the fields for your item here like:
    # 所爬取的目标元素
    title = scrapy.Field()
    author = scrapy.Field()
    type_1 = scrapy.Field()
    type_2 = scrapy.Field()
    cate = scrapy.Field()
    time = scrapy.Field()
    brief = scrapy.Field()
    pass
