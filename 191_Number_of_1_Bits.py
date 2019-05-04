class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        rtype = 0
        for i in list(bin(n)):
            if i == '1':
                rtype = rtype + 1
                pass
            pass
        return rtype
'''
Runtime: 24 ms, faster than 57.87% of Python online submissions for Number of 1 Bits.
Memory Usage: 11.7 MB, less than 5.10% of Python online submissions for Number of 1 Bits.

solution2:       
        return str(bin(n)[2:]).count('1')
'''
