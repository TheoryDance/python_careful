# 对象继承list写法
class Mylist(list):
    def popleft(self):
        self.reverse()
        res = self.pop()
        self.reverse()
        return res

m = Mylist()
m.append('hello')
m.append('world')
m.append('world2')
print(m)
print(m.popleft())
print(m.popleft())
print('----------------------------------')
from collections import deque
queue = deque(["Eric", "John", "Michael"])
print(queue.popleft())
print(queue.popleft())

print('--------------------多继承------------------------------')
class Person1:
    def say(self):
        print('this is Person1.say()')
class Person2:
    def say(self):
        print('this is Person2.say()')
class Child(Person2, Person1):
    pass

p = Child()
p.say()