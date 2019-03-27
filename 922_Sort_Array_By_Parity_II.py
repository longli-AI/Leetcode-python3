class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        not_even = []
        not_odd = []
        
        
        
        # get all not right elements
        for i in range(len(A)):
            if i%2 == 0:
                if A[i]%2 == 0:
                    pass
                else:
                    not_even.append(i)
                    pass
                pass
            if i%2 == 1:
                if A[i]%2 == 1:
                    pass
                else:
                    not_odd.append(i)
                    pass
                pass
            pass
        
        # swap them
        not_right = not_odd + not_even
        l = len(not_right)
        
        for i in range(int(l/2)):
            A[not_right[i]], A[not_right[l-i-1]] = A[not_right[l-i-1]], A[not_right[i]]
            pass
        return A    
'''
Runtime: 152 ms, faster than 48.17% of Python3 online submissions for Sort Array By Parity II.
Memory Usage: 15.4 MB, less than 5.49% of Python3 online submissions for Sort Array By Parity II.
'''           
