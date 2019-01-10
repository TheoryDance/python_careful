#!/usr/bin/python3

count = 0
while count < 5:
    print(count, ' 小于 5')
    count += 1
else:
    print(count, ' 大于等于 5')
print('------------------------')

sites = ['Baidu', 'Google', 'Runoob', 'Taobao']
for site in sites:
    if site == 'Runoob':
        print('菜鸟教程！')
        break
    print('循环数据', site)
else:
    print("正常完成循环")
print('Game Over!')
print('------------------------')

for i in range(5, 9):
    print(i)
