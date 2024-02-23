"""a=int(input())
b=int(input())
for i in range(a,b+1):
    print(i**2)"""
a=int(input())
b=int(input())
def test(a,b):
    for i in range(a,b+1):
        yield i**2
for i in test(a,b):
    print(i)