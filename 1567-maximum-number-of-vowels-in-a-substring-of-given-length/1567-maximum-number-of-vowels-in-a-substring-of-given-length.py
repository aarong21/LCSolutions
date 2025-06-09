class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a','e','i','o','u'}

        if not s or k > len(s):
            return 0

        curr_count = sum(1 for i in range(k) if s[i] in vowels)
        max_count = curr_count

        for i in range(k, len(s)):
            if s[i-k] in vowels:
                curr_count -= 1
            if s[i] in vowels:
                curr_count += 1
            
            max_count = max(curr_count, max_count)

            # optimization
            if max_count == k:
                break
        return max_count

