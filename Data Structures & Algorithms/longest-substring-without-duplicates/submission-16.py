class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ss = {}
        max_length = 0
        last_unique = 0
        for i in range(len(s)):
            prev = ss.setdefault(s[i],i)
            if  prev != i: 
                max_length = max(max_length,i-last_unique)
                last_unique = max(prev+1,last_unique)
                ss[s[i]] = i
            if max_length == len(set(s)): 
                break
        if max_length != len(set(s)):
            max_length = max(max_length,len(s) - last_unique)
        return max_length


        