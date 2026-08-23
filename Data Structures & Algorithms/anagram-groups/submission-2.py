class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = {}
        for s in strs:
            k = [0] * 26
            for c in s:
                k[ord(c)-ord('a')]+=1

            k = tuple(k)
            if k not in ans:
                ans[k] = []
            ans[k].append(s)
        return list(ans.values())