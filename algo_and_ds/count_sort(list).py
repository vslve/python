def count_sort_digit(A:list, N:int):
    """Сортировка списка А методом подсчета. N - количество возможных значений элементов
       сортируемого списка.

       Список содержит элементы, область значений которых
       ограничена и известна перед началом сортировки.

       Например, числа от 0 до 9.
    """
    counter = [0] * N
    A_sorted = []
    for element in A:
        counter[element] += 1
    for digit in range(N):
        count = counter[digit]
        if count > 0:
            for k in range(count):
                A_sorted.append(digit)
    return A_sorted
         

def test_cout_sort_digit(sort):
    #тест сортировки списка чисел от 0 до 9, где числа могут повторяться
    A = [1, 4, 3, 6, 7, 4, 8, 6, 9, 5, 2, 1, 5, 7, 2, 8, 9, 5, 7, 3, 8, 4, 2, 1, 7, 5, 3, 7]
    N = 10
    A_sorted = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 5, 6, 6, 7, 7, 7, 7, 7, 8, 8, 8, 9, 9]
    print("testcase #1 - " + "Ok" if count_sort_digit(A, N) == A_sorted else "Fail")


if __name__ == "__main__":
    test_cout_sort_digit(count_sort_digit)
