class Solution:
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        output = False
        if A == B:
            output = True
        else:
            if len(A) == len(B):
                for i in range(len(B)):
                    if A == B:
                        output = True
                        break
                    else:
                        B = B[1:] + B[0]
        return output
'''
Runtime: 32 ms, faster than 100.00% of Python3 online submissions for Rotate String.
''' 
