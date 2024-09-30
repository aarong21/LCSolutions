class Solution:
    def isPalindrome(self, s: str) -> bool:
        word = ""
        for i in s:
            if i.isalnum():
                word += i
    
        a, b = 0, len(word)-1
        while a < b:
            while not word[a].isalnum():
                a+=1
            while not word[b].isalnum():
                b-=1
            if word[a].lower() != word[b].lower():
                return False
            a += 1
            b -= 1
        return True