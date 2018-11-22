class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        # [9,9,9] -> [1,0,0,0]
        
        count = 0
        
        new = ''
        for i in digits:
            new = new + str(i)
        
        new = int(new) + 1
        new = str(new)
        output = []
        for j in new:
            output.append(int(j))
        return output     
'''
Runtime: 40 ms, faster than 72.39% of Python3 online submissions for Plus One.
'''
