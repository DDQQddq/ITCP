import scrapy
from learn_sc.items import LearnScItem


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        # 爬取目标xpath路径
        texts = response.xpath("//div[@class='quote']/span[1]/text()")
        authors = response.xpath("//div[@class='quote']/span/small/text()")
        tags = response.xpath("//div[@class='quote']/div[@class='tags']/a/text()")

        bot = LearnScItem()
        for text, author, tag in zip(texts, authors, tags):
            # 文本内容获取
            te = text.getall()
            # 控制台输出
            print(te)
            bot['text'] = te

            # 作者信息获取
            au = author.get()
            # 控制台输出
            print(au)
            bot['author'] = au

            # 标签获取
            ta = tag.getall()
            # 控制台输出
            print(ta)
            bot['tags'] = ta

            yield bot

            # 多页爬取（共十页100条数据）
            for i in range(2, 11):
                # 使用format函数组合链接
                next_page = f"http://quotes.toscrape.com/page/{i}/"
                yield scrapy.Request(next_page, callback=self.parse)
