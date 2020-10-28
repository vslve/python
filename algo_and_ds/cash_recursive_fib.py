# кэш для хранения значений каждого числа Фибоначчи до n
# заранее опередлен размер, т.е. максимальное число
fib = [None] * 10000 

def cash_recursive_fib(n:int):
    """Вычисляет n-ое число Фибоначчи методом рекурсии с запоминанием в кэш"""

    assert n > 0 and n <= 10000, "Допустимое 0 < n < 1000"
    
    if fib[n - 1] is None:
        if n <= 2:
            fib[n - 1] = n - 1
        else:
            fib[n - 1] = cash_recursive_fib(n-1) + cash_recursive_fib(n-2)
    return fib[n-1]

def test_fib(fun):
    print("testcase #1 - ", "ok" if fun(10) == 34 else "fail")
    print("testcase #2 - ", "ok" if fun(7) == 8 else "fail")
    print("testcase #3 - ", "ok" if fun(1) == 0 else "fail")
    print("testcase #4 - ", "ok" if fun(5) == 3 else "fail")
    print("testcase #5 - ", "ok" if fun(17) == 987 else "fail")

test_fib(cash_recursive_fib)
