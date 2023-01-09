def fib(n):
    # naive implementation
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

def f(a, b, n):
    # linear recursive routine
    if n <= 1:
        return b
    return f(b, a + b, n - 1)

def fib_top_down_dp(n):
    # runtime: O(n), space: O(n)
    seen = {0: 0, 1: 1}

    def fib(n):
        if n <= 1:
            return n
        if n not in seen:
            seen[n] = fib(n - 1) + fib(n - 2)
        return seen[n]
    return fib(n)

def fib_bottom_up_dp(n):
    # constant O(1) space and time of O(n)
    if n == 0:
        return 0
    p, c = 0, 1
    while n - 1:
        r = p + c
        p = c
        c = r
        n -= 1
    return c 
print(fib(30))
