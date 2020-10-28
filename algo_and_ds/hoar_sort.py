def hoar_sort(A:list):
    """Рекрсивная сортировка Тони Хоара("Быстрая сортировка,
        Quick sort").
       Сортирует список A методом рекурсии.
    """

    if len(A) <= 1:
        return
    barrier = A[0]
    L = []
    E = []
    G = []
    for x in A:
        if x == barrier:
            E.append(x)
        elif x > barrier:
            G.append(x)
        else:
            L.append(x)
    hoar_sort(L)
    hoar_sort(G)
    i = 0
    for x in L + E + G:
        A[i] = x
        i += 1


def test_hoar_sort(sort_algorithm):
    A = [0, 1, 5, 2, 7, 3, 8, 3, 7, 8, 3, 5, 2, 1]
    A_sorted = [0, 1, 1, 2, 2, 3, 3, 3, 5, 5, 7, 7, 8, 8]
    sort_algorithm(A)
    print("testcase #1 -", "ok" if A == A_sorted else "fail")

    A = [x for x in range (20, -1, -1)]
    A_sorted = [x for x in range (21)]
    sort_algorithm(A)
    print("testcase #2 -", "ok" if A == A_sorted else "fail")


test_hoar_sort(hoar_sort)
