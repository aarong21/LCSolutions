class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        count = 0
        for num in nums:
            heapq.heappush(heap, num*-1)
        while count < k:
            temp = heapq.heappop(heap)
            count += 1
        return temp*-1
