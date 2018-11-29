class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = len(nums)
        new = sorted(nums)
        return new[int((a-1)/2)]
'''
Runtime: 56 ms, faster than 67.31% of Python3 online submissions for Majority Element.
'''
