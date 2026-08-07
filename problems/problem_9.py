from collections import Counter
def find_anagrams(s: str, p: str) -> list[int]:
    """
    Given two strings s and p, return an array of all the start indices of p's 
    anagrams in s. You may return the answer in any order.

    Examples:
    Input: s = "cbaebabacd", p = "abc"
    Output: [0,6]
    Explanation:
    The substring with start index = 0 is "cba", which is an anagram of "abc".
    The substring with start index = 6 is "bac", which is an anagram of "abc".

    Input: s = "abab", p = "ab"
    Output: [0,1,2]
    Explanation:
    The substring with start index = 0 is "ab", which is an anagram of "ab".
    The substring with start index = 1 is "ba", which is an anagram of "ab".
    The substring with start index = 2 is "ab", which is an anagram of "ab".
    """
    ns, np = len(s), len(p)
    if ns < np:
        return []
    
    if np == 0:
        return []
        
    p_count = Counter(p)
    s_count = Counter(s[:np])
    res = []
    if p_count == s_count:
        res.append(0)
    
    # Buggy sliding window logic. The window only grows and never shrinks 
    # when the size exceeds len(p). Additionally, characters are never removed 
    # from s_count. Students must design and implement the correct sliding window 
    # map-updating bounds from scratch.
    for i in range(np, ns):

        s_count[s[i]] += 1

        s_count[s[i - np]] -= 1

        if s_count[s[i - np]] == 0:
            del s_count[s[i - np]]

        if s_count == p_count:
            res.append(i - np + 1)
    
            
    return res
