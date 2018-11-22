class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        output = False
        if x < 0:
            output = False
        else:
            new = str(x)[::-1]
            if x == int(new):
                output = True
        return output

'''
Runtime: 264 ms, faster than 90.67% of Python3 online submissions for Palindrome Number.
'''
