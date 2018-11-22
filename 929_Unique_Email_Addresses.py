class Solution:
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        new_list=[]
        for i in emails:
            x = i.find('@')
            new_i = i[x+1:]
            if new_i in new_list:
                pass
            else:
                new_list.append(new_i)
        return len(new_list)
    

'''
Runtime: 40 ms, faster than 100.00% of Python3 online submissions for Unique Email Addresses.
'''
