def _rob(start, nums, cache) -> int:
    if start >= len(nums):
        return 0
    if cache[start] != 0:
        return cache[start]
    cache[start] = nums[start] + max(_rob(start+2, nums, cache), _rob(start+3, nums, cache))
    return cache[start]

class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = [0 for _ in range(len(nums))]
        return max(_rob(0, nums, cache), _rob(1, nums, cache))