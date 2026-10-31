def _find_min(left, right, nums) -> tuple[int, int]:
    if left == right:
        return left, right
    mid = (left + right) // 2
    if nums[mid] > nums[right]:
        return _find_min(mid+1, right, nums)
    else:
        return _find_min(left, mid, nums)

class Solution:
    def findMin(self, nums: List[int]) -> int:
        ans, _ = _find_min(0, len(nums)-1, nums)
        return nums[ans]