def sieve_of_Eratosthenes(N:int):
    """Определяет простые и составные числа в последовательности
       от 0 до N.
    """
    
    A = [True] * N
    A[0] = A[1] = False
    for i in range(2, N):
        if A[i] == True:
            for j in range(2 * i, N, i):
                A[j] = False
    for i in range (N):
        print(i, "-", "простое" if A[i] else "составное")

N = int(input())
sieve_of_Eratosthenes(N)
