class Solution:
    LEFT_ITEM = ['(', '[', '{']
    RIGHT_ITEM =  [')', ']', '}']
    def isValid(self, s: str) -> bool:
        stack = []
        for c in list(s):
            if c in self.LEFT_ITEM:
                l = self.LEFT_ITEM.index(c)
                stack.append(l)
            else:
                r = self.RIGHT_ITEM.index(c)
                if len(stack) > 0 and r == stack.pop():
                    continue
                else:
                    return False
            print(stack)
        if len(stack) > 0:
            return False
        return True

        