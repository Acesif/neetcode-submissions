class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == " ":
            return 1
        if s == "":
            return 0
        if len(s) == 1:
            return 1
        maxLen = 1
        l,r=0,0
        x=""
        while(r<len(s)):
            while s[r] in x:
                l+=1
                x=s[l:r]
            x+=s[r]
            maxLen = max(maxLen, (r-l)+1)
            r+=1
        return maxLen
        