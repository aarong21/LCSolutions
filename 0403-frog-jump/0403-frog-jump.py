class Solution:
    def canCross(self, stones: List[int]) -> bool:
        end = stones[-1]
        memo = {}
        stone_set = set(stones)

        def dfs(k: int, pos: int) -> bool:
            # reached?
            if pos == end:
                return True
            # evaluated before?
            if (k,pos) in memo:
                return memo[(k,pos)]
            # if not, try next jumps
            for jump in range(k-1, k+2):
                if jump>0 and pos+jump in stone_set and dfs(jump, jump+pos):
                    memo[(k,pos)] = True
                    return True
            # else dead end
            memo[(k, pos)] = False
            return False
    
        if 0 in stones and 1 in stones:
            return dfs(1,1)