class Solution:
    def longestPalindrome(self, s: str) -> str:

        def substring_finder(left, right):
            while left >=0 and right < len(s) and s[left] == s[right]:
                left -=1
                right +=1
            return s[left+1:right]

        longest = ""
        for i in range(len(s)):
            palindrome = substring_finder(i,i)
            if len(palindrome) > len(longest):
                longest = palindrome
            palindrome = substring_finder(i,i+1)
            if len(palindrome) > len(longest):
                longest = palindrome
        return longest