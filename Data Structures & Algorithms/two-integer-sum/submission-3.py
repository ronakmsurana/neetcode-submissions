class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a = set()
        for i in nums:
            if target - i in a:
                x = nums.index(target - i)
                return [x,x+1+nums[x+1:].index(i)]
            a.add(i)
        