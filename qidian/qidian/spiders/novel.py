import scrapy
from qidian.items import QidianItem


class NovelSpider(scrapy.Spider):
    name = 'novel'
    allowed_domains = ['www.qidian.com']
    start_urls = ['https://www.qidian.com/rank/yuepiao/year2022-month06/']

    def parse(self, response):
        # 获取各个元素的xpath值
        titles = response.xpath("//div[@class='book-mid-info']/h2/a/text()")
        authors = response.xpath("//div[@class='book-mid-info']/p[@class='author']/a[@class='name']/text()")
        type_1s = response.xpath("//div[@class='book-mid-info']/p[@class='author']/a[2]/text()")
        type_2s = response.xpath("//div[@class='book-mid-info']/p[@class='author']/a[3]/text()")
        cates = response.xpath("//div[@class='book-mid-info']/p[@class='author']/span/text()")
        times = response.xpath("//div[@class='book-mid-info']/p[@class='update']/span/text()")
        briefs = response.xpath("//div[@class='book-mid-info']/p[@class='intro']/text()")

        bot = QidianItem()

        for title, author, type_1, type_2, cate, time, brief in zip(titles, authors, type_1s, type_2s, cates, times, briefs):

            # 获取标题值
            bot['title'] = title.get()
            # 控制台输出
            print(title.get())

            # 获取作者信息
            bot['author'] = author.get()
            # 控制台输出
            print(author.get())

            # 获取第一种类型的值
            bot['type_1'] = type_1.get()
            # 控制台输出
            print(type_1.get())

            # 获取第二种分类的值
            bot['type_2'] = type_2.get()
            # 控制台输出
            print(type_2.get())

            # 获取第三种分类的值
            bot['cate'] = cate.get()
            # 控制台输出
            print(cate.get())

            # 获取最近的更新时间
            bot['time'] = time.get()
            # 控制台输出
            print(time.get())

            # 获取小说简介
            bot['brief'] = brief.get()
            # 控制台输出
            print(brief.get())

            yield bot

        # 多页爬取（共5页）
        for i in range(2, 6):
            next_page = f"https://www.qidian.com/rank/yuepiao/year2022-month06-page{i}/"
            yield scrapy.Request(next_page, callback=self.parse)
