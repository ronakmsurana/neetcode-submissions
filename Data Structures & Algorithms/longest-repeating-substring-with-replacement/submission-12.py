class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n=len(s)
        t_max = 0
        for c in set(s):
            l = 0
            r = 0
            cur_k = k
            cur_max = 0
            while r<n:
                while r<n and (s[r] == c or cur_k):
                    if s[r]!=c: 
                        cur_k -=1
                    r+=1
                cur_max = max(cur_max, r-l)
                # print(c,l,r,cur_k)
                if cur_k<=0:
                    while l<r and s[l] == c:
                        l+=1
                    l+=1
                    cur_k +=1
                # print(c,l,r,cur_k)
                # print(" a----")
            t_max = max(cur_max,t_max)
        return t_max

