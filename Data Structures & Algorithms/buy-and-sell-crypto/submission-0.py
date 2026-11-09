class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        p = 0
        l = 0
        r = 1
        while(r<len(prices)):
            p = max(p,prices[r]-prices[l])
            if prices[l]>prices[r]:
                l=r
            r=r+1
        return p
                

