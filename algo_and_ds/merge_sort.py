def merge(A:list, B:list):
    """Сливает два отсортрованных списка A и B в один отсортированный
       список C
    """

    C = [0] * (len(A) + len(B))
    i = j = k = 0

    while i < len(A) and j < len(B):
        if A[i] <= B[j]: # реализация устойчивости сортировки,
                         # при равенстве элементов сначала добавляется
                         # элемент из первого списка => сохраняется порядок
                         # следования элементов в результирующем списке
            C[k] = A[i]
            i += 1
            k += 1
        else:
            C[k] = B[j]
            j += 1
            k += 1

    while i < len(A):
        C[k] = A[i]
        i += 1
        k += 1

    while j < len(B):
        C[k] = B[j]
        j += 1
        k += 1
    return C

def merge_sort(A:list):
    """Сортирует список рекурсивным методом слияния"""
    if len(A) <= 1:
        return
    middle = len(A) // 2
    L = [A[i] for i in range(0, middle)]
    R = [A[i] for i in range(middle, len(A))]
    merge_sort(L)
    merge_sort(R)
    C = merge(L, R)
    for i in range(len(A)): # len(A) = len(C)
        A[i] = C[i]


def test_merge_sort(sort_algorithm):

    A = [1, 5, 2, 6, 8, 3, 7, 5, 9, 3, 2, 1, 5, 7]
    A_sorted = [1, 1, 2, 2, 3, 3, 5, 5, 5, 6, 7, 7, 8, 9]
    sort_algorithm(A)
    print("testcase #1 -", "ok" if A_sorted == A else "fail")

    A = [x for x in range (5, 10)] + [x for x in range(5)] + [x for x in range(10, 15)]
    A_sorted = [x for x in range(15)]
    sort_algorithm(A)
    print("testcase #2 -", "ok" if A_sorted == A else "fail")

test_merge_sort(merge_sort)

    
