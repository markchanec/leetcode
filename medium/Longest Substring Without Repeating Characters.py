def getSubString(s):
    sub = ""
    for i in range(len(s)):
        if s[i] not in sub:
            sub+=s[i]
        else:
            break
    return sub

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longestSub = ""

        for i in range (len(s)):
            sub = getSubString(s[i:])
            if len(sub) > len(longestSub):
                longestSub = sub

        return len(longestSub)
