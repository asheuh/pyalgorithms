"""
Imports
"""


def straight_insertion_sort(_a: list):
    """
    The simplest insertion sort is the most obvious one
    """
    _n = len(_a)

    for j in range(1, _n):
        i = j - 1
        k = _a[j]
        _r = _a[j]

        while i >= 0 and k < _a[i]:
            _a[i + 1] = _a[i]
            i = i - 1

        _a[i + 1] = _r
    return _a

def isort(array):
    n = len(array)
    i = 0
    j = 1
    is_sorted = True

    while 1:
        x = array[i]
        y = array[j]
        
        if x > y:
            array[i] = y
            array[j] = x
            is_sorted = False

        i += 1
        j += 1
        if j >= n:
            i = 0
            j = 1
            if is_sorted:
                break
    return array


if __name__ == "__main__":
    A = [
        23, 128, 41, 1, 32, 3, 0, 93, 23, 42, 54, 12, 31, 14, 5, 87, 41, 10,
        11, 9, 7, 2
    ]
    RESULT = isort(A)

    print(RESULT)
