class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxlen = 0
        wrds = set()
        l = 0
        for r in range(len(s)):
            while s[r] in wrds:
                
                wrds.remove(s[l])
                l+=1
            wrds.add(s[r])
            maxlen = max(r-l+1, maxlen)
        return maxlen
            