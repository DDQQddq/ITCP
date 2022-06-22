import scrapy
from suki.items import SukiItem


class PopularSpider(scrapy.Spider):
    name = 'popular'
    allowed_domains = ['www.bilibili.com']
    start_urls = ['http://www.bilibili.com/v/popular/all']

    def parse(self, response):
        titles = response.xpath("//div[@class='video-card__info']/p/text()")
        up_name = response.xpath("//div/span[@class='up-name']/text()")
        view_num = response.xpath("//div/p[@class='video-stat']/span[1]/text()")  # strip()
        bullet_chat = response.xpath("//div/p[@class='video-stat']/span[2]/text()")  # strip()

        for title, up, view, bullet in zip(titles, up_name, view_num, bullet_chat):
            bot = SukiItem()

            ti = title.getall()
            print(ti)
            bot['title'] = ti

            up_na = up.get()
            print(up_na)
            bot['up'] = up_na

            vi = view.get().strip()
            bot['view'] = vi

            chat = bullet.get().strip()
            bot['bullet'] = chat

            yield bot
