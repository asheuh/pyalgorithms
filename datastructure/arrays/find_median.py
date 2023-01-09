def find_median_of_two_sorted_arrays(nums1, nums2):
    # Binary search
    # runtime = 175.4ms, memory usage = 14.2MB
    merged_array = [*nums1, *nums2]
    merged_array.sort()

    low = 0
    high = len(merged_array)

    while low < high:
        mid = (low + high) >> 1
        
        if high & 1:
            return merged_array[mid]
        return (merged_array[mid] + merged_array[mid - 1]) / 2

def find_median_of_two_sorted_arrays_optimized(nums1, nums2):
    l1 = len(nums1)
    l2 = len(nums2)
    to_search = nums1
    to_pad = nums2
    l = l1 + l2
    
    if l2 < l1:
        l1 = l2
        to_search = nums2
        to_pad = nums1

    low = 0
    high = l1
    
    while low < high:
        mid = (low + high) >> 1
        i = (l >> 1) - (mid + 1)
        j = mid + 1
        
        if to_pad[i - 1] <= to_search[j] and to_search[mid] <= to_pad[i]:
            if l & 1:
                return min(to_search[j], to_pad[i])
            return (max(to_search[j], to_search[j - 1]) + min(to_pad[i - 1], to_pad[i])) / 2
        low = mid + 1

if __name__ == '__main__':
    nums1 =  [1,2]
    nums2 = [3, 4]
    print(find_median_of_two_sorted_arrays_optimized(nums1, nums2))

