class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        while s.endswith(' '):
            s = s[0:-1:1]

        a = s.split(' ')
        output = len(a[-1])

        return output
'''
Runtime: 48 ms, faster than 24.79% of Python3 online submissions for Length of Last Word.
'''
