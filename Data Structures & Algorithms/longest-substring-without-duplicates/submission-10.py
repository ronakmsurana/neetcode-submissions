class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dc = {}
        max_len = l = 0
        best_len = len(set(s))

        for r, ch in enumerate(s):
            if ch in dc:
                l = max(l, dc[ch] + 1)
            dc[ch] = r
            max_len = max(max_len, r - l + 1)
            
            if max_len == best_len:
                break
        
        return max_len