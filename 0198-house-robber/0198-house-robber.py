class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {len(nums): 0, len(nums)+1: 0}
        # houses beyond end cannot be robbed

        def rob_from(n):
            if n not in memo:
                memo[n] = max(
                    # rob this house and skip next
                    nums[n]+rob_from(n+2),
                    # skip this house
                    rob_from(n+1)
                )
            return memo[n]
        
        return rob_from(0)
        
        # temp1, temp2 = 0, 0

        # for n in nums:
        #     temp = max(temp1+n, temp2)
        #     temp1 = temp2
        #     temp2 = temp
        # return temp2