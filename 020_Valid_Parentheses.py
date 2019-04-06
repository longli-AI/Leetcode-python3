class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        output = False
        while True:
            flag = 0
            if '()' in s:
                flag = 1
                s = s.replace('()','')
            if '[]' in s:
                flag = 1
                s = s.replace('[]','')
            if '{}' in s:
                flag = 1
                s = s.replace('{}','')
            if len(s) == 0:
                output = True
                break
            if flag == 0:
                if len(s)>0:
                    output = False
                break
        return output
'''
Runtime: 64 ms, faster than 9.18% of Python3 online submissions for Valid Parentheses.
'''

