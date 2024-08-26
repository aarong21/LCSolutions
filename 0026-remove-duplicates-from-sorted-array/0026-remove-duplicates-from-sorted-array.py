class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        num = 0
        umap = {}
        for i in range(len(nums)):
            if nums[i] not in umap:
                umap[nums[i]] = 1
                nums[i], nums[num] = nums[num], nums[i]
                num += 1
        return num
