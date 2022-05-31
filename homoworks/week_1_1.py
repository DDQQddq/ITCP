# author: Elf Dobby
# Github: https://github.com/DDQQddq/ITCP

goods = []
goods_1 = {}
goods_2 = {}
goods_1['num'] = '001'
goods_1['name'] = 'first'
goods_1['price'] = '9.15'
goods.append(goods_1)
goods_2['num'] = '002'
goods_2['name'] = 'second'
goods_2['price'] = '1919810'
goods.append(goods_2)
print(goods)
goods.remove(goods_2)
goods_1['price'] = '114514'
print(goods)
