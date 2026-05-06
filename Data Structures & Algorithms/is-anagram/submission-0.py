class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        charDict = {}
        for i in range(len(s)):
            if s[i] not in charDict:
                charDict[s[i]] = 1
            else:
                charDict[s[i]] += 1

        for i in range(len(t)):
            if t[i] not in charDict or charDict[t[i]] == 0:
                return False
            charDict[t[i]] = charDict[t[i]] - 1
        
        return True