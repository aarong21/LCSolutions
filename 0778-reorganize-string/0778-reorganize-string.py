class Solution:
    def reorganizeString(self, s: str) -> str:
        # frequency list of char in s
        count = defaultdict(int)
        for c in s:
            count[c] += 1
        
        # if count(char) > len(s)//2, impossible
        if any(freq > (len(s)+1)//2 for freq in count.values()):
            return ""
        
        # max heap (-freq, char)
        heap = [(-freq, char) for char, freq in count.items()]
        heapq.heapify(heap)
        res = ""
        ###
        prev_freq = 0
        prev_char = ''
        while heap:
            freq, char = heapq.heappop(heap)
            res += char
            freq += 1
            if prev_freq < 0:
                heapq.heappush(heap, (prev_freq,prev_char))
            prev_freq, prev_char = freq, char
        return res

