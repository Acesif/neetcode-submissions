import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub("[^a-zA-Z0-9]","",s)
        r=len(s)-1
        l=0
        while(l<r):
            if(s[l].lower() == s[r].lower()):
                l+=1
                r-=1
            else:
                return False
        return True

        