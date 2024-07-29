class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}
        for i in range(len(nums)):
            # if other val exists, return
            other = target-nums[i]
            if other in hash and hash.get(other)!=i:
                return [i, hash[other]]
            else:
                hash[nums[i]] = i
        return []