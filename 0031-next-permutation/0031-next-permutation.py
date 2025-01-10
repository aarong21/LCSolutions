class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pivot = None
        # find pivot index
        for i in range(len(nums)-1, 0, -1):
            if nums[i] > nums[i-1]:
                # first number thats decreasing from the right side is the pivot
                pivot = i-1
                break
        else:
            # no decreasing means return the array sorted
            nums.reverse()
            return
        
        # find the next highest number from pivot to swap with
        swap = len(nums)-1
        while nums[swap] <= nums[pivot]:
            swap -= 1
        # swap with it
        nums[swap], nums[pivot] = nums[pivot], nums[swap]
        # reverse order of right side since its in increasing order from right side
        nums[pivot+1:] = reversed(nums[pivot+1:])
        return