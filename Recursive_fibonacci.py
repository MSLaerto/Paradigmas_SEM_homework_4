def fibonachi_recursion(n):
    if n == 0 :
        return 0  
    if n in (1, 2):
        return 1
    return fibonachi_recursion(n - 1) + fibonachi_recursion(n - 2)
n = int(input("Введите n : "))    
print(f"Число Фиббоначи под номер {n} = {fibonachi_recursion(n)}")