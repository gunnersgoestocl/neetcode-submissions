class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # (n+m-2)C(m-1)
        s = max(m-1, n-1)
        t = n+m-2
        return factorial(t, s)//factorial(t-s, 0)

def factorial(n: int, m: int)->int:
    # print(n, m)
    ans = 1
    for i in range(n,m,-1):
        ans *= i
    # print(ans)
    return ans