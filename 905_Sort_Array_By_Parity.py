class Solution:
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        B = []
        C = []
        D = []
        for i in A:
            if i%2 == 0:
                B.append(i)
                pass
            else:
                C.append(i)
                pass
            pass
        D = B + C
        return D
        
'''
Runtime: 88 ms, faster than 55.08% of Python3 online submissions for Sort Array By Parity.
'''
