class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0
        prev = 0
        cwater = 0
        prev_index = 0
        for i in range(len(height)):
            if height[i] >= prev:
                water += cwater
                prev = height[i]
                cwater = 0
                prev_index = i
            else:
                cwater += prev - height[i]
        prev = 0
        cwater = 0
        for i in range(len(height)-1,prev_index-1,-1):
            if height[i] >= prev:
                water += cwater
                prev = height[i]
                cwater = 0
                prev_index = i
            else:
                cwater += prev - height[i]
        return water