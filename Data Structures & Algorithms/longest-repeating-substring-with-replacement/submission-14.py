class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0
        l = 0
        maxf = 0 # Tracks the most frequent character in the current window
        
        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1
            maxf = max(maxf, count[s[r]])
            
            # If (window size) - (most frequent char count) > k, window is invalid
            while (r - l + 1) - maxf > k:
                count[s[l]] -= 1
                l += 1
                
            res = max(res, r - l + 1)
            
        return res