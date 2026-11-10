import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def check(speed):
            ans = 0
            for i in piles:
                    ans += math.ceil(i/speed)
                    if ans > h:
                        break
            return ans<=h
        n = len(piles)
        r = max(piles)
        l = 1
        if h == n:
            return r
        
        while l<=r:
            m = (l+r)//2
            cur = check(m)
            if cur:
                if (not m-1) or not check(m-1):
                    return m
                else:
                    r = m-1
            else:
                l = m+1
        return r