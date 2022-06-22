import requests
import re

# req = requests.get('https://www.baidu.com')
# print(type(req))
# print(req.status_code)
# print(type(req.text))
# print(req.text)
# print(req.cookies)

# r = requests.get('https://httpbin.org/get')
# print(r.text)

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac Os X 10_11_4) AppleWebKit/537.36(KHTML, like Gecko) '
                  'Chrome/52.0.2743.116 Safari /537.36'
}

r = requests.get('https://www.zhihu.com/explore', headers=headers)
pattern = re.compile('explore-feed.*?question_link.*?>(.*?)</a>', re.S)
titles = re.findall(pattern, r.text)
print(titles)
