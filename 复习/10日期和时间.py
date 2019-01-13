#!/usr/bin/python3
import time

ticks = time.time()  # 时间戳
print('当前的时间戳：', ticks)

# 时间元组
time_tuple = time.localtime(time.time())
print('本地时间：', time_tuple)

localtime = time.asctime(time_tuple)
print('本地时间：', localtime)

str1 = time.strftime('%Y-%m-%d %H:%M:%S', time_tuple)
print(str1)

str2 = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
print(str2)


import calendar

cal = calendar.month(2016, 1)
print(cal)