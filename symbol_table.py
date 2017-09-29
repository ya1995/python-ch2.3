# 심볼 테이블 내용 확인
g_a = 1
g_b = 'symbol'


for i in range(5):
    g_c = 3
    g_d = 'python'
    print(locals())


def f():
    l_a = 2
    l_b = 'table'
    print(locals())


f()
print(globals())


class MyClass:
    x = 10
    y = 20


# 0. 내장 타입 객체나 내장 함수 네임스페이스 접근 금지
# 더 확장 불가
# print(g_a.__dict__)
# g_a.k = 'hello'
# print(print.__dict__)
# print.k = 'hello'

# 1. 클래스 객체
print(MyClass.__dict__)

# 2. 정의된 함수 객체
f.k = 'hello'
print(f.__dict__)

# 3. 인스턴스 객체
o = MyClass()
o.x = 100
print(o.__dict__)
print(o.x)