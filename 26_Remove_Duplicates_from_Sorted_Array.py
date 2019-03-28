class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        for i in range(len(nums)-1, 0, -1):
            if nums[i] == nums[i-1]:
                del nums[i]
                pass
            pass
        pass
    pass
'''
Runtime: 64 ms, faster than 64.35% of Python3 online submissions for Remove Duplicates from Sorted Array.
Memory Usage: 14.8 MB, less than 5.43% of Python3 online submissions for Remove Duplicates from Sorted Array.
'''
