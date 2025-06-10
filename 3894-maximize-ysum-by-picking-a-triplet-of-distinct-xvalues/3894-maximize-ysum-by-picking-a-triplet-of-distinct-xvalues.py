class Solution:
    def maxSumDistinctTriplet(self, x: List[int], y: List[int]) -> int:
        n = len(x)
        x_to_y = {}
        for i in range(n):
            if x[i] not in x_to_y or y[i] > y[x_to_y[x[i]]]:
                x_to_y[x[i]] = i
        
        if len(x_to_y) < 3:
            return -1
        
        ind = list(x_to_y.values())
        ind.sort(key=lambda i: y[i], reverse=True)

        best = ind[:3]
        return sum(y[i] for i in best)