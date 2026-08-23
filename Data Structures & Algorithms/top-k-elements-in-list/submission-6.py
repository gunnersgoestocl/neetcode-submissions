class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = {}

        for n in nums:
            freqs[n] = freqs.get(n, 0) + 1
        
        freqs2 = {}
        for n, freq in freqs.items():
            if freq not in freqs2:
                freqs2[freq] = []
            freqs2[freq].append(n)
        # print(freqs2)
        ans = []
        # maximum frequency is len(nums)
        for f in range(len(nums), -1, -1):
            if len(freqs2.get(f, [])) > 0:
                ans += freqs2[f]
                if len(ans) >= k:
                    return ans