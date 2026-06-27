class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num_sets = set()
        for num in nums:
            if num in num_sets:
                return True
            num_sets.add(num)
        return False

        