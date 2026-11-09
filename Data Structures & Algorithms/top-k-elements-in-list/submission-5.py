class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for i in nums:
            d[i] = d.setdefault(i,0) + 1
        n = {}
        for i,f in d.items():
            n.setdefault(f,[]).append(i)
        high = max(n.keys())
        ans = []
        for i in range(high,0,-1):
            if k<=0:
                return ans
            ans.extend(n.get(i,[]))
            k -= len(n.get(i,[]))
        return ans

        

        