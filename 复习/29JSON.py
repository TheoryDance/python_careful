#!/usr/bin/python3
"""
json.dumps() 将数据进行编码，将python数据类型转为json对应的类型
json.loads() 对数据进行解码，将json类型转为python类型
相互转换的类型对应表见：http://www.runoob.com/python3/python3-json.html
标准的json对象，键使用双引号进行包住
"""
data = {'name': "ranfusheng", 'addr': None}
print(data, type(data))

import json
json_str = json.dumps(data)
print(json_str, type(json_str))

data2 = json.loads(json_str)
print(data2, type(data2))
