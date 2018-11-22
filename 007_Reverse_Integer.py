class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        new = str(x)
        if '-' in new:
            new = new.replace('-','')
            new = '-' + new[::-1]
        else:
            new = new[::-1]
        new = int(new)
        if new < - 2**31 or new > 2**31 -1:
            new = 0
        return new
'''
Runtime: 72 ms, faster than 43.79% of Python3 online submissions for Reverse Integer.
'''
