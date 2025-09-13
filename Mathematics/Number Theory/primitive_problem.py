import math

def factorize(n):
    factors = {}
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors[d] = factors.get(d, 0) + 1
            n //= d
        d += 1
    if n > 1:
        factors[n] = factors.get(n, 0) + 1
    return factors

def phi(n):
    result = n
    p = 2
    while p * p <= n:
        if n % p == 0:
            while n % p == 0:
                n //= p
            result -= result // p
        p += 1
    if n > 1:
        result -= result // n
    return result

def is_primitive_root(g, p, factors_p_minus_1):
    n = p - 1
    for q in factors_p_minus_1:
        if pow(g, n // q, p) == 1:
            return False
    return True

if __name__ == '__main__':
    p = int(input().strip())
    if p == 2:
        print("1 1")
    else:
        n = p - 1
        factors = factorize(n)
        count_roots = phi(n)
        g = 2
        while g < p:
            if is_primitive_root(g, p, factors):
                break
            g += 1
        print(f"{g} {count_roots}")
