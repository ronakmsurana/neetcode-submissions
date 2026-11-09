class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []
        sans = []
        for i in range(n):
            a=set()
            for j in range(i+1,n):
                if -nums[i]-nums[j] in a:
                    x = [nums[i],nums[j],-nums[i]-nums[j]]
                    if set(x) not in sans:
                        ans.append(x)
                        sans.append(set(x))
                else:
                    a.add(nums[j])
        return ans
    