class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        # m x n matrix to n x m
        
        # calculate new row number
        new_n = len(A[0])
        
        # create empty list for new row
        AT = []
        for i in range(new_n):
            AT.append([])
        
        # push num in new row
        for row in A:
            # old column m will be reset
            m = 0 
            for i in row:
                AT[m].append(i)
                m = m + 1
        return AT      
'''
Runtime: 64 ms, faster than 59.80% of Python3 online submissions for Transpose Matrix.
Memory Usage: 13.7 MB, less than 5.45% of Python3 online submissions for Transpose Matrix.
'''