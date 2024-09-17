class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        res = []
        s1_words = s1.split()
        s2_words = s2.split()
        all_words = s1_words + s2_words
        all_words = Counter(all_words)

        return [word for word in all_words if all_words[word] == 1]