class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Hash Map (Two Pass)
        idx_dict = {}
        for i, n in enumerate(nums):
            if idx_dict.get(n) == None:
                idx_dict[n] = [i]
            else:
                idx_dict[n].append(i) 
        for n in nums:
            value_list = idx_dict.get(target-n, [])
            if len(value_list) == 1 and idx_dict[n][0] != value_list[0]:
                value1 = idx_dict[n][0]
                value2 = value_list[0]
                return [min(value1, value2), max(value1, value2)]
            elif len(value_list) > 1:
                return value_list
        return []
        
        