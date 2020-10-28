def lis(A):
    """Находит длину наибольшей возрастающей подпоследователтности
       последовательности А длиной n.
    """
    n = len(A)
    L = [0] * (n + 1)
    for i in range(1, n + 1): # i - номер элемента в последовательности A
        m = 0
        for j in range(1, i): # j - номер элемента
            if A[i-1] > A[j-1] and L[j] > m:
                m = L[j]
        L[i] = m + 1
    return L[n]

def test_lis(fun):
    A = [1, 2, 0, 1, 2, 3]
    print("testcase #1 -", "ok" if fun(A) == 4 else "fail")

    A = []
    print("testcase #2 -", "ok" if fun(A) == 0 else "fail")

    A = [1]
    print("testcase #3 -", "ok" if fun(A) == 1 else "fail")

test_lis(lis)
