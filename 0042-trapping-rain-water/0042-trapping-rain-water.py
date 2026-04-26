class Solution:
    def trap(self, height: List[int]) -> int:
        
        area = 0
        left, right = 0,len(height)-1
        left_max, right_max = height[left], height[right]
        while left < right:
            if left_max < right_max:
                left += 1
                left_max = max(height[left], left_max)
                area += left_max - height[left]
            else:
                right -= 1
                right_max = max(height[right], right_max)
                area += right_max - height[right]

        return area