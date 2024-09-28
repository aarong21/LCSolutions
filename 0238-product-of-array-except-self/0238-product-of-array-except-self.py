class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1]*len(nums)

        # first fill array with products from left
        left = 1
        for i in range(len(ans)):
            ans[i] = left
            left *= nums[i]
        # then go backwards and multiply from right side
        right = 1
        for i in range(len(ans)-1, -1, -1):
            ans[i] *= right
            right *= nums[i]
        return ans