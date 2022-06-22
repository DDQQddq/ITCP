# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TopbookItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    author = scrapy.Field()
    press = scrapy.Field()
    time = scrapy.Field()
    price = scrapy.Field()
    score = scrapy.Field()
    comment = scrapy.Field()
    pass
