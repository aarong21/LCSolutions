class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        minVal, maxVal = arrays[0][0], arrays[0][-1]
        maxDist = 0

        for i in range(1, len(arrays)):
            arr = arrays[i]
            maxDist = max(maxDist, abs(arr[-1]-minVal), abs(maxVal-arr[0]))
            minVal = min(minVal, arr[0])
            maxVal = max(maxVal, arr[-1])
        return maxDist