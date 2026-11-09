class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n=len(nums)
        l=0
        r=n-1
        while l<=r:
            m = (l+r)//2
            if nums[m] == target:
                return True
            if nums[m]>target:
                r = m-1
            else:
                l = m+1
        return False
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        l=0
        r=n-1
        while l<=r:
            m = (l+r)//2
            if matrix[m][0] <= target <= matrix[m][-1]:
                return self.search(matrix[m],target)
            if target < matrix[m][0]:
                r = m-1
            else:
                l = m+1
        return False