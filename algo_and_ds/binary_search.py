def left_bound(A:list, key):
    """Находит левую границу для искомого элемента.
       Т.е. ближайший элемент слева меньший искомого.
    """

    left = -1
    right = len(A)
    
    while right - left > 1:
        middle = (left + right) // 2
        if A[middle] < key:
            left = middle
        else:
            right = middle

    return left

def right_bound(A:list, key):
    """Находит правую границу для искомого элемента
       Т.е. ближайший элемент мправа больший искомого.
    """

    left = -1
    right = len(A)
    
    while (right - left > 1):
        middle = (left + right) // 2
        if A[middle] <= key:
            left = middle
        else:
            right = middle

    return right

def search(A, key):
    """Осуществляет поиск элемента key в списке A"""
    
    right = right_bound(A, key)
    left = left_bound(A, key)
    if right - left == 2:
        print("Элемент найден в позиции:", left + 1)
    elif right - left > 2:
        print("Элемент найден в позициях:", *[x for x in range(left + 1, right)])
    else:
        print("Элемент не найден")

if __name__ == "__main__":

    def test_search(search):
        A = [0, 0, 0, 0, 4, 4, 5, 7, 8, 9, 10, 14, 15, 15, 19]
        print("testcase #1 -", "ok" if search(A, 2) == print("Элемент не найден") else "fail")
        print()

        A = [0, 0, 0, 0, 4, 4, 5, 7, 8, 9, 10, 14, 15, 15, 19]
        print("testcase #2 -", "ok" if search(A, 15) == print("Элемент найден в позициях: 12 13") else "fail")
        print()
        
        A = [0, 0, 0, 0, 4, 4, 5, 7, 8, 9, 10, 14, 15, 15, 19]
        print("testcase #3 -", "ok" if search(A, 7) == print("Элемент найден в позиции: 7") else "fail")
        print()

    test_search(search)
