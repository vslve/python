def check_sorted(A, ascending=True):
    """Проверяет отсортирован ли список(за O(n)) по возрастанию, если ascending == True,
       или по убыванию, если ascending == False. 
       Возвращает True, если список отсортирован,
       иначе - False.
    """

    flag = True
    N = len(A)
    n = int(ascending) * 2 - 1
    for i in range(N - 1):
        if A[i] * n > A[i + 1] * n:
            flag = False
            break
    return flag


def test_check_sorted(sorted):
    A = [1, 2, 3, 4, 5]
    print("testcase #1 -", "ok" if sorted(A) else "fail")

    A = [5, 4, 3, 2, 1]
    print("testcase #2 -", "ok" if sorted(A, False) else "fail")

test_check_sorted(check_sorted)
