from pyalgorithms.combinatorial.permutations.lexcographic import lexico_permutations_fast

def lexicographic_permutations(s):
    perms = lexico_permutations_fast(s)
    return perms


if __name__ == '__main__':
    s = '0123456789'
    res = list(lexicographic_permutations(s))
    print(res[999999])
