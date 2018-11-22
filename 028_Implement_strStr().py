class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        output = 0
        if len(needle) == 0:
            output = 0
        else:
            if needle in haystack:
                output = haystack.find(needle)
            else:
                output = -1
        return output
'''
Runtime: 44 ms, faster than 58.04% of Python3 online submissions for Implement strStr().
'''
