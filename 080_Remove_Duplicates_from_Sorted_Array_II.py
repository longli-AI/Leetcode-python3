class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        for i in range(len(nums)-1,1,-1):
            if nums[i] == nums[i-1]:
                if nums[i-1] == nums[i-2]:
                    del nums[i]
                    pass
                pass
            pass
        return len(nums)
'''
Runtime: 48 ms, faster than 93.77% of Python3 online submissions for Remove Duplicates from Sorted Array II.
Memory Usage: 13.2 MB, less than 5.43% of Python3 online submissions for Remove Duplicates from Sorted Array II.
'''
