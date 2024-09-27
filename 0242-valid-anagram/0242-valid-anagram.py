class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False

        letts = Counter(s)
        for let in t:
            letts[let] -= 1
        
        for item in letts.values():
            if item != 0:
                return False
        return True