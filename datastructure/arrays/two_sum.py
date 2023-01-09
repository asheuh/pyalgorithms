def two_sum(nums, target):
    # while loop
    # runtime = 116.8ms, memory usage = 14.9MB
    i = 0
    j = 0
    c = 2
    l = len(nums)

    while True:
        a = nums[i]
        b = nums[j]

        if (a + b) == target:
            return [i, j]

        i += 1
        j += 1

        if j >= l:
            i = 0
            j = c
            c += 1

def two_sum_optimized_while(nums, target):
    # while loop
    # runtime = 120.4ms, memory usage = 15.2MB
    maps = {}
    i = 0
    while i < len(nums):
        num = nums[i]

        try:
            index = maps[target - num]
            return [index, i]
        except Exception as e:
            maps[num] = i
        i += 1

def two_sum_optimized_for(nums, target):
    # for loop
    # runtime = 107.1ms, memory usage = 15.2MB
    maps = {}
    for i, num in enumerate(nums):
        try:
            index = maps[target-num]
            return [index, i]
        except Exception as e:
            maps[num] = i

if __name__ == '__main__':
    nums = [-3,4,3,90]
    t = 0
    print(two_sum_optimized_for(nums, t))
