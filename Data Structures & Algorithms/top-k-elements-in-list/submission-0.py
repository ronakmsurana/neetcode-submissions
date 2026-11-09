class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for i in nums:
            d[i] = d.setdefault(i,0) + 1
        t = [(i,d[i]) for i in d.keys()]
        top = sorted(t,key = lambda x: x[1], reverse = True)[:k]
        return [i[0] for i in top]

        