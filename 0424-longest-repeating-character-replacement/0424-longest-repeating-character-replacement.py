class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        window = 0
        left = 0

        # move sliding window forward
        for right in range(len(s)):
            count[s[right]] = 1 + count.get(s[right], 0)
            # if more replacements than k are needed, move left side over
            while ((right - left + 1) - max(count.values())) > k:
                count[s[left]] -= 1
                left += 1
            
            window = max(window, right - left + 1)

        return window