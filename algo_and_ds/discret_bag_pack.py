def discret_bag_pack(m:list, v:list, N:int, M:int):
    """Определяет максимальную стоимость предметов, которые помещаются
       в рюкзак емкостью M.

       m - список масс предметов.
       v - список стоимостей предметов.

       Можно взять только первые N предметов.
       N <= len(m) == len(v).
    """

    F = [[0]*(N + 1) for k in range(M + 1)]
    for i in range(1, N + 1): # номер предмета
        for j in range(1, M + 1): # вместимость рюкзака
            if m[i-1] <= j: # первый предмет имеет индекс 0
                F[j][i] = max(F[j-m[i-1]][i-1] + v[i-1], F[j][i-1])
            else:
                F[j][i] = F[j][i-1]
    return F[M][N]



def test_bag_pack(fun):
    m = [2, 5, 1, 7, 3, 8, 4, 5, 5, 7, 1]
    v = [5, 2, 1, 5, 4, 8, 3, 2, 3, 5, 2]
    N = 11
    M = 5
    print("testcase #1 - ", "ok" if fun(m, v, N, M) == 9 else "fail")

    m = [2, 5, 1, 7, 3, 8, 4, 5, 5, 7, 1]
    v = [5, 2, 1, 5, 4, 8, 3, 2, 3, 5, 2]
    N = 5
    M = 5
    print("testcase #2 - ", "ok" if fun(m, v, N, M) == 9 else "fail")

    m = [2, 5, 1, 7, 3, 8, 4, 5, 5, 7, 1]
    v = [5, 2, 1, 5, 4, 8, 3, 2, 3, 5, 2]
    N = 7
    M = 15
    print("testcase #3 - ", "ok" if fun(m, v, N, M) == 18 else "fail")


test_bag_pack(discret_bag_pack)
