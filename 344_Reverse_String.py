class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l = len(s)
        i = 0
        
        for i in range(int(l/2)):
            s[i], s[l-i-1] = s[l-i-1], s[i]
            pass
        pass

'''
Runtime: 168 ms, faster than 61.35% of Python3 online submissions for Reverse String.
Memory Usage: 17.6 MB, less than 11.53% of Python3 online submissions for Reverse String.
'''
