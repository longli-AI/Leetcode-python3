class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace('.','[.]')
'''
Runtime: 28 ms, faster than 95.72% of Python3 online submissions for Defanging an IP Address.
Memory Usage: 13.3 MB, less than 100.00% of Python3 online submissions for Defanging an IP Address.
'''