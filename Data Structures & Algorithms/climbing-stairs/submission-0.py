class Solution:
    def climbStairs(self, n: int) -> int:
        n_cases = [1,1]
        for i in range(2, n+1):
            n_cases.append(n_cases[i-2]+n_cases[i-1])
        return n_cases[n]