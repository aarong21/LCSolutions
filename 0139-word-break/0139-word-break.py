class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        words = set(wordDict)

        dp = [False] * (n+1)
        # first element represents empty string
        dp[0] = True

        for i in range(1, n+1):
            for j in range(i):
                # checking if substring j to i is in dict
                if dp[j] and s[j:i] in words:
                    dp[i] = True
                    # no need to check more substrings
                    break
        
        return dp[n]
# ------------------------------------------------------
        from collections import Counter
        dic = Counter(s)
        n = len(s)
        flag = False

        for word in wordDict:
            for char in word:
                if dic[char] > 0:
                    dic[char] -= 1
                    n -= 1
                    if dic[char] == 0:
                        flag = True
                else:
                    continue
        
        if n == 0 and flag:
            return True
        return False