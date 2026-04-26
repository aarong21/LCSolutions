class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # mapp = {}
        # for num in nums:
        #     mapp[num] = mapp.get(num,0)+1
        # for num in mapp:
        #     if mapp[num] == 1:
        #         return num
        # return -1
        xor = 0
        for num in nums:
            xor ^= num
        return xor