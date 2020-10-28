def pi_function(s:str):
    """Находит длину максимального собственного суффикса строки,
       который является преффиксом.

       Собственный суффикс - суффикс строки, не являющийся самой строкой,
       т.е. не включающий в себя как минимум первый символ строки.
    """

    n = len(s)
    pi = [0] * n

    for i in range(1, n): # i - индекс элемента в строке 
        p = pi[i - 1] # pi функция для подстроки s[0:i]
        while p > 0 and s[p] != s[i]:
            p = pi[p - 1]
        if s[p] == s[i]:
            p += 1
        pi[i] = p
    return pi

def pi_substring(sub:str, s:str):
    """Находит вхождение подстроки sub в строку s.

       Возвращает индексы начала каждого вхождения
       Если вхождений нет возвращает устой список.
    """
    I = []
    string = sub + "#" + s
    pi = pi_function(string)
    for k in range(1, len(pi)):
        if pi[k] == len(sub):
            I.append(k - 2*len(sub))
    return I


def test_pi_substring(fun):
    sub = "aba"
    s = "abfsbabasabadsfwaabaababaabafsfaba"
    print("test #1 -", "ok" if fun(sub,s) == [5, 9, 17, 20, 22, 25, 31] else "fail")

    sub = "b"
    s = "abfsbabasabadsfwaabaababaabafsfaba"
    print("test #2 -", "ok" if fun(sub,s) == [1, 4, 6, 10, 18, 21, 23, 26, 32] else "fail")

    sub = "m"
    s = "abfsbabasabadsfwaabaababaabafsfaba"
    print("test #3 -", "ok" if fun(sub,s) == [] else "fail")
test_pi_substring(pi_substring)
