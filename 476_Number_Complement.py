class Solution:
    def findComplement(self, num: int) -> int:
        temp = bin(num).replace('0b','')
        output = ['0b']
        for i in temp:
            if i == '0':
                output.append('1')
            else:
                output.append('0')
        return int(''.join(output),2)
'''
Runtime: 36 ms, faster than 84.85% of Python3 online submissions for Number Complement.
Memory Usage: 13.2 MB, less than 38.90% of Python3 online submissions for Number Complement.
'''



'''
        return int((''.join(bin(num)))[2::].replace('0', '2').replace('1','0').replace('2','1'), 2)
'''