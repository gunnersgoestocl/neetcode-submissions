class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        result = merge_dict(nums)
        if result.get(target) == None:
            return 0
        else:
            return result[target]

def merge_dict(nums: List[int]) -> dict:
    if len(nums)==1:
        if nums[0] == 0:
            return { 0:2 }
        return { nums[0]:1, -nums[0]:1 }
    mid = len(nums)//2
    left_dict = merge_dict(nums[0:mid])
    right_dict = merge_dict(nums[mid:])
    # merge dicts
    new = {}
    for k in left_dict:
        for j in right_dict:
            cand_p = k+j
            if new.get(cand_p) == None:
                new[cand_p] = left_dict[k]*right_dict[j]
            else:
                new[cand_p] += left_dict[k]*right_dict[j]
            # cand_m = k-j
            # if new[cand_m] == None:
            #     new[cand_m] = left_dict[k]+right_dict[j]
            # else:
            #     new[cand_m] += left_dict[k]+right_dict[j]
    return new