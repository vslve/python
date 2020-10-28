def levenstain(a:str, b:str):
    """Определяет расстояние Левенштейна - редакционное расстояние двух строк.

       Т.е. какое минимальное количество редакторских правок
       необходимо внести в одну из строк для получения из нее
       строки полностью идентичной второй.
    """

    n = len(a)
    m = len(b)
    L = [[i + j if i * j == 0 else 0 for j in range(m + 1)] for i in range(n + 1)]

    for i in range(1, n + 1): # i, j - номер элемента в строке, не индекс
        for j in range(1, m + 1):
            if a[i-1] == b[j-1]:
                L[i][j] = L[i-1][j-1]
            else:
                L[i][j] = 1 + min(L[i][j-1], L[i-1][j], L[i-1][j-1])
    return L[n][m]

def test_levenstain(fun):
    a = "12345678910"
    b = "12344678910"
    print("estcase #1 -", "ok" if fun(a, b) == 1 else "fail")

    a = ""
    b = "12345"
    print("estcase #2 -", "ok" if fun(a, b) == 5 else "fail")

    a = "12345678910"
    b = "12345678910"
    print("estcase #3 -", "ok" if fun(a, b) == 0 else "fail")

test_levenstain(levenstain)
