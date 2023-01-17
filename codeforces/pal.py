def pal(s):
    n = len(s)
    pals = set()
    not_pals = set()
    s = [c for c in s]
    sc = s.copy()

    for i in range(n):
        m = ['a']
        f = sc[:i]
        k = sc[i:]
        r = [*f, *m, *k]

#         if i == (n - 1):
#             r = r + m

        out = ''.join(r)
        rev = ''.join(list(reversed(out)))

        if out == rev:
            pals.add(out)
        else:
            not_pals.add(out)

    if not not_pals and pals:
        return 'NO', None
    return 'YES', list(not_pals)[-1]



if __name__ == '__main__':
    T = int(input())

    for i in range(T):
        s = input()

        a, b = pal(s)
        if a:
            print(a)
        if b:
            print(b)
