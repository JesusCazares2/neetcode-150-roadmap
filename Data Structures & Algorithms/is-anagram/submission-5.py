class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        resultS = "".join(sorted(s))
        resultT = "".join(sorted(t))

        return resultS == resultT