class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1, 1 # one step before, two step before
        for i in range(2, n+1):
            tmp = one
            one = one + two # next one step before is the sum of the last one step before and the last two step before
            two = tmp   # next two step before is the last one step before
        return one