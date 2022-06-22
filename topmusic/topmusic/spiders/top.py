import scrapy
from topmusic.items import TopmusicItem


class TopSpider(scrapy.Spider):
    name = 'top'
    allowed_domains = ['music.douban.com']
    start_urls = ['https://music.douban.com/top250?start=0']

    next_page = ''

    def parse(self, response):
        names = response.xpath("//tr/td/div[@class='pl2']/a/text()")
        infos = response.xpath("//div[@class='pl2']/p[1]/text()")
        scores = response.xpath("//div[@class='star clearfix']/span[2]/text()")
        nums = response.xpath("//div[@class='star clearfix']/span[3]/text()")

        for name, info, score, num in zip(names, infos, scores, nums):
            bot = TopmusicItem()

            na = name.get().strip()
            print(na)
            bot['name'] = na

            _in = info.get()
            print(_in)
            singer = _in.split('/')[0].strip()
            # print(singer)
            bot['singer'] = singer

            time = _in.split('/')[1].strip()
            print(time)
            bot['time'] = time

            type_1 = _in.split('/')[2].strip()
            print(type_1)
            bot['type_1'] = type_1

            type_2 = _in.split('/')[3].strip()
            print(type_2)
            bot['type_2'] = type_2

            try:
                style = _in.split('/')[4].strip()
                print(style)
                bot['style'] = style
            except IndexError:
                style = ''
                print(style)
                bot['style'] = style

            score = scores.get()
            print(score)
            # print(score)
            bot['score'] = score

            num = nums.get().strip().replace(' ', '').replace('人评价', '').replace('(', '').replace(')', '').strip()
            print(num)
            bot['num'] = num

            yield bot

        for i in range(25, 226, 25):
            next_page = 'https://music.douban.com/top250?start=' + str(i)
            # print(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
