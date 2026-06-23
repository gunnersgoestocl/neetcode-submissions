class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_char = {}
        t_char = {}
        for i in range(len(s)):
            ss = s[i]
            tt = t[i]
            if s_char.get(ss) == None:
                s_char[ss] = 1
            else:
                s_char[ss] += 1
            if t_char.get(tt) == None:
                t_char[tt] = 1
            else:
                t_char[tt] += 1
        return s_char == t_char
            