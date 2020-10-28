def shift_the_array_to_the_left(A:list, N:int):
    """Сдвигает каждый элемент массива влево на один шаг"""
    tmp = A[0]
    for i in range(N - 1):
        A[i] = A[i + 1]
    A[N - 1] = tmp

def test_shift_the_array_to_the_left():
    A1 = [0, 1, 2, 3, 4, 5]
    print(A1)
    shift_the_array_to_the_left(A1, 6)
    print(A1)
    if A1 == [1, 2, 3, 4, 5, 0]:
        print("#test1 - ok")
    else:
        print("#test1 - fail")

    A2 = [5, 0, 0, 0, 7, 0, 0, 0, 1]
    print(A2)
    shift_the_array_to_the_left(A2, 9)
    print(A2)
    if A2 == [0, 0, 0, 7, 0, 0, 0, 1, 5]:
        print("#test2 - ok")
    else:
        print("#test2 - fail")

test_shift_the_array_to_the_left()
