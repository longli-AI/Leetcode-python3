class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = [1,2]
        if n == 1 or n == 2:
            return n
        else:
            for i in range(n-2):
                result.append(result[-2] + result[-1])
            return result[-1]
        
'''
Runtime: 32 ms, faster than 100.00% of Python3 online submissions for Climbing Stairs.
'''