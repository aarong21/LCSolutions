class Solution:
    def reorganizeString(self, s: str) -> str:
        # 1: count freq of each char
        freq = {}
        for char in s:
            freq[char] = freq.get(char, 0) + 1
        # 2: create max heap to order freq
        max_heap = [(-count, char) for char, count in freq.items()]
        heapq.heapify(max_heap)
        # 3: build the return string
        result = []
        prev_c = None
        prev_count = 0
        
        while max_heap:
            count, char = heapq.heappop(max_heap)
            result.append(char)
            
            if prev_count < 0:
                heapq.heappush(max_heap, (prev_count, prev_c))
            prev_c = char
            prev_count = count + 1
        # 4: return the return string
        ret_str = "".join(result)
        if len(ret_str) != len(s):
            return ""
        return ret_str