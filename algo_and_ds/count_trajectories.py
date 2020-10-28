def count_trajectories(n, allowed:list):
    """Осущесталяет поиск количества различных траекторий
       в пункт n.
       
       allowed - список, содержащий информацию о доступности пункта
       для посещения: если allowed[n] == true - пункт n открыт для посещения,
                             если allowed[n] == false - закрыт.
       
       Возможные ходы: +1, +2, +3.
    """

    K = [0, 1, int(allowed[2])] + [0] * (n - 2) # в пунктах, закрытых для посещения изначально 0
    for i in range(3, n + 1):
        if allowed[i]:
            K[i] = K[i-1] + K[i-2] + K[i-3]
    return K[n]

print(count_trajectories(5))


