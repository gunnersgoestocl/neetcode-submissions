class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        d = {}
        for n in nums:
            if n not in d:
                d[n] = 1
            else:
                d[n] += 1
        # print(d)

        ans = []
        l = sorted(d.items())
        # two pointers from bottom
        a = 0
        b = 0
        while a < len(l) and l[a][0] <= 0:
            c = len(l)-1
            if l[a][1]==1:
                b = a + 1
            else:
                b = a
            while b <= c:

                cc = -l[a][0]-l[b][0]
                if cc < l[b][0]:
                    break
                while c >= b and l[c][0] > cc:
                    c -= 1
                if c >= b and l[c][0] == cc:
                    if b == c:
                        if a == b and l[a][1] < 3:
                            pass
                        elif l[b][1] < 2:
                            pass
                        else:
                            ans.append([l[a][0], l[b][0], l[c][0]])
                    else:
                        ans.append([l[a][0], l[b][0], l[c][0]])

                b += 1
            a += 1
        return ans