class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len (t):
            return False

        inputS = []
        inputT = []

        for i in s:
            inputS.append(i)
        for j in t:
            inputT.append(j)
        inputS.sort()
        inputT.sort()

        return inputS == inputT