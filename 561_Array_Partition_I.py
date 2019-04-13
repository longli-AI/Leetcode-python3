class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        count = 0
        B = []
        for num in sorted(nums):
            if count % 2 == 0:
                B.append(num)
            count += 1
        return sum(B)
        
'''
Runtime: 120 ms, faster than 22.11% of Python3 online submissions for Array Partition I.
Memory Usage: 15.1 MB, less than 5.20% of Python3 online submissions for Array Partition I.
'''

