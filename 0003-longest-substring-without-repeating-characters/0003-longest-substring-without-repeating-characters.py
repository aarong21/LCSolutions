class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lett = set()
        left = 0
        count = 0

        for right in range(len(s)):
            while(s[right] in lett):
                lett.remove(s[left])
                left += 1
            lett.add(s[right])
            count = max(count, len(lett))
        return count