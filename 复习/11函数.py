def myfunc(name, *vars):
    print('name = ', name)
    print('type(vars) = ', type(vars))
    print(vars)
    print('----------------------------------------')



T1 = (1, 2, 3, 4, ['name', 'age', 'addr'])
L1 = [1, 2, 3, 4, ['name', 'age', 'addr']]
myfunc('ranfs', T1)
myfunc('ranfs', *L1)

print(T1)
print(L1)
aa = (1,2)
def add(a, b, c):
    return a + b + c
print(add(a=1,*aa))