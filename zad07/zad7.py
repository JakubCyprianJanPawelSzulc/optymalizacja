import random
import time

def karacuba(x,y):
    if x<10 or y<10:
        return x*y
    else:
        n = max(len(str(x)), len(str(y)))
        nby2 = n // 2

        high1, low1 = x // 10**nby2, x % 10**nby2
        high2, low2 = y // 10**nby2, y % 10**nby2

        z0 = karacuba(low1,low2)
        z1 = karacuba((low1+high1),(low2+high2))
        z2 = karacuba(high1,high2)

        return (z2*10**(2*nby2))+((z1-z2-z0)*10**(nby2))+(z0)

def normalne_mnozenie(x,y):
    return x*y

def test():
    num_bits = 1024
    random.seed(42)
    num1 = random.getrandbits(num_bits)
    num2 = random.getrandbits(num_bits)

    start_karacuba = time.time()
    result_karacuba = karacuba(num1, num2)
    end_karacuba = time.time()
    time_karacuba = end_karacuba - start_karacuba

    start_normalne = time.time()
    result_normalne = normalne_mnozenie(num1, num2)
    end_normalne = time.time()
    time_normalne = end_normalne - start_normalne

    print(f'Karacuba: {time_karacuba}')
    print(f'Normalne: {time_normalne}')

if __name__ == "__main__":
    test()