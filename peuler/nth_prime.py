from pymath import is_prime


def nth_prime(n):
    i = 1
    count = 0

    while 1:
        if is_prime(i):
            count += 1

            if count == n:
                return i
        i += 1

res = nth_prime(10001)
print(res)
