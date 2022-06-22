from urllib.parse import urlparse, urlunparse, urlsplit, urlunsplit, urlencode, quote, unquote

# scheme://netloc/path;params?query#fragment
url = 'https://www.baidu.com/index.html;user?id=5#comment'

# urllib.parse.urlparse(urlstring, scheme ='', allow_fragments=True)
print(urlparse(url))

data = ['https', 'www.baidu.com', 'index.html', 'user', 'a=6', 'comment']
print(urlunparse(data))

print(urlsplit(url))

data_2 = ['https', 'www.baidu.com', 'index.html', 'a=6', 'comment']
print(urlunsplit(data_2))

params = {
    'name': 'elf',
    'age': 22
}
base_url = 'https://www.baidu.com?'
url = base_url + urlencode(params)
print(url)

keyword = '圣嘉然'
url = 'https://wwww.baidu.com/s?wd=' + quote(keyword)
print(url)

un_url = 'https://wwww.baidu.com/s?wd=%E5%9C%A3%E5%98%89%E7%84%B6'
print(unquote(un_url))
