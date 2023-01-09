def fib(d):
    a = 0
    b = 1
    n = 1

    while 1:
        x = a + b
        a = b
        b = x
        n += 1
        if count_digits(x) == d:
            break
    return n

def count_digits(n):
    t = 0
    while n >= 10:
        n //= 10
        t += 1
    return t + 1

result = fib(1000)
print(result)
