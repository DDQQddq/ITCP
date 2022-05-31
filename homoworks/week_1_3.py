# author: Elf Dobby
# Github: https://github.com/DDQQddq/ITCP

def _add(first, second):
    result = int(first)+int(second)
    print(result)


def _subtract(first, second):
    result = int(first)-int(second)
    print(result)


def _multiply(first, second):
    result = int(first)*int(second)
    print(result)


def _divide(first, second):
    result = int(first) / int(second)
    print(result)


a = input('请输入第一个数据：')
b = input('请输入第二个数据：')
print('选择您要使用的运算类型：')
i = input('加减乘除依次为1,2,3,4: ')

if int(i) == 1:
    _add(a, b)

elif int(i) == 2:
    _subtract(a, b)

elif int(i) == 3:
    _multiply(a, b)

elif int(i) == 4:
    _divide(a, b)

else:
    print('出错了！')
