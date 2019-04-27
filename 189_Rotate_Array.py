class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        nums[:] = nums[-k:] + nums[0:-k]
'''
Runtime: 52 ms, faster than 82.36% of Python3 online submissions for Rotate Array.
Memory Usage: 13.5 MB, less than 5.04% of Python3 online submissions for Rotate Array.
'''
