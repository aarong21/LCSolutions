class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]]
            
        result = [[]]

        for num in nums:
            result += [subset + [num] for subset in result]

        return result