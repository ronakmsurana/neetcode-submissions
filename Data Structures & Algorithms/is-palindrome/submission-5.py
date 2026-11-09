class Solution:
    def isPalindrome(self, s: str) -> bool:
        i=0
        s = s.lower()
        for i in s:
            if (i.isalnum()) != True:
                s=s.replace(i,"")
        n=len(s)
        i=0
        while i<n/2:
            if s[i]!=s[-(i+1)] :
                return False
            i+=1
        return True
