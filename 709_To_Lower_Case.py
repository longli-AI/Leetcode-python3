class Solution:
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        #return str.lower()  # beat 94%
        x = ''
        for i in str:
            if ord(i) >= 65 and ord(i) <= 90:
                j = chr(ord(i)+32)
                pass
            else:
                j = i
            x = x + j
        return x
'''
Runtime: 48 ms, faster than 16.22% of Python3 online submissions for To Lower Case.
'''