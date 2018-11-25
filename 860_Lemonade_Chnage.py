class Solution:
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        sum1 = 0
        sum2 = 0
        sum3 = 0
        
        output = True
        for bill in bills:
            if bill == 5:
                sum1 = sum1 + 1
            if bill == 10:
                if sum1 == 0:
                    output = False
                    break
                else:
                    sum1 = sum1 - 1
                    sum2 = sum2 + 1
            if bill == 20:
                if sum2 >= 1 and sum1 >=1:
                    sum2 = sum2 - 1
                    sum1 = sum1 - 1
                elif sum2 == 0 and sum1 >=3:
                    sum1 = sum1 - 3
                else:
                    output = False
                    break
        return output
    
'''
Runtime: 56 ms, faster than 58.27% of Python3 online submissions for Lemonade Change.
'''