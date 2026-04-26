class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1]*n
        post = 1

        for i in range(1, n):
            answer[i] = nums[i-1]*answer[i-1]

        for i in range(n-1, -1, -1):
            answer[i] *= post
            post *= nums[i]
        return answer