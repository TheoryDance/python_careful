#!/usr/bin/python3
#encoding=utf-8
# 这节应该在循环之后学习
import sys

list = [1, 2, 3, 4]
it = iter(list)
for x in it:
    print(x, end=" ")
print('\n---------------')

class MyNumbers:
    def __init__(self):
        print('调用__init__()方法')

    def __iter__(self):
        print('调用__iter__()方法')
        self.a = 1
        return self

    def __next__(self):
        print('调用__next__()方法')
        x = self.a
        self.a += 1
        return x


myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

print('---------------定义iter----------------')
class Linux1:
    def __init__(self):
        self.n = 12

    def __next__(self):
        x = self.n
        self.n += 2
        if x > 100:
            raise StopIteration
        return x

class System1:

    def __init__(self):
        self.n = 12

    def __next__(self):
        x = self.n
        self.n += 2
        if x > 100:
            raise StopIteration
        return x

    def __iter__(self):
        return self

aa = iter(System1())

# item = next(aa)
for item in aa:
# while item != None:
    print(item)
    # item = next(aa)
