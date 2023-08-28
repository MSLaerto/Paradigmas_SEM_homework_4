def IsPrime(n):
    a = n
    k = 0
    for i in range(2, a // 2+1):
        if (a % i == 0):
            k = k+1
    if (k <= 0):
        print(a , end = " ")

def lazy_loading(items):
    for i in items:
        yield i 
items = [i for i in range(1000)]
for i in lazy_loading(items):
    IsPrime(i)