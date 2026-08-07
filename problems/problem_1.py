def longest_substring(s: str) -> int:
    """
    Given a string s, find the length of the longest substring without repeating characters.

    Examples:
    Input: s = "abcabcbb"
    Output: 3
    Explanation: The answer is "abc", with the length of 3.

    Input: s = "bbbbb"
    Output: 1
    Explanation: The answer is "b", with the length of 1.

    Input: s = "pwwkew"
    Output: 3
    Explanation: The answer is "wke", with the length of 3.
    Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
    """
    char_set = set()
    l = 0
    res = 0
    
    for r in range(len(s)):
        while s[r] in char_set:
            char_set.remove(s[l])
            l += 1
        char_set.add(s[r])
        # Cheeky syntax error: trailing space after the backslash line continuation
        res = max(res, r - l + 1)
        
    return res
