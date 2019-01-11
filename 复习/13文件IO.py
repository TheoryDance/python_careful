#!/usr/bin/python3
f = open('00.txt')
content = f.read()  # <class 'str'>
print(content, type(content))
f.close()
print('------------------------------------------')
f = open('00.txt')
content = f.readlines()  # 作为一个列表进行存放
print(content)
f.close()
print('------------------------------------------')
# 读取图片内容，写入到一个新的文件，使得文件能够打开
with open('C:/Users/grand/Pictures/this/8.jpg', 'rb') as f:
    ob = f.read()  # <class 'bytes'>
    print(type(ob))
    newf = open('demo.jpg', 'wb')
    newf.write(ob)
    newf.close()

