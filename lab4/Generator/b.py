"""n=int(input())
for i in range(n):
    if i%2==0:
        print(i)"""
n=int(input())
def test(n):
    for i in range(n):
        if i%2==0:
            yield i
for i in test(n):
    print(i)