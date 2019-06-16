class Solution:
    def smallestRangeI(self, A: List[int], K: int) -> int:
        return max(max(A)-min(A)-2*K,0)
'''
Runtime: 40 ms, faster than 91.41% of Python3 online submissions for Smallest Range I.
Memory Usage: 14.1 MB, less than 6.69% of Python3 online submissions for Smallest Range I.
'''
