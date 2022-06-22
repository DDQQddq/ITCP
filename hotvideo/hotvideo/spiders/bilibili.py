import scrapy
from hotvideo.items import HotvideoItem


class BilibiliSpider(scrapy.Spider):
    name = 'bilibili'
    allowed_domains = ['www.bilibili.com']
    start_urls = ['bilibili.com/v/popular/all']

    def parse(self, response):
        titles = response.xpath("//div[@class='video-card__info']/p/text()")
        up_name = response.xpath("//div/span[@class='up-name']")
        view_num = response.xpath("//div/p[@class='video-stat']/span[1]/text()")  # strip()
        bullet_chat = response.xpath("//div/p[@class='video-stat']/span[2]/text()")  # strip()

        for title, up, view, bullet in zip(titles, up_name, view_num, bullet_chat):
            bot = HotvideoItem()

            ti = title.get()
            print(ti)
            bot['title'] = ti

            up_na = up.get()
            bot['up'] = up_na

            vi = view.get().strip()
            bot['view'] = vi

            chat = bullet.get().strip()
            bot['bullet'] = chat

            yield bot


