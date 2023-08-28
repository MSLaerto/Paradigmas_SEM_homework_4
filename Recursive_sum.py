def RecursiveSum(n):
    if n > 0 :
        return n + RecursiveSum(n-1)
    else:
        return 0
n = int(input("Введите n : "))    
print(f"Сумма от 1 до {n} равна : {RecursiveSum(n)}")