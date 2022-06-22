import scrapy
from wind.items import WindItem


class BookSpider(scrapy.Spider):
    name = 'wind'
    allowed_domains = ['www.readnovel.com']
    start_urls = ['https://www.readnovel.com/rank/xyyuepiao?pageNum=1']

    def parse(self, response):
        names = response.xpath("//div[@class='book-mid-info']/h4/a/text()")
        authors = response.xpath("//div[@class='book-mid-info']/p[@class='author']/a[1]/text()")
        types = response.xpath("//div[@class='book-mid-info']/p[@class='author']/a[2]/text()")
        states = response.xpath("//div[@class='book-mid-info']/p[@class='author']/span/text()")
        prices = response.xpath("//div[@class='m-num']/p/span/text()")

        for name, author, type, state, price in zip(names, authors, types, states, prices):
            bot = WindItem()

            bot['name'] = name.get()
            print(bot['name'])

            bot['author'] = author.get()
            print(bot['author'])

            bot['type'] = type.get()
            print(bot['type'])

            bot['state'] = state.get()
            print(bot['state'])

            bot['price'] = price.get()
            print(bot['price'])

            yield bot

            next_page = 'https://www.readnovel.com/rank/xyyuepiao?pageNum=2'
            yield scrapy.Request(next_page, callback=self.parse)
