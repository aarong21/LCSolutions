class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word = ""
        ind1, ind2 = 0,0

        while ind1 < len(word1) and ind2 < len(word2):
            if word1[ind1]:
                word += word1[ind1]
                ind1 += 1
            if word2[ind2]:
                word += word2[ind2]
                ind2 += 1
        
        if ind1 < len(word1):
            word += word1[ind1:]
        if ind2 < len(word2):
            word += word2[ind2:]
    
        return word
            