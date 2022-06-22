from scrapy import cmdline

cmdline.execute('scrapy crawl popular -o popular.csv -t csv'.split())
# cmdline.execute('scrapy crawl popular -o popular.json -t json'.split())
# cmdline.execute('scrapy crawl popular'.split())
