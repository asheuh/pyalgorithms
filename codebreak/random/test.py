import sys
from time import sleep

def solve(nums, target):
    """
    0. the is where the max and the min value lie
    1. the first index to the pivot is in ascending order
    2. the pivot to the last index is in ascending order
    3. all the values for the pivot to the last value are less than 
       all the the values from the pivot to the beginning value
    """
    n = len(nums)
    low = 0
    high = n

    while low < high:
        mid = (low + high) >> 1
        value = nums[mid]

        if value < target:
            k = mid + 1

            if k < n and nums[k] < value:
                break

            if target > nums[-1] and value < nums[0]:
                high = mid
                continue

            low = mid + 1
        elif value > target:
            if target < nums[0] and nums[-1] < value:
                low = mid + 1
            else:
                high = mid
        else:
            return mid
    return -1


def find_min(nums):
    """
    find pivot: pivot is where the array is rotated from
    note that the pivot:
        has it's values to the left all greater than values to the right
    """
    n = len(nums)
    low = 0
    high = n

    while low < high:
        mid = (low + high) >> 1
        k = nums[mid]
        j = mid + 1

        if nums[-1] > nums[0]:
            return nums[0]

        if j < n:
            m = nums[j]
            key = m - k

            if key > 0:
                if nums[0] < k:
                    low = mid
                else:
                    high = mid
            else:
                return nums[j]
        else:
            return k 


def solve_portion(k):
    e = 1
    w = 0
    h = 100 - k

    while 1:
        r = (e / (e + w)) * 100
        n = (w / (e + w)) * 100

        if (r == k) or (n == h):
            break

        if r < k:
            e += 1
        elif r > k:
            w += 1
        
    return e + w


def solve_done(arr):
    team1 = arr[:2]
    team2 = arr[2:]

    lossers = [min(team1), min(team2)]
    winners = [max(team1), max(team2)]

    comp = max(lossers)

    for score in winners:
        if score < comp:
            return 'NO'

    return 'YES'


def gcd(x, y):
    if x <= 0:
        return y

    if x == y:
        return x

    while 1:
        r = y % x

        if r == 0:
            return x

        y = x
        x = r


def solve(arr, n):
    count_good = 0

    for i in range(n):
        for j in range(i + 1, n):
            a, b = arr[j], arr[i]
            x, y = arr[i], arr[j]

            g = gcd(x, 2 * y)
            g2 = gcd(a, 2 * b)
            
            if g > 1 or g2 > 1:
                count_good += 1

    return count_good

if __name__ == '__main__':
    input = lambda: sys.stdin.readline().rstrip()
    T = int(input())

    for _ in range(T):
        n = int(input())
        arr = list(map(int, input().split()))
        r = solve(arr, n)
        print(r)
