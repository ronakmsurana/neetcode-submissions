class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1d = {}
        s2d = {}
        x =0 
        n = len(s1)
        n2 = len(s2)
        for i in range(97,123):
            s1d[chr(i)] = 0
            s2d[chr(i)] = 0
        for i in s1:
            s1d[i] += 1
            if x<n2:
                s2d[s2[x]] += 1
                x+=1
        if s1d == s2d:
                return True
        for i in range(len(s2)-len(s1)):
            s2d[s2[i]] -= 1
            s2d[s2[i+n]] += 1
            if s1d == s2d:
                return True
            i+=1
        return False
