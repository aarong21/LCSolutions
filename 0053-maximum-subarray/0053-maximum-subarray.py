class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # currsum, maxsum = 0, nums[0]
        # for i in nums:
        #     currsum += i
        #     maxsum = max(currsum, maxsum)
        #     if (currsum < 0):
        #         currsum = 0
        # return maxsum
        curr,maxS = 0,nums[0]
        for i in nums:
            curr = max(i, curr+i)
            maxS = max(curr, maxS)
        return maxS