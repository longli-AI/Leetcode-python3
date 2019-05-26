class Solution:
    def fib(self, N: int) -> int:
        f = [0, 1]
        while len(f) < N+1:
            f.append(f[-1] + f[-2])
        return f[N]
'''
Runtime: 32 ms, faster than 96.54% of Python3 online submissions for Fibonacci Number.
Memory Usage: 13.3 MB, less than 7.44% of Python3 online submissions for Fibonacci Number.
'''