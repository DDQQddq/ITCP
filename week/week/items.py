# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class WeekItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    first = scrapy.Field()
    second = scrapy.Field()
    area = scrapy.Field()
    floor = scrapy.Field()
    name = scrapy.Field()
    price = scrapy.Field()
    house_name = scrapy.Field()
    env = scrapy.Field()
    location = scrapy.Field()
    pass
