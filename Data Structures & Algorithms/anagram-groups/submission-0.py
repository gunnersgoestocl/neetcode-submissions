class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = {}
        for s in strs:
            s_key = "".join(sorted(s))
            if ans.get(s_key) == None:
                ans[s_key] = [s]
            else:
                ans[s_key].append(s)
        return list(ans.values())