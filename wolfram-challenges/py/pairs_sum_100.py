# Problem: https://challenges.wolframcloud.com/challenge/pairs-that-sum-to-100


from typing import List, Tuple

def pairs_sum_target(numbers: List[int], target: int) -> List[Tuple[int,int]]:
    n = len(numbers)
    results = []

    for i in range(n):
        for j in range(i + 1, n):
            x, y = numbers[i],  numbers[j]
            k = x + y
            
            if k == target:
                results.append((x, y))
    return results

if __name__ == '__main__':
    numbers = [34, -65, -40, 12, 174, 44, -186, 169, -136, 153, -15, 127, 29, 15, -87, 191, 102, -3, 26, -175, 36, 21, 177, -135, -77, 138, 166, -140, -187, 156, -88, 100, 183, -81, -68, -18, 120, 37, -167, -104, -145, -59, 160, -105, -53, -120, 70, -46, 172, 22, 56, -134, -8, -174, -57, 39, 84, -50, 19, -106, -133, -161, -169, 171, 108, -45, 122, -55, 61, 25, 24, 14, -17, 135, 114, 188, -14, -7, -25, -61, 69, 52, -72, -125, 20, 149, -132, 199, -13, -170, 157, -4, -38, 168, 89, -124, 85, 8, 189, 196] 
    res = pairs_sum_target(numbers, 100)
    print(res)
