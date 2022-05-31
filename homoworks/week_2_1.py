# author: Elf Dobby
# Github: https://github.com/DDQQddq/ITCP

posts = [
    {
        'id': 1,
        'title': '测试标题1',
        'author': '匿名用户1',
        'publish': '2018-01-01',
        'content': '这里是帖子的测试内容1……',
        'reply': [  # 作业文档这里用的是replay，我猜测您是想用reply
            {
                'publish': '2018-01-06',
                'content': '这里是回复内容1……'
            },
            {
                'publish': '2018-01-05',
                'content': '这里是回复内容2……'
            }
        ]
    },
    {
        'id': 2,
        'title': '测试标题2',
        'author': '匿名用户3',
        'publish': '2018-02-11',
        'content': '这里是帖子的测试内容2……',
        'reply': [
            {
                'publish': '2018-02-15',
                'content': '这里是回复内容3……'
            },
            {
                'publish': '2018-01-12',
                'content': '这里是回复内容4……'
            }
        ]
    }
]

print("论坛帖子")
print('====================')
i = 0
while i <= 1:
    print(f"postID:{posts[i]['id']}")
    print(f"title:{posts[i]['title']}")
    print(f"author:{posts[i]['author']}")
    print(f"{posts[i]['publish']}")
    print('-------------------------------')
    print(f"publish:{posts[i]['content']}")
    print(f"\n回复<{posts[i]['reply'][0]['publish']}>:{posts[i]['reply'][0]['content']}")
    print(f"回复<{posts[i]['reply'][0]['publish']}>:{posts[i]['reply'][1]['content']}\n")
    i += 1
