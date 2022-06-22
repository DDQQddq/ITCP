from urllib import request, parse

url = 'https://www.httpbin.org/post'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko',
    'HOST': 'httpbin.org'
}

dict_ = {
    'name': 'elf'
}

data = bytes(parse.urlencode(dict_), encoding='utf8')
req = request.Request(url=url, data=data, headers=headers, method='POST')
# req.add_header('User Agent', 'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko')
response = request.urlopen(req)
print(response.read().decode('utf-8'))
