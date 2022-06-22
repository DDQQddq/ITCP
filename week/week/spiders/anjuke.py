import scrapy
from week.items import WeekItem


class AnjukeSpider(scrapy.Spider):
    name = 'anjuke'
    allowed_domains = ['xa.zu.anjuke.com']
    start_urls = ['https://xa.zu.anjuke.com/fangyuan/gaoxinxa/']

    next_page = ''

    def parse(self, response):

        titles = response.xpath("//div[@class='zu-info']/h3/a/b/text()")
        infos = response.xpath("//div[@class='zu-info']/p[@class='details-item tag']")
        prices = response.xpath("//div[@class='zu-side']/p/strong/b/text()")
        xiaoqumingchengs = response.xpath("//div[@class='zu-info']/address/a/text()")
        addresses = response.xpath("//div[@class='zu-info']/address/text()[2]")
        envs = response.xpath("//div[@class='zu-info']/p[@class='details-item bot-tag']")

        for title, info, price, xiaoqu, addr, env in zip(titles, infos, prices, xiaoqumingchengs, addresses, envs):
            zfitem = WeekItem()
            zfitem['title'] = title.get()

            shi = info.xpath("b[1]/text()").get()
            zfitem['first'] = shi  # 将抓取的数据传递给实体属性准备存储

            # 获取厅的信息
            ting = info.xpath("b[2]/text()").get()
            zfitem['second'] = ting
            # 获取面积的信息
            mianji = info.xpath("b[3]/text()").get()
            zfitem['area'] = mianji  # 将抓取的数据传递给实体属性准备存储

            # 获取楼层信息
            louceng = info.xpath("./text()[5]").get()
            zfitem['floor'] = louceng  # 将抓取的数据传递给实体属性准备存储

            # 获取价格
            jiage = price.get()
            zfitem['price'] = jiage  # 将抓取的数据传递给实体属性准备存储

            # 获取小区名称
            xqname = xiaoqu.get()
            zfitem['name'] = xqname  # 将抓取的数据传递给实体属性准备存储

            # 获取地址的值
            address = addr.get().strip()
            #print(address)
            zfitem['location'] = address  # 将抓取的数据传递给实体属性准备存储

            # 获取环境
            huanjing = env.xpath('span/text()').getall()
            zfitem['env'] = huanjing  # 将抓取的数据传递给实体属性准备存储
            yield zfitem

        for i in range(2, 6):
            next_page = 'https://xa.zu.anjuke.com/fangyuan/gaoxinxa/p'+str(i)
            print(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
