class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count ={}
        if len(s)!=len(t):
            return False
        for i in range(len(s)):
            count[s[i]] = count.get(s[i], 0) + 1
            count[t[i]] = count.get(t[i], 0) - 1
        a = set(count.values())
        return len(a) == 1 and 0 in a

