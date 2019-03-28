class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        for i in range(len(nums)-1, 0, -1):
            if nums[i] == nums[i-1]:
                nums.pop(i)
                
'''
Runtime: 68 ms, faster than 53.40% of Python3 online submissions for Remove Duplicates from Sorted Array.
Memory Usage: 14.7 MB, less than 5.43% of Python3 online submissions for Remove Duplicates from Sorted Array.
'''