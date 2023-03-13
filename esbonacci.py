#inizio

def iterative_fibonacci(n: int) -> int:
    """
    Calcola l'n-esimo numero della successione di Fibonacci in modo iterativo.
    """
    if n == 0:
        return 0
    if n == 1:
        return 1
    fib_minus_2 = 0
    fib_minus_1 = 1
    for i in range(2, n+1):
        fib = fib_minus_1 + fib_minus_2
        fib_minus_2 = fib_minus_1
        fib_minus_1 = fib
    return fib

def recursive_fibonacci(n: int) -> int:
    """
    Calcola l'n-esimo numero della successione di Fibonacci in modo ricorsivo.
    """
    if n == 0:
        return 0
    if n == 1:
        return 1
    return recursive_fibonacci(n-1) + recursive_fibonacci(n-2)

