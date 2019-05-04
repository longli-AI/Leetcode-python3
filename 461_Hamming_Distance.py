class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        y_list = list(bin(y))
        x_list = list(bin(x))

        y_len = len(y_list) 
        x_len = len(x_list)
        if y_len >= x_len:
            for i in range(y_len-x_len):
                x_list.insert(2,'0')
        else:
            for i in range(x_len-y_len):
                y_list.insert(2,'0')

        flag = 0

        for i in range(len(y_list)):
            if y_list[i] != x_list[i]:
                flag = flag + 1

        return flag
    
'''
Runtime: 36 ms, faster than 89.32% of Python3 online submissions for Hamming Distance.
Memory Usage: 12.9 MB, less than 5.84% of Python3 online submissions for Hamming Distance.
'''
