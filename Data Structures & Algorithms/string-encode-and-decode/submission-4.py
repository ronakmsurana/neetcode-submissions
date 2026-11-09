class Solution:

    def encode(self, strs: List[str]) -> str:
        return "€".join(i for i in strs) if strs else "₹"

    def decode(self, s: str) -> List[str]:
        return s.split("€") if s!="₹" else []
