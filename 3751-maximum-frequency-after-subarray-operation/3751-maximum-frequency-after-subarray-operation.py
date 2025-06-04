class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        base = sum(v==k for v in nums) # freq of k in arr
        max_gain = 0

        for x in range(-50, 51):
            diff = k - x
            if diff == k or not (1<=diff<=50):
                continue

            cur = 0
            for num in nums:
                if num == diff:
                    cur += 1
                elif num == k:
                    cur -= 1
                if cur < 0:
                    cur = 0
                max_gain = max(max_gain, cur)
        return base + max_gain