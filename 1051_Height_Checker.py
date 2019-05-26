class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        l = len(heights)
        sorted_heights = sorted(heights)
        output = 0
        for i in range(len(heights)):
            if heights[i] != sorted_heights[i]:
                output += 1
        return output
'''
Runtime: 36 ms, faster than 100.00% of Python3 online submissions for Height Checker.
Memory Usage: 13.3 MB, less than 100.00% of Python3 online submissions for Height Checker.
'''
