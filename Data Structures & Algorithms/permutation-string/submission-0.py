class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        for i in range(len(s2)-len(s1)+1):
            if set(s1) == set(s2[i:i+len(s1)]) and all(s1.count(j) == s2[i:i+len(s1)].count(j) for j in list(set(s2))):
                
                return True
        return False
