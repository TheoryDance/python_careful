dict1 = {'name': 'ranfs', 'info': {'age': 27, 'addr': '大渡口'}}
dict2 = dict1.copy()  # 字典浅拷贝
print(id(dict1), id(dict2))
dict2['name'] = 'grand_ranfs'
dict2['info']['home'] = 1
print(dict1)
print(dict2)