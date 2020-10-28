def lcs(A:list, B:list):
    """Вычисляет длину наибольшей общей подпоследовательности
       последовательностей А длины n и B длины m.
    """
    n = len(A)
    m = len(B)
    L = [[0] * (m + 1) for i in range(n + 1)] 
    for i in range(1, n + 1): # здесь i - номер элемента в последовательности A
        for j in range(1, m + 1): # здесь j - номер элемента в последовательности B
            if A[i-1] == B[j-1]: # первый элемент последовательности имеет индекс 0
                L[i][j] = 1 + L[i-1][j-1]
            else:
                L[i][j] = max(L[i-1][j], L[i][j-1])
    return L[-1][-1]


def test_lcs(fun):
    A = [1, 5, 2, 6, 8, 3, 1, 6, 10]
    B = [1, 7, 2, 5, 9, 4, 15, 3, 1, 10]
    print("testcase #1 -", "ok" if fun(A, B) == 5 else "fail")

    A = [1, 2, 3, 4, 5]
    B = []
    print("testcase #2 -", "ok" if fun(A, B) == 0 else "fail")

    A = [5, 4, 3, 2, 1, 1, 1, 0]
    B = [2, 1, 1, 0]
    print("testcase #3 -", "ok" if fun(A, B) == 4 else "fail")

test_lcs(lcs)
