def count_sort(N):
    """Сорртировка списка из N элементов методом подсчета.

       О(n).
       
       Применяется для заранее известного
       ограниченного диапозона элементов списка.

       Например последовательность чисел от 0 до 9, где
       числа могут повторяться.
    """
    counter = [0] * N
    for i in range(N):
        x = int(input())
        counter[x] += 1

    for digit in range(N):
        count = counter[digit]
        if count > 0:
            for k in range(count):
                print(digit, end=" ")
                
N = int(input("Введите количество сортируемых элементов: "))
count_sort(N)
    
