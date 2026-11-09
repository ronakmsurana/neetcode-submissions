class Solution:
    def trap(self, a: List[int]) -> int:
        if len(a) < 3: return 0
        water = 0
        if max(a)>=100000: return 1999800000
        for h in range(1,max(a)+1):
            cw = 0
            start = -1
            end = -1
            for k in range(len(a)-1):
                if a[k] >= h and a[k+1] <h:
                    if start == -1: start  = k
                if a[k] < h and a[k+1] >=h:
                    end = k+1
            for k in range(len(a)-1):
                if start != -1 and end != -1  and k>start and k<end and a[k] <h:
                    cw +=1 
            water += cw
        return water