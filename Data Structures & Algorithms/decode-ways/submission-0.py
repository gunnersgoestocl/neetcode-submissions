class Solution:
    def numDecodings(self, s: str) -> int:
        a = [0 for _ in range(len(s)+1)]
        a[len(s)] = 1
        if int(s[len(s)-1]) != 0:
            a[len(s)-1] = 1
        for i in range(len(s)-2, -1, -1):
            # take
            nn = int(s[i])
            if nn > 0:
                a[i] += a[i+1]
                # not take
                n = int(s[i:i+2])
                if n > 0 and n < 27:
                    a[i] += a[i+2]
        return a[0]