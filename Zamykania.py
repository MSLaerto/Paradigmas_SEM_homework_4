def outer(n):
    a = 0
    def inner():
        nonlocal a
        print(f'Число во внешней функции до итерации: {a}')
        a += n
        print(f'Число во внешней функции после итерации: {a}')
    return inner
f = outer(5)
for i in range(5):
    print(f'Итерация {i+1}')
    f()
    print('\n')