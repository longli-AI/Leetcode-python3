class Solution:
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        a = int(len(s) / (2*k))
        check_list = []
        if a > 0:
            for i in range(a):
                check_list.append(s[2*i*k:2*i*k+2*k])
        check_list.append(s[2*a*k:])

        output = ''
        for j in check_list:
            if len(j) >= 2*k:
                tmp = j[0:k]
                tmp = tmp[::-1]
                j = tmp + j[k:2*k]
            elif len(j) >= k and len(j) < 2*k:
                tmp = j[0:k]
                tmp = tmp[::-1]
                j = tmp + j[k:]
            else:
                j = j[::-1]
            output = output + j
        return output
'''
Runtime: 36 ms, faster than 95.52% of Python3 online submissions for Reverse String II.
'''
