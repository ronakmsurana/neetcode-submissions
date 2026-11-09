class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ns = len(s)
        nt = len(t)
        l=0
        r=0
        resl = resr = 0
        reslen = ns+1
        min_l = ns
        nt_d = {}
        win = {}
        for i in t:
            nt_d[i] = nt_d.setdefault(i,0) + 1
            win[i] = 0
        matches = 0
        want = len(nt_d)
        for r in range(ns):
            c = s[r]
            win[c] = win.setdefault(c,0) + 1
            if c in nt_d and win[c] == nt_d[c]:
                matches +=1
            while matches == want:
                if (r-l+1 < reslen):
                    reslen = r-l+1
                    resr,resl = r,l
                win[s[l]] -= 1
                if s[l] in nt_d and win[s[l]] < nt_d[s[l]]:
                    matches -= 1
                l +=1
        return s[resl:resr+1] if reslen <ns+1 else ""




            

        