class Solution:
    def reverseBits(self, n: int) -> int:
        bit32_str = format(n, '32b')
        ans = 0
        for i,c in enumerate(bit32_str):
            if c == '1':
                ans += 1<<i
        return ans
        