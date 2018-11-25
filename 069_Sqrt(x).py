class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        low = 0
        high = x
        
        while True:
            mid = int((low + high) / 2)
            if mid*mid == x:
                return mid
            if mid*mid < x:
                if (mid+1)*(mid+1) > x:
                    return mid
                else:
                    low = mid + 1
            if mid*mid > x:
                high = mid - 1
'''
Runtime: 64 ms, faster than 68.03% of Python3 online submissions for Sqrt(x).

Note:
binary search
'''
