class Solution:
    def romanToInt(self, s: str) -> int:
        # create dict for all roman combination
        sum1 = 0
        ind = 0
        dict1 = {'I':1,'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}

        # split s in correct combination
        while ind < len(s) - 1:
            l, r = dict1[s[ind]], dict1[s[ind+1]]
            if l >= r:
                sum1 = sum1 + l
                ind = ind + 1
                pass
            else:
                sum1 = sum1 + (r - l)
                ind = ind + 2
                pass
            pass
        if ind == len(s) - 1:
            sum1 = sum1 + dict1[s[ind]]
            pass
        return sum1
            
'''
Runtime: 128 ms, faster than 71.19% of Python3 online submissions for Roman to Integer.
Memory Usage: 13.2 MB, less than 5.05% of Python3 online submissions for Roman to Integer.
'''
