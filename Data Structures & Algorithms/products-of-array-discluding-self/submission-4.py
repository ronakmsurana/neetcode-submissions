class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        zc =0 
        res = [0]*n
        zi =0 
        p = 1
        for i in range(n):
            if nums[i]==0:
                zc += 1
                zi = i  
            else:
                p *= nums[i]
        if zc >= 2:
            return res
        if zc == 1:
            res[zi] = p
            return res
        for i in range(n):
            res[i] = int(p/nums[i])
        return res

        