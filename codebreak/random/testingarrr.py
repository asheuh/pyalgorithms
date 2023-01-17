def minSumOfLengths(arr, target):
    # dp = [0, 0, 0, 0, 0]
    prefix, dp = {0: -1}, [0]*len(arr)  # dp[i], min len of target subarray until i
    result = min_len = float("inf")
    accu = 0
    for right in range(len(arr)): 
        accu += arr[right] # accu if right = 0 = 3
        print(accu, prefix, dp, arr, min_len)
        prefix[accu] = right # {3: 0}
        # Prefix stores the sum of subarrays
        if accu-target in prefix:
            left = prefix[accu-target]
            min_len = min(min_len, right-left)
            if left != -1:
                result = min(result, dp[left] + (right-left))
        dp[right] = min_len

    print(dp, result)
    return result if result != float("inf") else -1

# manually break into subs
# keep a record of the sum of subs e.g prefix[stores the sum and locations of sub indices]
# keep sum variable to add to prefix record


test = [3,2,2,4,3]
minSumOfLengths(test, 3)
# sub = [[3], [3, 2], [3, 2, 2], [3, 2, 2, 4], [3, 2, 2, 4, 3], [2], [2, 2], [2, 2, 4], [2, 2, 4, 3], [2], [2, 4], [2, 4, 3], [4], [4, 3], [3]]
