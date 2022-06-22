# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TopmusicItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    singer = scrapy.Field()
    time = scrapy.Field()
    type_1 = scrapy.Field()
    type_2 = scrapy.Field()
    style = scrapy.Field()
    score = scrapy.Field()
    num = scrapy.Field()
    pass
