from scrapy import cmdline

# 输出相应文件（已经生成，故注释）
cmdline.execute('scrapy crawl quotes -o quotes.csv -t csv'.split())
# cmdline.execute('scrapy crawl quotes -o quotes.json -t json'.split())
# cmdline.execute('scrapy crawl quotes'.split())
