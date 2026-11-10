class Solution:
    def largestRectangleArea(self, h: List[int]) -> int:
        n = len(h)
        stack=[]
        left, right = [0]*n,[0]*n
        for i in range(n):
            while stack and stack[-1][0]>h[i]:
                right[stack.pop()[1]] = (h[i],i)
            stack.append((h[i],i))
        while stack:
            high, ind = stack.pop()
            right[ind] = (high,ind)
        stack=[]
        for i in range(n-1,-1,-1):
            while stack and stack[-1][0]>h[i]:
                left[stack.pop()[1]] = (h[i],i)
            stack.append((h[i],i)) 
        while stack:
            high, ind = stack.pop()
            left[ind] = (high,ind)
        maxa = 0
        for i in range(n):
            lh,li = left[i]
            rh,ri = right[i]
            if li!=i:
                li = li+1
                lh = h[li]
            else:
                li = 0
            if ri!=i:
                ri = ri-1
                rh = h[ri]
            else:
                ri = n-1
            area = h[i]*(ri-li+1)
            maxa = max(maxa, area)

        return maxa
            