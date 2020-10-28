def substring(sub, s):
    """Проверяет является ли строка sub подстрокой строки s.

       Если sub - подстрока s, то возвращает индексы начала каждого вхождения
       sub в s.

       Если sub не является подстрокой s - возвращает False.
    """
    I = []
    for i in range(len(s) - len(sub)):
        flag = True
        if s[i] == sub[0]:
            for j in range(1, len(sub)):
                if  s[i + j] != sub[j]:
                    flag = False
                    break
            if flag:
                I.append(i)
    if I:
        return I
    return False


def search_substring(sub, s):

    I = []
    for i in range(len(s) - len(sub)):
        if s[i:i+len(sub)] == sub:
            I.append(i)
    return I if I else False

def test_substring(fun):
    a = "123452345"
    b = "23"
    print("test #1 -", "ok" if fun(b, a) == [1, 5] else "fail")

    a = "123452345"
    b = "a"
    print("test #2 -", "ok" if fun(b, a) == False else "fail", end="\n\n")


def test_search_substring(fun):
    a = "123452345"
    b = "23"
    print("test #1 -", "ok" if fun(b, a) == [1, 5] else "fail")

    a = "123452345"
    b = "a"
    print("test #2 -", "ok" if fun(b, a) == False else "fail")

test_substring(substring)
test_search_substring(substring)

                
