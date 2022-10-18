Comment = """ Числа Фибоначчи — элементы числовой последовательности 0, 1, 1, 2, 3, 5, 8, 13, 21, 34,
        55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, …,
        в которой первые два числа равны 0 и 1, а каждое последующее число равно сумме двух
        предыдущих чисел."""

def fib_bad(n):
    """ Плохой алгоритм"""
    if n<=1:
        return n
    else:
        n = fib_bad(n-1) + fib_bad(n-2)
        return n
for i in range(11):
    print(fib_bad(i), end=' ')
print()    
        
    

#быстрый алгоритм на основании массива
# линейная асимптотика
n = 10
fib = [0,1] + [0]*(n-1)
for i in range(2, n+1):
    fib[i] = fib[i-1] + fib[i-2]
print(*fib)
