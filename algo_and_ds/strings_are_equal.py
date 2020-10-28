def equal(a:str, b:str):
    """Определяет равны ли две строки.

       Если строки равны - возвращает True. Иначе - False.
    """

    if len(a) != len(b):
        return False
    for i in range(len(a)):
        if a[i] != b[i]:
            return False
    return True


def test_equal(fun):

    a = "12345"
    b = "12345"
    print("test #1 -", "ok" if fun(a, b) == True else "fail")

    a = "a"
    b = "ab"
    print("test #2 -", "ok" if fun(a, b) == False else "fail")

    a = "aaaaaa"
    b = "aaaaab"
    print("test #3 -", "ok" if fun(a, b) == False else "fail")

test_equal(equal)
