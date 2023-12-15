def gray_binary_code_generation(a):
    n = len(a)
    k = n - 1
    x = ['0'] * k
    f = [i for i in range(n)]

    while k:
        c = ''.join(x)
        m = '0' + c
        p = '1' + c
        print(m)
        print(p)

        j = f[0]
        f[0] = 0

        if j >= k:
            break

        f[j] = f[j + 1]
        f[j + 1] = j + 1
        x[j] = str(1 - int(x[j]))


if __name__ == '__main__':
    test = [0,0,0,0,0]
    gray_binary_code_generation(test)
