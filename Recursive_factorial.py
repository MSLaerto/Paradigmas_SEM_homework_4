def RecursiveFactorial(n):
    if n > 0 :
        return n * RecursiveFactorial(n-1)
    else:
        return 1
n = int(input("Введите n : "))    
print(f"Факториал {n} равен : {RecursiveFactorial(n)}")