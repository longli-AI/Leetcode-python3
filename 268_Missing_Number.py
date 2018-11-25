class Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        new = sorted(nums)
        low = 0
        high = len(new) - 1
        
        if new[high] == high:
            return len(new)

        while True:
            mid = int((low + high) /2)
            if new[mid] == mid:
                low = mid + 1
            if new[mid] > mid:
                high = mid
            if low >= high:
                return low
            
'''
Runtime: 76 ms, faster than 20.58% of Python3 online submissions for Missing Number.

Note:
binary sort
best way is to use n*(n+1)//2 - sum(nums)
'''
