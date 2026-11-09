class Solution:
    def isValid(self, s: str) -> bool:
        a = []
        br = {')':'(','}':'{',']':'['}
        for i in s:
            if i in {'(','{','['}:
                a.append(i)
            else:
                if not a or a.pop() != br[i]:
                    return False
        if not a:
            return True
        return False
                
        