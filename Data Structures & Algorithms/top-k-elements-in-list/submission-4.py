class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = {}
        topk = []

        for n in nums:
            if n not in freqs:
                freqs[n] = 0
            freqs[n] += 1

        for it in freqs.items():
            heapq.heappush(topk, (it[1], it[0]))
            if len(topk) > k:
                heapq.heappop(topk)
        return [it[1] for it in topk] 