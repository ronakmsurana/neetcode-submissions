class Solution:
    def dailyTemperatures(self, t: List[int]) -> List[int]:
        n= len(t)
        ans = [0]*n
        a = []
        for i in range(n):
            while a and a[-1][1] < t[i]:
                index = a.pop()[0]
                ans[index] = i - index
            a.append((i,t[i]))
        return ans
