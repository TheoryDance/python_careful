# 1、list中可以包含不同的类型，序列都可以：索引，切片，加，乘，检查成员
list1 = ['ranfs', 'gaoc', 1991, 1995]
for item in list1:
    print(item, type(item))

# 2、使用.append(x) 进行追加元素
list1.append('@grand')
print(list1, id(list1))

# 3、使用del删除元素,跟remove()方法类似
del list1[2]
print(list1, id(list1))

list2 = list1.copy()
print(id(list2))