class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {}
        for ind in range(len(nums)):
            num = nums[ind] # the number value
            if target-num in hm:
                return [ind,hm[target-num]]
            hm[num] = ind # number : index
        return []