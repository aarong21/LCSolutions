class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        from collections import deque
        n = len(nums1)
        queue = deque(sorted(nums1))
        # sorting nums2 by indice of largest to smallest num
        order = sorted(range(n), key=lambda x: nums2[x], reverse=True)
        res = [0]*n
        print(order)
        for item in order:
            # if highest in n1 is greater than highest in n2, set
            if queue[-1] > nums2[item]:
                res[item] = queue.pop()
            # else just assign it lowest so next highest has chance
            else:
                res[item] = queue.popleft()
        return res