class Solution:
    def wordBreak(self, s: str, wordDict: List[str], map: dict[str, List[str]] = None) -> List[str]:
        if map is None:
            map = {}
        elif s in map:
            return map[s]
        
        # build list of sentences to be made from s
        res = []

        # check which words match start of s
        for word in wordDict:
            if s.startswith(word):
                if s == word:
                    res.append(word)
                else:
                    # find all sentences for remainder of s
                    following = self.wordBreak(s[len(word):], wordDict, map)
                    for sub in following:
                        res.append(word + ' ' + sub)
            map[s] = res
        return res
        