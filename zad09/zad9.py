def silnia(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * silnia(n-1)
    
def symbol_newtona_definicja(n, k):
    if k == 0 or k == n:
        return 1
    else:
        return silnia(n) / (silnia(k) * silnia(n-k))
    
def symbol_newtona_rekurencyjnie(n, k):
    if k == 0 or k == n:
        return 1
    else:
        return symbol_newtona_rekurencyjnie(n-1, k-1) + symbol_newtona_rekurencyjnie(n-1, k)
    
def symbol_newtona_iteracyjnie(n, k):
    result = 1
    for i in range(1, k + 1):
        result = result * (n - i + 1) // i
    return result

def stirling_II_rekurencyjnie(n, k):
    if n == k == 0:
        return 1
    elif n > 0 and k == 0:
        return 0
    elif n == 0 and k > 0:
        return 0
    else:
        return k * stirling_II_rekurencyjnie(n-1, k) + stirling_II_rekurencyjnie(n-1, k-1)


def stirling_II_wzor_suma(n, k):
    result = 0
    for j in range(k + 1):
        result += ((-1) ** (k - j)) * symbol_newtona_definicja(k, j) * (j ** n)
    result //= silnia(k)
    return result

def liczby_bella_rekurencyjnie(n):
    result = 0
    for k in range(n + 1):
        result += stirling_II_rekurencyjnie(n, k)
    return result

def liczby_bella_stirling(n):
    result = 0
    for k in range(n + 1):
        result += stirling_II_wzor_suma(n, k)
    return result


def liczba_podzialow(n, k):
    if n == 0 and k == 0:
        return 1
    elif n < 0 or k == 0:
        return 0
    else:
        return liczba_podzialow(n-k, k) + liczba_podzialow(n-1, k-1)
