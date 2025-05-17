class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lett = set()
        left, right = 0, 0
        longest = 0
        for i in range(len(s)):
            while s[i] in lett:
                lett.remove(s[left])
                left += 1
            lett.add(s[right])
            right += 1
            longest = max(longest, right-left)
        return longest