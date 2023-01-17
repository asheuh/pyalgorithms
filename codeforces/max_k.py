import sys
from time import time

def solve(n):
    b = 1

    while n > 1:
        n >>= 1
        b <<= 1
    return b - 1


def solve_sequence_pair_weight(n, arr):
    maps = {}
    ans = 0

    for i in range(n):
        if arr[i] in maps:
            ans += maps[arr[i]] * (n - i)
        else:
            maps[arr[i]] = 0

        maps[arr[i]] += i + 1
    
    return ans

def solve_number_of_eq_pairs_bf(n, arr):
    # brute force

    current = 0
    nxt = 1
    count = 0

    while current < n and nxt < n:
        if arr[current] == arr[nxt]:
            count += 1
            nxt += 1
        else:
            nxt += 1

        if nxt == n:
            current += 1
            nxt = current + 1
    return count


def solve_number_of_eq_pairs_opmized(n, arr):
    maps = {} # keep a dict for storing seen numbers
    count = 0

    for i in range(n):
        if arr[i] in maps:
            count += maps[arr[i]]
        else:
            maps[arr[i]] = 0

        maps[arr[i]] += 1
    return count

def add_bin_number(binary):
    total = 0

    while binary > 10:
        total += binary % 10
        binary //= 10
    return total + binary


if __name__ == '__main__':
#     input = lambda: sys.stdin.readline().rstrip()
#     T = int(input())
# 
#     for _ in range(T):
#         n = int(input())
#         arr = list(map(int, input().split()))
#         r = solve_sequence_pair_weight(n, arr)

    s = '100611591 100611591 983971727 572464533 983971727 837355589 967439567 66290426 913510375 983971727 837355589 475845364 983971727 683371437 445904892 572464533 468239467 475845364 572464533 840697540 967439567 683371437 840697540 135608862 837355589 100611591 935197499 611510378 935197499 683371437 100611591 837355589 66290426 951644064 707607840 611510378 707607840 445904892 967439567 707607840 983971727'
    arr = [int(i) for i in s.split(' ')]
    n = len(arr)
    
    t1 = time()
    R = solve_number_of_eq_pairs_bf(n, arr)
    el = time() - t1

    t2 = time()
    Rop = solve_number_of_eq_pairs_opmized(n, arr)
    el2 = time() - t2
    print(R, Rop)

    print('Time')
    print('BF', el)
    print('OP', el2)
    print(el2 < el)
    

    bi = add_bin_number(123)
    print(bi)
