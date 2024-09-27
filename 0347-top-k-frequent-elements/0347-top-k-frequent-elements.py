class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        bucket = [[] for i in range(len(nums)+1)] # bucket sort

        # fill frequency hash table
        for num in nums:
            freq[num] = 1 + freq.get(num, 0)
        # in bucket list, have freq:[items with that freq]
        for num, amt in freq.items():
            bucket[amt].append(num)
        
        res = []
        # backwards it thru bucket and add to res
        for i in range(len(bucket)-1, 0, -1):
            for count in bucket[i]:
                res.append(count)
                # when res size is equal to top k, return
                if len(res) == k:
                    return res
