def shift_the_array_to_the_right(A:list, N: int):
    """ Сдвигает каждый элемент массива вправо на один шаг"""
    tmp = A[N - 1]
    for i in range(N - 2, -1, -1):
        A[i + 1] = A[i]
    A[0] = tmp

def test_shift_the_array_to_the_right():
    A1 = [0, 1, 2, 3, 4, 5]
    shift_the_array_to_the_right(A1, 6)
    if A1 == [5, 0, 1, 2, 3, 4]:
        print("#test1 - ok")
    else:
        print("#test1 - fail")

    A2 = [0, 0, 0, 0, 0, 0, 0, 0, 1]
    shift_the_array_to_the_right(A2, 9)
    if A2 == [1, 0, 0, 0, 0, 0, 0, 0, 0]:
        print("#test2 - ok")
    else:
        print("#test2 - fail")
        
test_shift_the_array_to_the_right()
