class Solution:
    def rob(self, nums: List[int]) -> int:
        temp1, temp2 = 0, 0

        for n in nums:
            temp = max(temp1+n, temp2)
            temp1 = temp2
            temp2 = temp
        return temp2