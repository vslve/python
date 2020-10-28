def recursive_fib(n):
    """Вычисляет n-ое число Фибоначчи методом рекурсии.
       Неоптимальный алгоритм O(fibN).
    """

    if n <= 2:
        return n - 1
    else:
        return recursive_fib(n-1) + recursive_fib(n-2)


def fib(n):
    """Вычисляет n-ое число Фибоначчи методом динамического программирования.
       Оптимальный алгоритм. O(n)
    """

    fib_n = [0, 1] + [0] * (n - 2)
    for i in range(2, n):
        fib_n[i] = fib_n[i - 1] + fib_n[i - 2]
    return fib_n[n-1]

print(recursive_fib(10))
print(fib(10))

def test_recursive_fib(fib):

    n = 10
    print("recursive_fib testcase #1 -", "ok" if fib(n) == 34 else "fail")

def test_fib(fib):

    n = 10
    print("fib testcase #1 -", "ok" if fib(n) == 34 else "fail")

test_recursive_fib(recursive_fib)
test_fib(fib)
