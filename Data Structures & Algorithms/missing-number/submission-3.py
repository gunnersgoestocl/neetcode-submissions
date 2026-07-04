class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # refsum = 0
        # getsum = 0
        # for i, n in enumerate(nums):
        #     refsum += i
        #     getsum += n
        # refsum += len(nums)
        # return refsum - getsum
        res = len(nums)
        for i, n in enumerate(nums):
            res += i - n
        return res
        