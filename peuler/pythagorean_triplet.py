import math

from pymath import is_coprime

def generate_euclid(x):
    # Generate a, b, c using Euclid's formula
    # a = k ⋅ ( m 2 − n 2 ) ,   b = k ⋅ ( 2 m n ) ,   c = k ⋅ ( m 2 + n 2 ): a=k\cdot (m^{2}-n^{2}),\ \,b=k\cdot (2mn),\ \,c=k\cdot (m^{2}+n^{2})
    # assert a + b + c = n
    # assert a^^2 + b^^2 = c^^2
    # assert a<b<c
    a = b = c = 0
    k = 1 # if > 1 the pt generates uniquely
    perms = permutations(range(x), 2)
    pts = []
    for perm in perms:
        m, n = perm
        if m > n > 0 and is_coprime(m, n) and (not m & 1 or not n & 1):
            a = k * (m**2 - n**2) 
            b = k * (2 * m * n)
            c = k * (m**2 + n**2) 
            is_pt = a**2 + b**2 == c**2
            pts.append((a, b, c))
    return pts


def naive_approach(n):
    starta = 3
    enda = (n - 3) // starta
    for a in range(starta, enda):
        for b in range(a + 1, (n - 1 - a) // 2):
            c = n - a - b
            is_pt = a**2 + b**2 == c**2
            if is_pt:
                return a * b *c


def parametrisation(n):
    # https://en.wikipedia.org/wiki/Pythagorean_triple#General_properties
    # https://en.wikipedia.org/wiki/Pythagorean_triple#Special_cases
    s = n // 2
    limit = math.ceil(math.sqrt(s)) - 1

    for m in range(2, limit):
        if s % m == 0:
            sm = s // m
            while sm % 2 == 0: # Removing all factors of 2 to reduce search space
                sm = sm // 2

            if m % 2 == 1:
                k = m + 2
            else:
                k = m + 1

            while k < 2 * m and k <= sm:
                if sm % k == 0 and is_coprime(k, m):
                    d = s // (k * m)
                    n = k - m
                    a = d * (m**2 - n**2) 
                    b = d * (2 * m * n)
                    c = d * (m**2 + n**2)
                k += 2

if __name__ == '__main__':
    n = 1000
    res = parametrisation(n)

