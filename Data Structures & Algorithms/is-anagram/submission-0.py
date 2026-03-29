class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # dumb way
        # for i in range(len(s)):
        #    for j in range(len(t)):
        #        if s[i] == t[j]:
        #            if j!=len(t)-1:
        #                t = t[:j] + t[j+1:]
        #            else:
        #                t = t[:j]
        # if len(s) == len(t) == 0:
        #    return True
        # else:
        #    return False
        if len(s)!=len(t):
            return False
        wordDict = {}
        for i in range(len(s)):
            if s[i] not in wordDict:
                wordDict[s[i]] = 1
            else:
                wordDict[s[i]]+=1
        for j in range(len(t)):
            if t[j] not in wordDict:
                return False
            else:
                wordDict[t[j]]-=1
        return True

        