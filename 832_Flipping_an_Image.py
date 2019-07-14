class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        B = []
        for a in A:
            b = a[::-1]
            c = []
            for i in b:
                new_i = 1 - i
                c.append(new_i)
                pass
            B.append(c)
            pass
        return B
'''
Runtime: 40 ms, faster than 98.02% of Python3 online submissions for Flipping an Image.
Memory Usage: 13.1 MB, less than 67.61% of Python3 online submissions for Flipping an Image.
'''
