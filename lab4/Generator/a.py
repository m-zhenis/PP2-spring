"""   print(i**2) 
n=int(input())
for i in range(n):
"""
n=int(input())
def a(n):
    for i in range(n):
        yield i**2
for i in a(n):
    print(i)