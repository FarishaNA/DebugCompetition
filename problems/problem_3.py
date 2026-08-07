def three_sum(nums: list[int]) -> list[list[int]]:
    """
    Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] 
    such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

    Notice that the solution set must not contain duplicate triplets.

    Examples:
    Input: nums = [-1,0,1,2,-1,-4]
    Output: [[-1,-1,2],[-1,0,1]]
    Explanation: 
    nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
    nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
    nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
    The distinct triplets are [-1,0,1] and [-1,-1,2].

    Input: nums = []
    Output: []
    """
    res = []
    nums.sort()
    
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        target = -nums[i]
        l, r = i + 1, len(nums) - 1

        while l < r:
            s = nums[l] + nums[r]

            if s == target:
                res.append([nums[i], nums[l], nums[r]])

                low = nums[l]
                while l < r and nums[l] == low:
                    l += 1

                high = nums[r]
                while l < r and nums[r] == high:
                    r -= 1

            elif s > target:
                r -= 1

            else:
                l += 1
            
            
    return res
