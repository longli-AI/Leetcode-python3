class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            num = target - nums[i]
            if num in nums:
                j = nums.index(num)
                if i !=j:
                    return [i,j]
'''
Runtime: 1200 ms, faster than 26.50% of Python3 online submissions for Two Sum.
'''