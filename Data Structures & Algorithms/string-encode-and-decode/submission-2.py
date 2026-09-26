class Solution:

    def encode(self, strs: List[str]) -> str:
        code = ""
        for s in strs:
            l = len(s)
            code += str(l) + '#' + s
        return code
    def decode(self, s: str) -> List[str]:
        ans = []
        head = 0
        cur = 0
        while cur < len(s):
            if s[cur] == '#':
                l = int(s[head:cur])
                head = cur + l + 1
                if l == 0:
                    ans.append("")
                else:
                    ans.append(s[cur+1:head])
                cur = head
            else:
                cur += 1
        return ans

