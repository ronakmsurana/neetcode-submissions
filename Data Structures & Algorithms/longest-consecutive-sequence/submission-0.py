class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        h = 0
        for i in nums:
            if i-1 not in s:
                l = 1
                while i + l in s:
                    l+=1
                h = max(h,l)
        return h