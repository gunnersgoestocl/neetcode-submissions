class Solution:
    def reverseBits(self, n: int) -> int:
        # Bit manipulation2
        ans = 0
        for i in range(32):
            bit = (n >> i) & 1
            ans += (bit << (31 - i))
        return ans