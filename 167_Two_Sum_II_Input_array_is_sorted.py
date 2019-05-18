class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l,r = 0,len(numbers)-1
    
        while l<=r:
            if numbers[l] +numbers[r] == target:
                return [l+1,r+1]
            if numbers[l] +numbers[r] < target:
                l += 1
            if numbers[l] +numbers[r] > target:
                r -= 1
        return [l+1,r+1]
'''
Runtime: 44 ms, faster than 49.27% of Python3 online submissions for Two Sum II - Input array is sorted.
Memory Usage: 13.8 MB, less than 5.14% of Python3 online submissions for Two Sum II - Input array is sorted.
'''




class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        l = 0
        r = 0

        for i in range(n-1,-1,-1):
            r = i
            left = target - numbers[i]
            if left in numbers:
                l = numbers.index(left)
                if r != l:
                    break
        return [l+1,r+1]

'''
Runtime: 2192 ms, faster than 7.56% of Python3 online submissions for Two Sum II - Input array is sorted.
Memory Usage: 13.7 MB, less than 5.14% of Python3 online submissions for Two Sum II - Input array is sorted.
'''




