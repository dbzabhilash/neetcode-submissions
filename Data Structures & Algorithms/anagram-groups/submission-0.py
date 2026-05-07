class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        myDict = {}
        for s in strs:
            alphaNumList = [0] * 26
            for ch in s:
                alphaNumList[ord(ch) - ord('a')] += 1
            if tuple(alphaNumList) not in myDict:
                myDict[tuple(alphaNumList)] = [s]
            else:
                myDict.get(tuple(alphaNumList), []).append(s)
        return list(myDict.values())