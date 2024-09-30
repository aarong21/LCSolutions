class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxArea = 0
        start, end = 0, len(height)-1
        while start < end:
            h = min(height[start], height[end])
            area = h * (end - start)
            maxArea = max(area, maxArea)

            if height[start] < height[end]: # front shorter
                start += 1
            else: # back shorter
                end -= 1
        return maxArea