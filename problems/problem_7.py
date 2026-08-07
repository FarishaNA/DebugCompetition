def subarray_sum(nums: list[int], k: int) -> int:
    """
    Given an array of integers nums and an integer k, return the total number of 
    subarrays whose sum equals to k.

    A subarray is a contiguous non-empty sequence of elements within an array.

    Examples:
    Input: nums = [1,1,1], k = 2
    Output: 2

    Input: nums = [1,2,3], k = 3
    Output: 2
    """
    count = 0
    curr_sum = 0
    prefix_sums = {0:1}
    
    for num in nums:
        curr_sum += num
        if curr_sum - k in prefix_sums:
            count += prefix_sums[curr_sum - k]
        prefix_sums[curr_sum] = prefix_sums.get(curr_sum, 0) + 1
        
    return count
