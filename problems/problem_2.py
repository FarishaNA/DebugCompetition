def max_area(height: list[int]) -> int:
    """
    Given n non-negative integers height_1, height_2, ..., height_n, where each represents 
    a point at coordinate (i, height_i). n vertical lines are drawn such that the two endpoints 
    of the line i is at (i, height_i) and (i, 0). Find two lines that together with the x-axis 
    forms a container, such that the container contains the most water.

    Return the maximum amount of water a container can store.

    Examples:
    Input: height = [1,8,6,2,5,4,8,3,7]
    Output: 49
    Explanation: The vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, 
    the max area of water the container can contain is 49.

    Input: height = [1,1]
    Output: 1
    """
    l, r = 0, len(height) - 1
    res = 0
    
    while l < r:
        area = (r - l) * min(height[l], height[r])
        res = max(res, area)
        
        if height[l] < height[r]:
            l += 1
        else:
            r -= 1
            
    return res
