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