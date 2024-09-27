class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        count = Counter(nums)
        for el in count.keys():
            if count[el] > 1:
                return True
        return False