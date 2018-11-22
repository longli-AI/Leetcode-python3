class Solution:
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        output = False
        countL = moves.count('L') 
        countR = moves.count('R') 
        countD = moves.count('D')
        countU = moves.count('U')
        if countL == countR and countD == countU:
            output = True
            pass
        return output        
'''
Runtime: 56 ms, faster than 74.59% of Python3 online submissions for Robot Return to Origin.
'''