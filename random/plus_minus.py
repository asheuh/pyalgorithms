def plus_minus(arr):
    # Write your code here
    seen = {'+': 0, '-': 0, '0': 0}
    n = len(arr)
    for item in arr:
        if item < 0:
            seen['-'] += 1
        elif item > 0:
            seen['+'] += 1
        else:
            seen['0'] += 1
            
    for it in seen:
        count = seen[it]
        ratio = count / n
        print(round(ratio, 6))

if __name__ == '__main__':
    arr = [-4, 3, -9, 0, 4, 1]
    plus_minus(arr)
