class Solution:

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sdict={}
        for s in strs:
            key = "".join(sorted(s))
            sdict.setdefault(key, []).append(s)
        return list(sdict.values())
        