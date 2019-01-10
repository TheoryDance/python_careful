"""
1、由于\是转义符，如果不想反斜杠转移，可以在字符串前使用r
2、字符串可以用+运算连接在一起，用*运算符重复
3、字符串有两种索引方式：从左往右以0开始，从右往左以-1开始
4、字符串的截取语法
    变量[头下标:尾下标:步长]
"""

# \转义符与r
print('hello,\name')
print('\转义符与r')
print(r'hello,\name')

print('------2、字符串运算符--------')
first_name = "Ran"
last_name = "fusheng"
print(first_name + last_name)
print(first_name*2 + last_name)

print('------3、字符串索引方式--------')
name = "ranfusheng"
print(name[0])
print(name[-1])

print('------4、字符串的截取语法--------')
print(name[1:-1])
print(name[1:-1:2])

print('------转移字符--------')
print('响铃\a')
print('退格\b')

print('-----字符串格式化-----')
print("1、网站名：{name},地址：{url}".format(name="菜鸟教程", url="www.runoob.com"))
print("2、网站名：{},地址：{}".format("菜鸟教程", "www.runoob.com"))
print("3、网站名：{0}{1},地址：{0}".format("菜鸟教程", "www.runoob.com"))
ob = {"name": "菜鸟教程", "url": "www.runoob.com"}
# 通过字典设置参数
print("4、网站名：{name},地址：{url}".format(**ob))
# 通过列表索引设置参数
my_list = ['菜鸟教程', 'www.runoob.com']
print("5、网站名：{0[0]}, 地址 {0[1]}".format(my_list))  # "0" 是必须的

print('-----字符串内建函数-----')
print('ranfusheng'.capitalize())
print('ranfusheng'.center(20))
print('ranfusheng'.count('n'))
print('ranfusheng.jpg'.endswith('.jpg'))
print('ranfusheng.jpg'.endswith('.png'))
print('ran'.find('an'))  # 没有返回-1
print('ran'.index('an'))  # 没有会抛一个异常
print('ran fu sheng'.title())



