import copy

# copy reference
a = 1
b = a

a = [1, 2, 3]
a = [4, 5, a]
x = [a, b, 100]
y = x

print(x)
print(y)
print(x is y)

x[2] = 0
print(x)
print(y)

# shallow copy
a = [1, 2, 3]
a = [4, 5, a]
x = [a, b, 100]
y = copy.copy(x)

print(x)
print(y)
print(x is y)
print(x[0] is y[0])

# deep copy
a = [1, 2, 3]
a = [4, 5, a]
x = [a, b, 100]
y = copy.deepcopy(x)


print(x)
print(y)
print(x is y)
print(x[0] is y[0])

# 깊은 복사가 복합 객체만을 생성하기 때문에
# 복합객체가 한개만 있는경우 얕은 복사와 깊은 복사의 차이가 없다
a = ['hello', 'world']
b = copy.deepcopy(a)
print(a is b)
print(a[0] is b[0])

