class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = 0
        end = 0 # back of sliding window
        seen = set()

        for i in range(len(s)):
            while s[i] in seen:
                seen.remove(s[end])
                end += 1 # move back of sliding window to current repeat character
            seen.add(s[i])
            count = max(count, i - end + 1)
        return count
        

