n=int(input())
def test(n):
    for i in range(n,-1,-1):
        yield i
for i in test(n):
    print(i)