class Solution:
    def fib(self, N: int) -> int:
        if N == 0 or N == 1:
            return N
        else:
            return self.fib(N-1)+self.fib(N-2)
'''
Runtime: 1140 ms, faster than 18.60% of Python3 online submissions for Fibonacci Number.
Memory Usage: 13.1 MB, less than 51.81% of Python3 online submissions for Fibonacci Number.
'''
