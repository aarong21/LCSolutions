class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # sorting array
        counting = [0 for _ in range(2 * 5 * 10**4 + 1)]
        for num in nums:
            # add 5*10^4 to account for smallest element
            counting[num + 5 * 10**4] += 1
        write_ind = 0
        for number_ind, freq in enumerate(counting):
            while freq != 0:
                nums[write_ind] = number_ind - 5 * 10**4
                write_ind += 1
                freq -= 1
        return nums

        # # bubble sort --> too long
        # n = len(nums)
        # for i in range(n-1,0,-1):
        #     for j in range(i):
        #         if nums[j] > nums[j+1]:
        #             nums[j],nums[j+1] = nums[j+1],nums[j]
        # return nums

        