import sys

x = object()
print(type(x))
print(sys.getrefcount(x))
y = x
print(sys.getrefcount(x))

# 레퍼런스 값을 줄인다.
del x
print(sys.getrefcount(y))

xyz = 10
print(sys.getrefcount(xyz))


