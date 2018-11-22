class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        SD = dict()
        for s in S:
            if s in SD:
                SD[s]=SD[s]+1
            else:
                SD[s] = 1
        sum = 0
        for j in J:
            if j in SD:
                sum = sum + SD[j]   
        return sum
    
'''
Runtime: 48 ms, faster than 47.63% of Python3 online submissions for Jewels and Stones.
'''
