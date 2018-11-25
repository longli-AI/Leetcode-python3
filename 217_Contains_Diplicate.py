class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) != len(set(nums)):
            return True
        else:
            return False
'''
Runtime: 48 ms, faster than 79.64% of Python3 online submissions for Contains Duplicate.
'''
