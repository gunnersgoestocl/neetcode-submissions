class Solution:
    PAIR = {')': '(', ']': '[', '}': '{'}
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c in self.PAIR:  # c in key of self.PAIR
                if stack and stack[-1] == self.PAIR[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        if stack:
            return False
        return True
        # if not stack:
        #     return True
        # return False
