class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list) # allows for new lists

        for st in strs:
            lis = [0]*26 # list of all letters in string
            for s in st:
                lis[ord(s)-ord('a')] += 1 # numerically ordered as opposed to char
            ans[tuple(lis)].append(st) # use list as key and have words as values

        return ans.values()