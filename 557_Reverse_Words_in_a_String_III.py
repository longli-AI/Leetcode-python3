class Solution:
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        list_ = s.split(' ')
        output = []
        for i in list_:
            output.append(i[::-1])
            pass
        return ' '.join(output)

'''
Runtime: 44 ms, faster than 63.12% of Python3 online submissions for Reverse Words in a String III.
'''
