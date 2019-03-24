class Solution:
    def romanToInt(self, s: str) -> int:
        # create dict for all roman combination
        dict1 = {'I':1,'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000,'IV' :4, 'IX':9,'XL':40, 'XC':90,'CD':400,'CM':900}

        # split s in correct combination
        l = len(s)
        new_list = list()
        i = 0
        while i < l:
            if i + 2 <= l:
                if s[i:i+2] in dict1.keys():
                    new_list.append(s[i:i+2])
                    i = i + 2
                    pass
                else:
                    new_list.append(s[i])
                    i = i + 1
                    pass
                pass
            if i + 1 == l:
                new_list.append(s[i])
                i = i + 1
                pass
            pass
        
        
        # sum
        sum = 0 
        for x in new_list:
            sum = sum + dict1[x]
            pass
        return sum
    
'''
Runtime: 140 ms, faster than 37.57% of Python3 online submissions for Roman to Integer.
Memory Usage: 13.3 MB, less than 5.05% of Python3 online submissions for Roman to Integer.
'''
