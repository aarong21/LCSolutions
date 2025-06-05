class Solution:
    def trap(self, height: List[int]) -> int:
        if not height or len(height) < 3:
            return 0
        
        left, right = 0, len(height)-1 # two pointer
        left_max = right_max = 0 # highest bar from both sides
        trapped = 0

        while left < right:
            if height[left] < height[right]:
                if height[left] >= left_max:
                    left_max = height[left] # update left max if new max
                else:
                    trapped += left_max - height[left] # add trapped 
                left += 1
            else:
                if height[right] >= right_max:
                    right_max = height[right] # update right max
                else:
                    trapped += right_max-height[right] # add trapped
                right -=1
        return trapped