class Solution:
    def reverseBits(self, n: int) -> int:
        bit32_str = format(n, '32b')
        ans = 0
        # reverse32_str = format(0, '32b')
        for i,c in enumerate(bit32_str):
        #     reverse32_str[31-i] = c
        # return int(reverse32_str, 2)
            if c == '1':
                ans += 1<<i
        return ans
        