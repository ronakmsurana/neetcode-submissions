class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        a = 0
        n = len(numbers)
        b = n-1
        x = numbers
        while a<b:
            s = x[a] + x[b]
            if s == target:
                return [a+1,b+1]
            elif s > target:
                b-=1
            else:
                a+=1