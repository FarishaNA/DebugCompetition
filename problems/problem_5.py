def longest_consecutive(nums: list[int]) -> int:
    """
    Given an unsorted array of integers nums, return the length of the longest 
    consecutive elements sequence.

    You must write an algorithm that runs in O(n) time.

    Examples:
    Input: nums = [100,4,200,1,3,2]
    Output: 4
    Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. 
    Therefore its length is 4.

    Input: nums = [0,3,7,2,5,8,4,6,0,1]
    Output: 9
    """
    num_set = set(nums)
    longest_streak = 0
    current_streak = 0
    
    for num in num_set:
        if num - 1 not in num_set:
            current_streak = 1
            current_num = num
                
            while current_num + 1 in num_set:
                current_num += 1
                current_streak += 1
                
            longest_streak = max(longest_streak, current_streak)
            
    return longest_streak
