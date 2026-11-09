class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        ans = []

        nums.sort()

        for index, num in enumerate(nums):
            if(index > 0 and num == nums[index - 1]):
                continue

            left = index + 1
            right = len(nums) - 1

            while left < right:
                val = num + nums[left] + nums[right]

                if val > 0:
                    right -= 1
                
                elif val < 0:
                    left += 1
                
                elif val == 0:
                    ans.append([num, nums[left], nums[right]])
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                          left += 1
                
        return ans
