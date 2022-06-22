import scrapy
from topbook.items import TopbookItem


class BookSpider(scrapy.Spider):
    name = 'book'
    allowed_domains = ['book.douban.com']
    start_urls = ['http://book.douban.com/top250?start=0']

    def parse(self, response):

        names = response.xpath("//tr/td/div[@class='pl2']/a/@title")
        infos = response.xpath("//p[@class='pl']/text()")
        scores = response.xpath("//div[@class='star clearfix']/span[2]/text()")
        comments = response.xpath("//p[@class='quote']/span/text()")

        bot = TopbookItem()
        for name, info, score, comment in zip(names, infos, scores, comments):
            bot['name'] = name.get().replace(" ", "").strip()
            print(bot['name'])

            info = info.get().split('/')
            print(info)
            if len(info) == 5:
                bot['author'] = f"{info[0].split()}/{info[1].split()}"
                print(bot['author'])
            else:
                bot['author'] = info[0].split()
                print(bot['author'])

            bot['press'] = info[-3]
            print(bot['press'])

            bot['time'] = info[-2]
            print(bot['time'])

            bot['price'] = info[-1]
            print(bot['price'])

            bot['score'] = score.get()
            print(bot['score'])

            bot['comment'] = comment.get()
            print(bot['comment'])

            yield bot

            for i in range(25, 301, 25):
                next_page = 'https://book.douban.com/top250?start=' + str(i)
                # print(next_page)
                yield scrapy.Request(next_page, callback=self.parse)
