class Solution:
    def diStringMatch(self, S: str) -> List[int]:
        l = len(S)
        r = 0
        output = []
        for s in S:
            if s == 'I':
                output.append(r)
                r = r + 1
            else:
                output.append(l)
                l = l - 1
        output.append(l)
        return output
'''
Runtime: 92 ms, faster than 73.89% of Python3 online submissions for DI String Match.
Memory Usage: 14.3 MB, less than 43.64% of Python3 online submissions for DI String Match.
'''
