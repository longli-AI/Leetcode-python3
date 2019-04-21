class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        flag = 0
        new_S = ''
        for s in S:
            if s == '(':
                if flag !=0:
                    new_S=new_S + s
                flag = flag + 1
            else:
                if flag != 1:
                    new_S=new_S + s
                flag = flag - 1
                pass
            pass
        return new_S
'''
Runtime: 40 ms, faster than 100.00% of Python3 online submissions for Remove Outermost Parentheses.
Memory Usage: 13.1 MB, less than 100.00% of Python3 online submissions for Remove Outermost Parentheses.
'''
