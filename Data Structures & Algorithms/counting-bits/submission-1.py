class Solution:
    def countBits(self, n: int) -> List[int]:
        p2 = 1
        while p2 < n:
            p2 *= 2
        visited = [False for _ in range(n+1)]
        ans = [0 for _ in range(n+1)]
        def _countBits(k: int):
            if visited[k]:
                return
            visited[k] = True
            if k == 1:
                ans[1] = 1
                return
            _countBits(k//2)
            if k % 2 == 0:
                ans[k] = ans[k//2]
            else:
                ans[k] = ans[k//2] + 1
            # print(k, k//2, visited, ans)
        for i in range(1, n+1):
            _countBits(i)
        return ans
