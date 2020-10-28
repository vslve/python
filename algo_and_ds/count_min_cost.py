def count_min_cost(n, price):
    """Осуществляет расчет минимальной стоимости достижения пункта n.

       price - список стоимостей посещения пунктов.

       Возможные ходы: +1, +2.
    """

    C = [float("-inf"), price[1], price[1] + price[2]]  + [0] * (n - 2)
    for i in range(3, n + 1):
        C[i] = pice[i] + min(price[i-1], price[i-2]
    return C[n]
