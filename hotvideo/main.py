from scrapy import cmdline

# cmdline.execute('scrapy crawl bilibili -o bilibili.csv -t csv'.split())
cmdline.execute('scrapy crawl bilibili'.split())
