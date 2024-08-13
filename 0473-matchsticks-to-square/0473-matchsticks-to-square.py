class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        # Base cases
        # Square should be able to be made
        totalLength = sum(matchsticks)
        if totalLength % 4 != 0 or max(matchsticks) > totalLength // 4:
            return False
        targetLen = totalLength // 4
        matchsticks.sort(reverse=True)

        def can_partition(k, target):
            buckets = [0] * k
        
            def backtrack(idx):
                # If all elements have been used, check if all are equal.
                if idx == len(matchsticks):
                    return len(set(buckets)) == 1
                
                # Try placing numbers in each bucket.
                for b in range(k):
                    buckets[b] += matchsticks[idx]
                    if buckets[b] <= target and backtrack(idx + 1):
                        return True
                    buckets[b] -= matchsticks[idx]
                    
                    # Pruning: Buckets are filled from left to right. If any bucket remains empty,
                    # then all buckets to the right of it will also be empty.
                    if buckets[b] == 0:
                        break
                
                return False
            
            return backtrack(0)
        return can_partition(4, targetLen)

