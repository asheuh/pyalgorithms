# Problem: https://challenges.wolframcloud.com/challenge/pairingfunction
# Resources: http://szudzik.com/ElegantPairing.pdf
#          : https://en.wikipedia.org/wiki/Pairing_function
import math


def pairing_function(x: int, y: int):
    # Using Cantor pairing function
    # (1/2 * ((x + y + 1)(x + y))) + y: Solve quadratically
    # Pair[x, y] := (x**2 + x + 2xy + 3y + y**2) // 2
    return (x**2 + x + (2 * x * y) + (3 * y) + y**2) // 2

def inverting_pairing_function(z: int):
    # geting pairs of coordinate from a number
    # w = x + y
    # z =  (1/2 * ((x + y + 1)(x + y))) + y
    # t = 1/2 * w(w+1) == (w**2 + w) / 2
    w = math.floor((math.sqrt(8*z + 1) - 1) / 2)
    t = (w**2 + w) // 2
    # z = t + y
    y = z - t
    # w = x + y
    x = w - y
    return (x, y)

def all_pfs(l: list):
    results = []
    for x, y in l:
        z = pairing_function(x, y)
        results.append(z)
    return results

if __name__ == '__main__':
    x, y = 0, 4
    res = pairing_function(x, y)
    r = inverting_pairing_function(res)
    al = all_pfs([(0, 4), (1, 3), (2, 2), (3, 1), (4, 0)])
    print(res, r, al)
