class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        sum1 = 0
        if len(a) > 1:
            for i in range(len(a)):
                sum1 = sum1 + int(a[i])*(2**(len(a)-1-i))
        else:
            sum1 = int(a)
        sum2 = 0
        if len(b) > 1:
            for j in range(len(b)):
                sum2 = sum2 + int(b[j])*(2**(len(b)-1-j))
        else:
            sum2 = int(b)        
            
        sum3 = sum1 + sum2
        output = str(bin(sum3)).replace('0b','')
        return output
    
'''
Runtime: 52 ms, faster than 49.20% of Python3 online submissions for Add Binary.
'''
