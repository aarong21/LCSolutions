class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        search = -1
        while left <= right:
            mid = (right + left) // 2
            if nums[mid] == target:
                return mid
            
            # left side
            if nums[mid] >= nums[left]: # right of left
                if target > nums[mid] or target < nums[left]:
                    left = mid + 1
                else: # left of left
                    right = mid - 1
            # right side
            else:
                if target < nums[mid] or target > nums[right]: # left of right
                    right = mid-1
                else: # right of right
                    left = mid + 1
        return search
            