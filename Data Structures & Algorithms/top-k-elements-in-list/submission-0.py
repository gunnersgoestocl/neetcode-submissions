import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}

        for n in nums:
            if n not in d:
                d[n] = 0
            d[n] += 1
        
        sorted_items = sorted(d.items(), key=lambda x: -x[1])
        ans = [sorted_items[i][0] for i in range(k)]
        return ans
