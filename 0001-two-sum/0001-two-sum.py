class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapp = {}
        for i in range(len(nums)):
            num = nums[i]
            if target-num in mapp:
                return [i, mapp[target-num]]
            mapp[num] = i 
        return []