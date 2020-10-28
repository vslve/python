def insert_sort(A):
    """Сортировка списка A методом вставки"""
    N = len(A)
    for top in range(1, N):
        k = top
        while k > 0 and A[k] < A[k-1]:
            A[k], A[k-1] = A[k-1], A[k]
            k -= 1
        

def choice_sort(A):
    """Сортировка списка A методом выбора"""
    N = len(A)
    for pos in range(N - 1):
        for k in range(pos + 1, N):
            if A[k] < A[pos]:
                A[k], A[pos] = A[pos], A[k]

def babble_sort(A):
    """Сортировка списка A методом пузырька"""
    N = len(A)
    for pass_number in range(N - 1):
        for k in range(N - 1 - pass_number):
            if A[k] > A[k+1]:
                A[k], A[k+1] = A[k+1], A[k]
                

def test_sort(sort_algorithm):
    print("Тестируем: ", sort_algorithm.__doc__)
    A = [4, 2, 5, 1, 3]
    A_sorted = [1, 2, 3, 4, 5]
    sort_algorithm(A)
    print("testcase #1 - ", end="")
    print("Ok" if A == A_sorted else "Fail")

    A = list(range(10, 20)) + list(range(10))
    A_sorted = list(range(20))
    sort_algorithm(A)
    print("testcase #2 - ", end="")
    print("Ok" if A == A_sorted else "Fail")

    A = [4, 4, 5, 1, 3, 1, 2]
    A_sorted = [1, 1, 2, 3, 4, 4, 5]
    sort_algorithm(A)
    print("testcase #1 - ", end="")
    print("Ok" if A == A_sorted else "Fail")

if __name__ == "__main__":
    test_sort(insert_sort)
    test_sort(choice_sort)
    test_sort(babble_sort)
    
    
