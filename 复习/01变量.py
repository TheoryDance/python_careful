# 命名规范：
# 变量命名：
# 类命名：
num1 = 20
list1 = [12, 34]
def myfunc():
    print(num1)
    print(list1)

myfunc()

sum = lambda num1, num2: num1 + num2
print(sum(23, 45))

# 变量作用域：局部作用域L、闭包函数外的函数中E、全局作用域G、内建作用域B
# 以L -> E -> G -> B的规则查找

x = int(2.9)  # 内建作用域
g_count = 0  # 全局作用域
def outer():
    o_count = 1  # 闭包函数外的函数中
    def inner():
        i_count = 2  # 局部作用域

"""
python中只有模块、类、函数、lambda才会引入新的作用域，其他代码块比如if，while，try等是不会
引入新的作用域的，也就是这些语句内定义的变量，外部也可以访问
准备看【函数/全局变量和局部变量】
global与nonlocal
"""

a = 10
def test(a):
    a += 1
    print(a)
test(a)
print(a)

print('-------------------------------------')