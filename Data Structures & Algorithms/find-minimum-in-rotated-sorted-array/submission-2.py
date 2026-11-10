class Solution:
    def findMin(self, nums: List[int]) -> int:
        n=len(nums)
        l=0
        r=n-1
        while l<=r:
            m = (l+r)//2
            a = nums[l]
            b = nums[m]
            c = nums[r]
            print(a,b,c)
            if a<=b<=c:
                return a
            if a>=b>=c:
                return c
            if a < b and b>c:
                l = m+1
            elif a > b < c:
                r = m
            else:
                r = m-1
        return -1